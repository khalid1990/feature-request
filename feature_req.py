from flask import Flask, request, redirect, url_for, render_template, flash
from forms import FeatureReqForm
from flask_bootstrap import Bootstrap
from models import db, FeatureRequest
from config import APP_SECRET_KEY, Config
from feature_req_service import check_feature_req_with_same_priority_for_client, \
                                update_all_feature_req_with_equal_greater_priority

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
app.config.from_object(Config())
bootstrap = Bootstrap(app)

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/', methods = ['GET', 'POST'])
def feature_request():
    form = FeatureReqForm()
    if form.validate_on_submit():
        feature_req = FeatureRequest()
        form.populate_obj(feature_req)
        client_id = form.client.data
        priority = form.client_priority.data
        messages = []
        if check_feature_req_with_same_priority_for_client(client_id, priority, db):
            messages = update_all_feature_req_with_equal_greater_priority(client_id, priority, db)

        db.session.add(feature_req)
        db.session.commit()

        flash('New feature request {} is added successfully with priority {}.'
            .format(form.title.data, form.client_priority.data))
        for message in messages:
            flash(message)

        return redirect(url_for('done'))
        
    return render_template('feature.html', form=form)    

@app.route('/done')
def done():
    return render_template('done_page.html')

if __name__ == '__main__':
    app.run()
