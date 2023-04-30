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
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

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
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"

    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    max_date_query = session.query(func.max(Measurement.date))
    
    max_date = max_date_query.scalar()
    max_date = dt.datetime.strptime(max_date, '%Y-%m-%d').date()

    # Calculate the date one year from the last date in data set.
    filter_date = dt.datetime(max_date.year -1, max_date.month, max_date.day-1)

    # Perform a query to retrieve the data and precipitation scores
    sql = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= filter_date)

    # Save the query results as a Pandas DataFrame and set the index to the date column
    measurement_df = pd.read_sql(sql = sql.statement, con = engine)

    # Sort the dataframe by date
    measurement_df = measurement_df.groupby(['date']).max(['prcp'])

    measurement_df = measurement_df[measurement_df.prcp > 0.0].sort_values(['date']).reset_index()
    measurement_df = measurement_df.rename(columns={'prcp': 'percipitation'})
    return jsonify(measurement_df.set_index('date').to_dict())


if __name__ == '__main__':
    app.run(debug=True)