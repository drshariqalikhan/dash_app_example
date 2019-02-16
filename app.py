from flask import Flask, request,jsonify
from bs4 import BeautifulSoup 
import requests
import os
import json
from files.parser import parse_page
from files.search import searchFor


app = Flask(__name__)

@app.route('/')
def index():
   r = requests.get("https://google.com")
   s = BeautifulSoup(r.content,'lxml')
   return "hi there bro 123 %s" %r.status_code

@app.route('/a')
def func():
   parse_page()

   out = {
      'scrape':'done'
   }

   return jsonify(out)


@app.route('/b')
def apifunc():
   SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
   json_uri = os.path.join(SITE_ROOT,'files/apidata.json')
   return jsonify(json.load(open(json_uri)))
   # return "hi"


@app.route('/c')
def searchFunc():
   search_item = request.args.get('q')
   l = searchFor(search_item)
   return jsonify(l)
   # return "hi"

