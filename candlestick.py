from __main__ import app
from __main__ import finnhub_client

import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# for unix timestamp
import time
from datetime import datetime as dt
import datetime

def unix_timstampe_toString(timestamp):
    return dt.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

# Symbols Dropdown event 
@app.callback(
    Output('candlestick-div', 'children'),
    [Input('symbols-dropdown', 'value'),
     Input('resolutions-dropdown', 'value'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')])
def update_candlestick(symbol, resolution, startDate, endDate):
    # convert dates to unix timestamps
    startTimestamp = time.mktime(datetime.datetime.strptime(startDate, "%Y-%m-%d").timetuple())
    endTimestamp = time.mktime(datetime.datetime.strptime(endDate, "%Y-%m-%d").timetuple())

    # get stock candles data
    response = finnhub_client.stock_candles(symbol, resolution, int(startTimestamp), int(endTimestamp))
    
    # convert unix timestamp to readable string
    converted_t = [unix_timstampe_toString(t) for t in response["t"]]
    
    fig = go.Figure(data=[go.Candlestick(x=converted_t, open=response["o"], high=response["h"], low=response["l"], close=response["c"])])
    
    # this line disables the range slider
    fig.update_layout(xaxis_rangeslider_visible=False)

    # remove x date with empty data
    graphTitle = symbol + " Candlestick"
    fig.layout = dict(xaxis = dict(type="category", categoryorder='category ascending'), title=graphTitle)
    
    return [dcc.Graph(figure=fig)]