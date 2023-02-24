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
     sauces = {k: v for k, v in (os.environ).items() if k.startswith('sauce0')}
     sauces = list(sauces.values())
   except KeyError: 
     sauces = 'null' 

   return render_template('index.html', environment=environment, sauces=sauces )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
   app.run()