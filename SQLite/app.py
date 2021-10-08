import os
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from sqlalchemy.ext.automap import automap_base
from datetime import date
import sqlalchemy as sa

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from sqlalchemy.sql.expression import extract
from sqlalchemy.sql.schema import Index


engine = create_engine("sqlite:///database/stock_exchange_db.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

print(Base.classes.keys())

stock = Base.classes.stock_exchange

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#--------------------------------------------
# create route that renders HTML templates
@app.route("/")
def home():
    return render_template("index.html")

#------------------------------------------
#API Routes


###Filter by year###
@app.route("/api/years/<year>/<stockindex>")
def years(year, stockindex):

    session = Session(engine)

    first = date(int(year), 1, 1)
    last = date(int(year), 12, 31)
    print(first)
    print(last)

    results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between (first,last), stock.Stock_index == stockindex).all()
    
    results = [list(r) for r in results]

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

    year_results = {
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
    }

    session.close()
    # print(set(year_results))
    return jsonify(year_results)

# pie chart to dispaly volume for all stock indexes
@app.route("/api/pie/<year>")
def pie(year):
    session = Session(engine)
    print("PieChart App.py")
    first = date(int(year), 1, 1)
    last = date(int(year), 12, 31)
    print(first)
    print(last)

    results = session.query(stock.Exchange, func.sum(stock.Volume)).filter(stock.Date.between (first,last)).group_by(stock.Stock_index).all()
    
    Exchange = [result[0] for result in results]
    Volume = [result[1] for result in results]

    pie_results ={
        "Index": Exchange,
        "Volume": Volume
    }

    session.close()
    
    return jsonify(pie_results)


@app.route("/api/pie2/<stockIndex>")
def pie2(stockIndex):
    print("PIE2")
    session = Session(engine)

    results = session.query(func.strftime("%Y", stock.Date), func.sum(stock.Volume * 0.00001)).filter(stock.Stock_index == stockIndex).group_by(func.strftime("%Y", stock.Date)).order_by(desc(func.strftime("%Y", stock.Date))).all()

    Year = [result[0] for result in results]
    Volume = [result[1] for result in results]
    print(Year)
    print(Volume)
    pie_results ={
        "Year": Year,
        "Volume": Volume,
    }

    session.close()
    
    return jsonify(pie_results)

###Filter by stock exchange###
@app.route("/api/exchanges/<year>/<stockIndex>")
def exchanges(year, stockIndex):

    print("Exchange Endpoint")
    session = Session(engine)
    print("Exchange App.py")
    first = date(int(year), 1, 1)
    last = date(int(year), 12, 31)

    results = session.query(stock.Date, stock.exchange_rate).filter(stock.Date.between (first,last), stock.exchange_rate > 0, stock.Stock_index == stockIndex).all()

    
    Date = [result[0] for result in results]
    Exchange_Rate = [result[1] for result in results]
    
    exchange_results ={
        "Date": Date,
        "Rate": Exchange_Rate,
    }

    session.close()
    
    return jsonify(exchange_results)

    

if __name__ == "__main__":
    app.run()

    