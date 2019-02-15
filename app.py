from flask import Flask
from bs4 import BeautifulSoup 
import requests
app = Flask(__name__)

@app.route('/')
def index():
   r = requests.get("https://google.com")
   s = BeautifulSoup(r.content,'lxml')
   return "hi there bro %s" %r.status_code
