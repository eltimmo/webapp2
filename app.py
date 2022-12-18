from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route('/')

def index():

   try:  
     environment = os.environ['environment'] 
   except KeyError: 
     environment = 'null'

   try:  
     secret = os.environ['secret'] 
   except KeyError: 
     secret = 'null'

   return render_template('index.html', environment=environment, secret=secret )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
   app.run()