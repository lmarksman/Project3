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
from sqlalchemy.sql.schema import Index


engine = create_engine("sqlite:///database/stock_exchange_db.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

stock = Base.classes.stock_exchange

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/exchange")
def pals():

    session = Session(engine)

    results = session.query(stock.Index, stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Voume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).all()

    Index = [result[0] for result in results]
    Date = [result[1] for result in results]
    Open = [result[2] for result in results]
    High = [result[3] for result in results]
    Low = [result[4] for result in results]
    Close = [result[5] for result in results]
    Volume = [result[6] for result in results]
    Region = [result[7] for result in results]
    Exchange = [result[8] for result in results]
    Currency = [result[9] for result in results]
    USD = [result[10] for result in results]
    exchange_rate = [result[11] for result in results]
    Open_USD = [result[12] for result in results]
    High_USD = [result[13] for result in results]
    Low_USD = [result[14] for result in results]
    Close_USD = [result[15] for result in results]

    results = {
        "Index": Index,
        "Date": Date,
        "Open": Open,
        "High": High,
        "Low": Low,
        "Close": Close,
        "Volume": Volume,
        "Region": Region,
        "Exchange": Exchange,
        "Currency": Currency,
        "USD": USD,
        "exchange_rate": exchange_rate,
        "Open_USD": Open_USD,
        "High_USD": High_USD,
        "Low_USD": Low_USD,
        "Close_USD": Close_USD
    }

    session.close()

    return jsonify(results)
    

if __name__ == "__main__":
    app.run()