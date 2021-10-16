#dependencies

import json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template

#################################################
# Database Setup
#################################################
rds_connection_string = "postgres:VinceNoir@localhost:5432/amc"
engine = create_engine(f'postgres://{rds_connection_string}')

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
        f"/api/v1.0/amc/Date<br/>"
        f"/api/v1.0/amc/Close<br/>"
        f"/api/v1.0/amc/Volume<br/>"
        f"/api/v1.0/nasdaq/Date<br/>"
        f"/api/v1.0/nasdaq/Close<br/>"
        f"/api/v1.0/nasdaq/Volume"

    )

@app.route("/api/v1.0/amc/Date")
def amc_date():
    session = Session(engine)

    date_results = session.query(amc.Date).all()

    session.close()
    return jsonify(date_results)
    

@app.route("/api/v1.0/amc/Close")
def amc_close():
    session = Session(engine)

    close_results = session.query(amc.Close).all()

    session.close()
    return jsonify(close_results)

@app.route("/api/v1.0/amc/Volume")
def amc_volume():
    session = Session(engine)

    volume_results = session.query(amc.Volume).all()

    session.close()
    return jsonify(volume_results)

@app.route("/api/v1.0/nasdaq/Date")
def n_date():
    session = Session(engine)

    n_date_results = session.query(nasdaq.Date).all()

    session.close()
    return jsonify(n_date_results)

@app.route("/api/v1.0/nasdaq/Close")
def n_close():
    session = Session(engine)

    n_close_results = session.query(nasdaq.Close).all()

    session.close()
    return jsonify(n_close_results)

@app.route("/api/v1.0/nasdaq/Volume")
def n_volume():
    session = Session(engine)

    n_volume_results = session.query(nasdaq.Volume).all()

    session.close()
    return jsonify(n_volume_results)

if __name__ == '__main__':
    app.run(debug=True)