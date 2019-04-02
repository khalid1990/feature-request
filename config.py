import os
project_dir = os.path.abspath(os.path.dirname(__file__))
APP_SECRET_KEY = 'The app secret key'

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(project_dir, 'isw.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
