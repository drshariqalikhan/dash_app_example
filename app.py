from flask import Flask, request,jsonify,send_from_directory
from bs4 import BeautifulSoup 
import requests
import os
import json
# from files.parser import parse_page
# from files.search import searchFor
# from files.rediffapi import getNewsUpdates
# from files.geo import getCity


app = Flask(__name__)

@app.route('/')
def index():
   r = requests.get("https://google.com")
   s = BeautifulSoup(r.content,'lxml')
   return "hi there brother 123 %s" %r.status_code

