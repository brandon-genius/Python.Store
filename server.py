

from flask import Flask
import json
from mock_data import mock_catalog

app = Flask('server')


@app.route("/home")
def home():
    return "sup"


home()


@app.route("/")
def root():
    return "Welcome to the store"


###############################################################
###############################################################
########################  API CATELOG  ########################

@app.route("/api/about", methods=['post'])
def about():
    me = {
        "first_name": "Brandon",
        "last_name": "Britt",
        "age": 30,
        "address": {
            "num": 1200,
            "street": "Queen Emma",
            "city": "Honolulu"
        }
    }
    return json.dumps(me) #parse into json, then return

@app.route("/api/catalog")
def get_catalog():
    return json.dumps(mock_catalog)


# start the server
app.run(debug=True)
