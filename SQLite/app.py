import os
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from datetime import date

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

    # new_york = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Year == year).filter(stock.Exchange = "New York Stock Exchange").all()
    first = date(int(year), 1, 1)
    last = date(int(year), 12, 31)
    print(first)
    print(last)

    # results = session.execute(f"Select * from stock_exchange WHERE Date Between {first} AND {last}").fetchall()
    # print("Year Results")
    # print(results)
    results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between (first,last), stock.Stock_index == stockindex).all()
    
    # if year == "2000":
    #      results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between (date(year, 1, 1), date(year, 12, 31))).all()
    # elif year == "2002":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2001-01-01', '2001-12-31')).all()
    # elif year == "2003":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2003-01-01', '2003-12-31')).all()
    # elif year == "2004":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2004-01-01', '2004-12-31')).all()
    # elif year == "2005":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2005-01-01', '2005-12-31')).all()
    # elif year == "2006":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2006-01-01', '2006-12-31')).all()
    # elif year == "2007":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2007-01-01', '2007-12-31')).all()
    # elif year == "2008":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2008-01-01', '2008-12-31')).all()
    # elif year == "2009":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2009-01-01', '2009-12-31')).all()
    # elif year == "2010":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2010-01-01', '2010-12-31')).all()
    # elif year == "2011":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2011-01-01', '2011-12-31')).all()
    # elif year == "2012":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2012-01-01', '2012-12-31')).all()
    # elif year == "2013":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2013-01-01', '2013-12-31')).all()
    # elif year == "2014":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2014-01-01', '2014-12-31')).all()
    # elif year == "2015":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2015-01-01', '2015-12-31')).all()
    # elif year == "2016":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2016-01-01', '2016-12-31')).all()
    # elif year == "2017":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2017-01-01', '2017-12-31')).all()
    # elif year == "2018":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2018-01-01', '2018-12-31')).all()
    # elif year == "2019":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2019-01-01', '2019-12-31')).all()
    # elif year == "2020":
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date.between ('2020-01-01', '2020-12-31')).all()
    # else:
    #     results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Date >='2021-01-01').all()
        

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
        #  "Open_USD": Open_USD,
        #   "High_USD": High_USD,
        #   "Low_USD": Low_USD,
        #   "Close_USD": Close_USD
    }

    session.close()
    # print(year_results)
    return jsonify(year_results)

###Filter by stock exchange###
@app.route("/api/exchanges/<exchange>")
def exchanges(exchange):

    print(exchange)


    if exchange == "New York":
        name = "New York Stock Exchange"
    elif exchange == "NASDAQ":
        name = "NASDAQ"
    elif exchange == "Hong Kong":
        name = "Hong Kong Stock Exchange"
    elif exchange == "Shanghai":
        name = "Shanghai Stock Exchange"
    elif exchange == "Toronto":
        name = "Toronto Stock Exchange"
    elif exchange == "Shenzhen":
        name = "Shenzhen Stock Exchange"
    elif exchange == "India":
        name = "National Stock Exchange of India"
    elif exchange == "Frankfurt":
        name = "Frankfurt Stock Exchange"
    elif exchange == "Korea":
        name = "Korea Exchange"
    elif exchange == "Swiss":
        name = "SIX Swiss Exchange"
    elif exchange == "Johannesburg":
        name = "Johannesburg Stock Exchange"
    elif exchange == "Tokyo":
        name = "Tokyo Stock Exchange"
    elif exchange == "Euronext":
        name = "Euronext"

    session = Session(engine)

    results = session.query(stock.Stock_index,stock.Date,stock.Open,stock.High,stock.Low,stock.Close,stock.Volume,stock.Region,stock.Exchange,stock.Currency,stock.USD,stock.exchange_rate,stock.Open_USD,stock.High_USD,stock.Low_USD,stock.Close_USD).filter(stock.Exchange == name).all()
    
    results = [list(r) for r in results]

    exchange_results = {
        "results": results,
    }

    session.close()

    return jsonify(exchange_results) 
    

if __name__ == "__main__":
    app.run()

    