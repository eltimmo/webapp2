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
      proteins = (os.environ['proteins']).split(",")
    except KeyError: 
      proteins = 'null'     

    try:  
      sauces = {key: value for key, value in (os.environ).items() if key.startswith('sauce0')}
      sauces = list(sauces.values())
    except KeyError: 
      sauces = 'null' 

    return render_template('index.html', environment=environment, sauces=sauces )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/health')
def health():
    
    try:  
      environment = os.environ['environment']
      response_code = "200"
    except KeyError: 
      response_code = "500"
      
    return response_code

if __name__ == '__main__':
    app.run()
