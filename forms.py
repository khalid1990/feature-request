from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, NumberRange, Length
import datetime

class FeatureReqForm(FlaskForm):
    title = TextField("Title", 
        validators=[DataRequired("Please enter a title"), 
        Length(max=250, message="Title should be maximum 250 character long")])
    client = SelectField("Client", choices=[
        ('', '--- Please select a client ---'),
        ('9001', 'Client A'),
        ('9002', 'Client B'),
        ('9003', 'Client C')
    ], validators=[DataRequired()])
    client_priority = IntegerField("Priority", 
        validators = [DataRequired("Please Enter a positive number"), NumberRange(min=1)])
    target_date = DateField("Target date", validators = [DataRequired()], format="%m/%d/%Y")
    product_area = SelectField("Product Area", choices=[
        ('', '--- Please select a Product Area ---'),
        ('PL', 'Policies'),
        ('BL', 'Billing'),
        ('CL', 'Claims'),
        ('RP', 'Reports')
    ], validators = [DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired(), 
        Length(max=1000, message="Description should be maximum 1000 characters long")])
    submit_button = SubmitField("Add")

    def validate(self):
        v = FlaskForm.validate(self)
        if not v:
            return False
        target_date = self.target_date.data
        if target_date < datetime.date.today():
            self.target_date.errors.append("Past date not allowed")
            return False

        return True
