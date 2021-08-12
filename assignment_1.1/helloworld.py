from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/users/<string:username>')
def hello_world(username='MyName'):
    return("Hello {}!".format(username))

# Development
## USE THE APP RUN COMMAND TO SERVE YOUR APP

# Production
## OPTIONAL: USE WAITRESS TO SERVE YOUR APP