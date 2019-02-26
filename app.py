from flask import Flask, request,jsonify,send_from_directory
from bs4 import BeautifulSoup 
import requests
import os
import json
from flask_sqlalchemy import SQLAlchemy

# from files.parser import parse_page
# from files.search import searchFor
# from files.rediffapi import getNewsUpdates
# from files.geo import getCity
#DATABASE_URL: postgres://oipfsfiayphqsu:b9d7b026fc00203e471d8c9020284a2fd6285516ef8f50230dfef22379a7f374@ec2-50-17-193-83.compute-1.amazonaws.com:5432/d5lvt5aov2s0ou

app = Flask(__name__)

DATABASE_DEFAULT = 'postgresql://postgres:14051976@localhost/flaskmovie'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.debug = True
db = SQLAlchemy(app)

class User(db.Model):

   id = db.Column(db.Integer,primary_key = True)
   username = db.Column(db.String(80),unique = True)
   email = db.Column(db.String(120),unique = True)

   def __init__(self,email):

      self.username = username
      self.email = email

   def __repr__(self):
      return '<User %r>' %self.username



@app.route('/')
def index():
   r = requests.get("https://google.com")
   s = BeautifulSoup(r.content,'lxml')
   return "hi there brother 123 %s" %r.status_code


@app.route('/add',methods = ['GET','POST'])
def post_user():
    if request.method == 'POST':
        #TODO clear all data in db
        User.query.delete()
        # u = request.args.get('u')
        e = request.args.get('e')
        user = User(e)
        db.session.add(user)
        db.session.commit()
        return "done"
    else:

        lis = []
        data = User.query.first()
        data = {
            # 'username':data.username,
            'email':data.email
        }
         
        return jsonify(data)

