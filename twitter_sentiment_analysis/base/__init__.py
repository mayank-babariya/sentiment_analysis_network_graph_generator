from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import warnings
from datetime import timedelta

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app=Flask(__name__)
app.secret_key='assignment_2'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config['TESTING']=True
app.config['SQLALCHEMY_TRACK_MODIFICATION']=True
app.config['SQLALCHEMY_ECHO']= False
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1111@localhost:5432/sentiment_analysis'
app.config['SQLALCHEMY_MAX_OVERFLOW']=0
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
db=SQLAlchemy(app)
app.app_context().push()

import base.com.controller