import os
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


engine = create_engine("sqlite:///db.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)