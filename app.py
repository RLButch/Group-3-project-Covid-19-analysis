#Import libraries and packages needed for app.py
from flask import Flask, jsonify
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()
class Data(Base):
    __tablename__ = 'data'
    Country = Column(String(512), primary_key=True)
    New_cases = Column(Integer)
    Cumulative_cases = Column(Integer)
    New_deaths = Column(Integer)
    Cumulative_deaths = Column(Integer)
    Latitude = Column(Float)
    Longitude = Column(Float)
engine = create_engine('sqlite:///covid.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/covid<br/>"
    )
@app.route("/api/covid")
def covid():
    results = session.query(Data).all()
    session.close()
    all_covid_data = []
    for result in results:
        data = {
            "Country": result.Country,
            "New_cases": result.New_cases,
            "Cumulative_cases": result.Cumulative_cases,
            "New_deaths": result.New_deaths,
            "Cumulative_deaths": result.Cumulative_deaths,
            "Latitude": result.Latitude,
            "Longitude": result.Longitude
        }
        all_covid_data.append(data)
    return jsonify(all_covid_data)
if __name__ == '__main__':
    app.run()

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

# if __name__ == '__main__':
#     app.run()

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