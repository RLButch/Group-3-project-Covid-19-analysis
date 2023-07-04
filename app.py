#Import libraries and packages needed for app.py

from flask import Flask, jsonify, render_template
#import sqlalchemy as sql
#import json
#import numpy as np
#import pandas as pd
##import datetime as dt 

#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
##from sqlalchemy import create_engine, func
#from sqlalchemy.sql.functions import session_user
#from sqlalchemy.sql.selectable import subquery


app=Flask(__name__)

#engine=sql.create_engine('sqlite:///data/covid.db')



#app = Flask(__name__)
#@app.route("/jsonified")
#def jsonified():
          #return jsonify(covid)
#if __covid__ == “__main__”:
          #app.run(debug=True)

# Flask Setup
#app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# 1. Define what to do when a user hits the index route


@app.route("/")
def index():
    print("Server received request for 'index' page...")
    return render_template('index.html')

# 2. charts route


#@app.route("/charts")
#def charts():
    #print("Server received request for 'charts' page...")
    #return render_template('charts.html')

# 3. maps route


#@app.route("/maps")
#def maps():
    #print("Server received request for 'maps' page...")
    #return render_template('maps.html')

# 4. other charts route


#@app.route("/bri_charts")
#def bri_charts():
    #print("Server received request for 'other charts' page...")
    #return render_template('bri_charts.html')


if __name__ == '__main__':
    app.debug = True
    app.run()