from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():

    if "environment" in os.environ:
        environment = os.environ['environment']
    else:
        environment = None

    if "proteins" in os.environ:
        proteins = (os.environ['proteins']).split(",")
    else:
        proteins = [None]

    if "sauces" in os.environ:
        sauces = {key: value for key, value in (os.environ).items() if key.startswith('sauce0')}
        sauces = list(sauces.values())
    else:
        sauces = [None]

    return render_template('index.html', environment=environment, sauces=sauces, proteins=proteins )

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
