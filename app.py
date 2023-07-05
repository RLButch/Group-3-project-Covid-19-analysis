#Import libraries and packages needed for app.py

from flask import Flask, jsonify, #render_template
from flask import Flask
import sqlite3
import json

#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
##from sqlalchemy import create_engine, func
#from sqlalchemy.sql.functions import session_user
#from sqlalchemy.sql.selectable import subquery


app=Flask(__name__)

#Set up the engine and base to run
engine=sql.create_engine('sqlite:///data/covid.db')
Base = automap_base()
Base.prepare(engine, reflect=True)

@app.route('/')
def index():
    conn = sqlite3.connect('C:\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\Project 3\covid.db')
    # Perform further operations with the connection
    # ...
    conn.close()  # Close the connection when done
    return 'Imported SQLite file into Flask'
@app.route('/')
def index():
    conn = sqlite3.connect('C:\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\Project 3\covid.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM covid')  # actual table name
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/')
def index():
    conn = sqlite3.connect('C:\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\Project 3\covid.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM covid')
    rows = cursor.fetchall()
    conn.close()

    # Convert to JSON
    data = jsonify(rows).json

    # Save JSON to a file
    with open('C:\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\Project 3.json', 'w') as file:
        json.dump(data, file)

    return 'JSON file created'

@app.route('/covid19')
def get_coviddata():
    conn = sqlite3.connect('C:\WAUS-VIRT-DATA-PT-03-2023-U-LOLC\Project 3\covid.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM covid19')
    users = cursor.fetchall()
    conn.close()
    return str(users)  # Return the fetched data as a string

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