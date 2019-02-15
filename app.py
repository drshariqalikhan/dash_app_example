from flask import Flask
from bs4 import BeautifulSoup 
import requests
app = Flask(__name__)

@app.route('/')
def index():
   r = requests.get("https://google.com")
   # s = bs(r,'lxml')
   return "hi %s" %r.status_code
