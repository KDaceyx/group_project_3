#dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
rds_connection_string = "postgres:VinceNoir@localhost:5432/amc"
engine = create_engine(f'postgresql://{rds_connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
amc = Base.classes.amc_1
nasdaq = Base.classes.nasdaq_1

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/amc<br/>"
        f"/api/v1.0/nasdaq"
    )

@app.route("/api/v1.0/amc")
def amc():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return all stock data for amc"""
    #Query all stock data
    amc_results = session.query(amc).all()

    session.close()

@app.route("/api/v1.0/amc/Date")
def date():
    session = Session(engine)

    date_results = session.query(amc.Date).all()

    session.close()

@app.route("/api/v1.0/amc/Close")
def close():
    session = Session(engine)

    close_results = session.query(amc.Close).all()

    session.close()

@app.route("/api/v1.0/amc/Volume")
def volume():
    session = Session(engine)

    volume_results = session.query(amc.Volume).all()

    session.close()

@app.route("/api/v1.0/nasdaq")
def amc():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return all stock data for nasdaq"""
    #Query all stock data
    nasdaq_results = session.query(nasdaq).all()

    session.close()

@app.route("/api/v1.0/nasdaq/Date")
def date():
    session = Session(engine)

    date_results = session.query(nasdaq.Date).all()

    session.close()

@app.route("/api/v1.0/nasdaq/Close")
def close():
    session = Session(engine)

    close_results = session.query(nasdaq.Close).all()

    session.close()

@app.route("/api/v1.0/nasdaq/Volume")
def volume():
    session = Session(engine)

    volume_results = session.query(nasdaq.Volume).all()

    session.close()

