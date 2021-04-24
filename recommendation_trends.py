from __main__ import app
from __main__ import finnhub_client

import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from datetime import date
import datetime
from datetime import datetime as dt

# Symbols Dropdown event 
@app.callback(
    Output('recommendation-trends-div', 'children'),
    [Input('symbols-dropdown', 'value')])
def update_recommendation_trends(value):
    response = finnhub_client.recommendation_trends(value)

    periods = []
    buy = []
    hold = []
    sell = []
    strongBuy = []
    strongSell = []
    
    today = date.today()
    delta = datetime.timedelta(days = 365)
    startDate = today - delta
    
    graphTitle = value + " Recommendation Trends"
    
    for data in response:
        dateStr = data["period"]
        dateObj = dt.strptime(dateStr, "%Y-%m-%d")
        if dateObj.date() >= startDate:
            periods.append(data["period"])
            buy.append(data["buy"])
            hold.append(data["hold"])
            sell.append(data["sell"])
            strongBuy.append(data["strongBuy"])
            strongSell.append(data["strongSell"])
    
    strongBuyTrace = go.Bar(
        x=periods,
        y=strongBuy,
        text = strongBuy,
        textposition='auto',
        name='StrongBuy',
        marker=go.bar.Marker(color='rgb(54, 152, 25)')
    )  
    buyTrace = go.Bar(
        x=periods,
        y=buy,
        text = buy,
        textposition='auto',
        name='Buy',
        marker=go.bar.Marker(color='rgb(0, 255, 0)')
    )
    holdTrace = go.Bar (
        x=periods,
        y=hold,
        text = hold,
        textposition='auto',
        name='Hold',
        marker=go.bar.Marker(color='rgb(255, 153, 0)')
    )
    sellTrace = go.Bar (
        x=periods,
        y=sell,
        text = sell,
        textposition='auto',
        name='Sell',
        marker=go.bar.Marker(color='rgb(233, 148, 148)')
    )
    strongSellTrace = go.Bar (
        x=periods,
        y=strongSell,        
        text = strongSell,
        textposition='auto',
        name='StrongSell',
        marker=go.bar.Marker(color='rgb(141, 14, 14)')
    )
    return [dcc.Graph(figure=go.Figure(data=[strongSellTrace, sellTrace, holdTrace, buyTrace, strongBuyTrace], layout=go.Layout(title=graphTitle, plot_bgcolor='lightgray', barmode='stack')))]