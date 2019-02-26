from flask import Flask, request,jsonify,send_from_directory
from bs4 import BeautifulSoup 
import requests
import os
import json
from flask_sqlalchemy import SQLAlchemy
from models import User

# from files.parser import parse_page
# from files.search import searchFor
# from files.rediffapi import getNewsUpdates
# from files.geo import getCity
#DATABASE_URL: postgres://oipfsfiayphqsu:b9d7b026fc00203e471d8c9020284a2fd6285516ef8f50230dfef22379a7f374@ec2-50-17-193-83.compute-1.amazonaws.com:5432/d5lvt5aov2s0ou


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://oipfsfiayphqsu:b9d7b026fc00203e471d8c9020284a2fd6285516ef8f50230dfef22379a7f374@ec2-50-17-193-83.compute-1.amazonaws.com:5432/d5lvt5aov2s0ou'
DATABASE_DEFAULT = 'postgresql://postgres:14051976@localhost/flaskmovie'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# heroku = Heroku(app)
db = SQLAlchemy(app)

@app.route('/')
def index():
   r = requests.get("https://google.com")
   s = BeautifulSoup(r.content,'lxml')
   return "hi there brother 123 %s" %r.status_code


@app.route('/db')
def dbase():
   data = User.query.first()

   data = {
      'email': data.email
   }
   
   return jsonify(data)
