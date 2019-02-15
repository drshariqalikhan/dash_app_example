from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def index():
   code = requests.get("https://google.com")
   return "hi %s" %code.status_code
