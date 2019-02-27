from flask import Flask, request,jsonify,send_from_directory
from bs4 import BeautifulSoup 
import requests
import os
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from files.newsapi import getNewsUpdates
from files.geo import getCity
from files.aboutflu import parseCsvFolder
import datetime
#DATABASE_URL: postgres://oipfsfiayphqsu:b9d7b026fc00203e471d8c9020284a2fd6285516ef8f50230dfef22379a7f374@ec2-50-17-193-83.compute-1.amazonaws.com:5432/d5lvt5aov2s0ou

app = Flask(__name__)

DATABASE_DEFAULT = 'postgresql://postgres:14051976@localhost/fludb'
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_DEFAULT

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.debug = True
db = SQLAlchemy(app)

class User(db.Model):


   __tablename__ = 'user_table'

   id = db.Column(db.Integer,primary_key = True)
   uid = db.Column(db.String(80),unique = True)
   timestamp = db.Column(db.DateTime)
   lat = db.Column(db.Float)
   lon = db.Column(db.Float)
   hasflu = db.Column(db.Boolean)

   def __init__(self,uid,timestamp,lat,lon,hasflu):
      self.uid = uid
      self.timestamp = timestamp
      self.lat = lat
      self.lon = lon
      self.hasflu = hasflu

   def __repr__(self):
      return '<uid %r>' %self.uid

class flunews(db.Model):

   __tablename__ = 'news'

   id = db.Column(db.Integer,primary_key = True)
   newsjson = db.Column(db.JSON)

   def __init__(self,newsjson):
      self.newsjson = newsjson

   def __repr__(self):
      # return '%r' %self.
      return self.newsjson

class fludetail(db.Model):
   __tablename__ = 'fludeatil'

   id = db.Column(db.Integer,primary_key = True)
   flujson = db.Column(db.JSON)

   def __init__(self,flujson):
      self.flujson = flujson

   def __repr__(self):
      return self.flujson


@app.route('/')
def index():
   # r = requests.get("https://google.com")
   # s = BeautifulSoup(r.content,'lxml')
   #
   return os.path.join(app.root_path, 'flucsv') #"hi there brother 123 %s" %r.status_code


@app.route('/a',methods = ['GET','POST'])
def addNews():

   if request.method == 'GET':
      flunews.query.delete()
      news_data = getNewsUpdates()
     
      y = json.dumps(news_data) #this is a json

      mynews = flunews(y)
      db.session.add(mynews)
      db.session.commit()
      return "news done"
   else:
      data = flunews.query.first()
      val = json.loads(str(data)) #this is a dict
      return jsonify(val) 



@app.route('/add',methods = ['GET','POST'])
def post_user():
    if request.method == 'POST':
        #TODO clear all data in db
        User.query.delete()
        u = request.args.get('u')
        user = User(u)
         
        db.session.add(user)
        db.session.commit()
        return "done"
    else:

        lis = []
        data = User.query.first()
        data = {
            'username':data.username,
        }
         
        return jsonify(data)


###to get FLU DATA####

@app.route('/h',methods = ['GET','POST'])
def OnApi():
   return "hi"

@app.route('/f')
def OneApi():

  
   lat = request.args.get('lat')
   lon = request.args.get('lon')
   hasflu = request.args.get('hasflu')
   uid = request.args.get('uid')
   timestamp = datetime.datetime.now()
      #   save to user table
   User.query.delete()
   user = User(uid,timestamp,lat,lon,hasflu)
   db.session.add(user)
   db.session.commit()

   user_location = getCity(lat,lon)
   country = user_location[0]
   code = user_location[1]
   data = flunews.query.first()
   l = json.loads(str(data)) #this is a dict


   SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
   folder_path = os.listdir(os.path.join(SITE_ROOT,'flucsv'))
      # print(folder_path)
      # print("root : %s"% SITE_ROOT)
   # folder_path = os.path.join(app.root_path, 'flucsv')
   d = parseCsvFolder(folder_path,SITE_ROOT)
      
   data_out = {


      'country':country,
      'code':code,
      'fludata': d,
      'news':l,
      }
   # data_out ={
   #    'e':'test'
   # }
   return jsonify(data_out)
  
     




