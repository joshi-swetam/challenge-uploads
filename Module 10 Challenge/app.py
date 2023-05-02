# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite?check_same_thread=False")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the  Hawaii Wather Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"

    )

@app.route("/api/v1.0/precipitation")
def percipitation():
    # Perform a query to retrieve the data and precipitation scores
    sql = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= get_filter_date())

    # Save the query results as a Pandas DataFrame and set the index to the date column
    measurement_df = pd.read_sql(sql = sql.statement, con = engine)

    # Sort the dataframe by date
    measurement_df = measurement_df.groupby(['date']).max(['prcp'])

    measurement_df = measurement_df[measurement_df.prcp > 0.0].sort_values(['date']).reset_index()
    
    output = []
    for index, row in measurement_df.iterrows():
        measurement = {}
        measurement["date"] = row["date"]
        measurement["prcp"] = row["prcp"]
        
        output.append(measurement)
    
    return jsonify(output)

@app.route("/api/v1.0/stations")
def stations():
    stations_list = session.query(Station.station, Station.name, Station.longitude, Station.latitude, Station.id, Station.elevation).all()
    output = []
    for s in stations_list:
        station = {}
        station["station"] = s["station"]
        station["name"] = s["name"]
        station["longitude"] = s["longitude"]
        station["latitude"] = s["latitude"]
        station["elevation"] = s["elevation"]
        
        output.append(station)
        
    return jsonify(output)

@app.route("/api/v1.0/tobs")
def tobs():
    most_active_stations_query = session.query(Measurement.station, func.count(Measurement.station).label('count')).group_by(Measurement.station)
    most_active_stations_df = pd.read_sql(sql = most_active_stations_query.statement, con = engine).dropna().sort_values('count', ascending=False)
    most_active_station_id =  most_active_stations_df.iloc[0]['station']
    
    sql = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= get_filter_date(), Measurement.station == most_active_station_id)
    measurement_df = pd.read_sql(sql = sql.statement, con = engine)
    
    output = []
    for index, row in measurement_df.iterrows():
        measurement = {}
        measurement["date"] = row["date"]
        measurement["tobs"] = row["tobs"]
        
        output.append(measurement)
    
    return jsonify(output)

@app.route("/api/v1.0/<start>", defaults={'end': None})
@app.route("/api/v1.0/<start>/<end>")
def temp_by_date(start, end):
    print(start)
    if end is None:
        query = session.query(Measurement.date, func.min(Measurement.tobs)
                              , func.avg(Measurement.tobs)
                              , func.max(Measurement.tobs)) \
                        .filter(Measurement.date >= start) \
                        .group_by(Measurement.date)
    else:
        query = session.query(Measurement.date, func.min(Measurement.tobs)
                              , func.avg(Measurement.tobs)
                              , func.max(Measurement.tobs)) \
                        .filter(Measurement.date >= start, Measurement.date <= end) \
                        .group_by(Measurement.date)
    output = []
    for row in query.all():
        
        stats = {}
        stats["date"] = row[0]
        stats["min"] = round(row[1], 2)
        stats["avg"] = round(row[2], 2)
        stats["max"] = round(row[3], 2)
        
        output.append(stats)
    
    return jsonify(output)

def get_filter_date():
    max_date_query = session.query(func.max(Measurement.date))
    
    max_date = max_date_query.scalar()
    max_date = dt.datetime.strptime(max_date, '%Y-%m-%d').date()

    # Calculate the date one year from the last date in data set.
    filter_date = dt.datetime(max_date.year -1, max_date.month, max_date.day-1)
    return filter_date

def toDate(dateString): 
    return dt.datetime.strptime(dateString, "%Y-%m-%d").date()

if __name__ == '__main__':
    app.run(debug=True)