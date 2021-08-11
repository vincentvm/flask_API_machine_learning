from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/users/<string:username>')
def hello_world(username='MyName'):
    return("Hello {}!".format(username))

# Development
app.run(host='0.0.0.0', port=8000, debug=True)

# Production
#serve(app, host='0.0.0.0', port=8000)