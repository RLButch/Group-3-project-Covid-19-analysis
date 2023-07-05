#Import libraries and packages needed for app.py

from flask import Flask, jsonify, render_template
import sqlite3
import json
import numpy as np
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#from sqlalchemy.sql.functions import session_user
#from sqlalchemy.sql.selectable import subquery


engine = create_engine('sqlite:///covid.db')

# reflect the tables
#Base.prepare(autoload_with=engine)
# Create a Data Class for the table. 
class Data(Base):
    __tablename__ = 'data'
    Country = Column(String(512),primary_key=True)
    New_cases = Column(Integer)
    Cumulative_cases = Column(Integer)
    New_deaths = Column(Integer)
    Cumulative_deaths = Column(Integer)
    Latitude = Column(Float)
    Longitude = Column(Float)

# Save reference to the table
#covid = Base.classes.data

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/covid<br/>"
        
    )

@app.route("/api/covid")
def covid():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all covid data"""
    # Query all passengers
    results = session.query(covid.name).all()

    session.close()

    # Convert list of tuples into normal list
    allcovid = list(np.ravel(results))

    return jsonify(allcovid)

# @app.route('/')
# def index():
#     conn = sqlite3.connect('C:\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\Project 3\covid.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM covid')  # actual table name
#     rows = cursor.fetchall()
#     conn.close()
#     return jsonify(rows)

# @app.route('/')
# def index():
#     conn = sqlite3.connect('C:\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\Project 3\covid.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM covid')
#     rows = cursor.fetchall()
#     conn.close()

#     # Convert to JSON
#     data = jsonify(rows).json

#     # Save JSON to a file
#     with open('C:\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\Project 3.json', 'w') as file:
#         json.dump(data, file)

#     return 'JSON file created'

# @app.route('/covid19')
# def get_coviddata():
#     conn = sqlite3.connect('C:\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\Project 3\covid.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM covid19')
#     users = cursor.fetchall()
#     conn.close()
#     return str(users)  # Return the fetched data as a string

if __name__ == '__main__':
    app.run()

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


# @app.route("/")
# def index():
#     print("Server received request for 'index' page...")
#     return render_template('index.html')

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


# if __name__ == '__main__':
#     app.debug = True
#     app.run()