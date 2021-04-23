from __main__ import app
from __main__ import config
from __main__ import finnhub_client

import dash
import dash_html_components as html
from dash.dependencies import Input, Output

from datetime import date
import datetime
from datetime import datetime as dt

import json

# Return a div containing company news
def get_company_news_row(news):
    timestamp = dt.fromtimestamp(news["datetime"])
    timestampStr = timestamp.strftime("%m/%d/%Y %H:%M")
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.A([html.H2(children=news["headline"],),], href=news["url"]),
                    html.P(children=news["source"]+ " " + timestampStr,),
                    html.Span(children=news["summary"],),
                ]
            ,style={'display': 'inline-block', 'width': '70%', 'verticalAlign': 'top'}),
            html.Div(
                children=[
                    html.A([
                        html.Img(src=news["image"]
                        , style={'height': '150px'}),
                    ], href=news["url"]),
                ]
            ,style={'display': 'inline-block', 'width': '30%', 'verticalAlign': 'top'}),
        ], style={'margin': '10px', 'padding': '10px'},        
    )
    
# Populate Company New tab with news within the last week for the selected symbol 
@app.callback(
    Output('company-news-div', 'children'),
    [Input('symbols-dropdown', 'value')])
def update_company_news(value):
    # get news for the last week
    today = date.today()
    todayStr = today.strftime("%Y-%m-%d")
    delta = datetime.timedelta(days = 7)
    fromDate = today - delta
    fromDateStr = fromDate.strftime("%Y-%m-%d")
    
    response = finnhub_client.company_news(value, _from=fromDateStr, to=todayStr)

    return html.Div(children=[get_company_news_row(news) for news in response])
