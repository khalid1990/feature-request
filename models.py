from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class FeatureRequest(db.Model):
    __tablename__ = 'feature_request'
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(256), nullable=False)
    client = db.Column(db.Integer(), nullable=False)
    client_priority = db.Column(db.Integer(), nullable=False)
    target_date = db.Column(db.Date(), nullable=False)
    product_area = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    created = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
