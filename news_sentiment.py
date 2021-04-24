from __main__ import app
from __main__ import finnhub_client

import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Symbols Dropdown event 
@app.callback(
    Output('news-sentiment-div', 'children'),
    [Input('symbols-dropdown', 'value')])
def update_news_sentiment(value):
    response = finnhub_client.news_sentiment(value)
    #print(response)
    
    colors = ['rgb(255,255,255)', 'rgb(255,255,255)', 'rgb(255,255,255)']
    overall = "<b>Bullish</b>"
    if response["sentiment"]["bullishPercent"] < response["sentiment"]["bearishPercent"]:
        overall = "<b>Bearish</b>"
        #colors.append('rgb(233, 148, 148)')    
    
    sentimentFig = go.Figure(data=[go.Table(
        header=dict(
            values=['<b>Sentiment</b>', ''],
            fill_color='lightgray',
        ),
        cells=dict(
            values=[
                ['Bearish %','Bullish %', 'Overall'],
                [response["sentiment"]["bearishPercent"], response["sentiment"]["bullishPercent"], overall],
            ],
            line_color=[colors],
            fill_color=[colors],
        ))
    ])
    
    sentimentFig.update_layout(
        margin=dict(l=20, r=20, t=30, b=20),
        height=150,
        #paper_bgcolor="LightSteelBlue",
    )   
    
    buzzFig = go.Figure(data=[go.Table(
        header=dict(
            values=['<b>Buzz Statistic</b>', ''],
            fill_color='lightgray',
        ),
        cells=dict(
            values=[
                ['Articles In Last Week','Weekly Average', "Score"],
                [response["buzz"]["articlesInLastWeek"], response["buzz"]["weeklyAverage"], response["buzz"]["buzz"]],
            ]
        ))
    ])

    buzzFig.update_layout(
        margin=dict(l=20, r=20, t=30, b=20),
        height=150,
        #paper_bgcolor="LightSteelBlue",
    )    
    
    sectorFig = go.Figure(data=[go.Table(
        header=dict(
            values=['<b>Sector Statistic</b>', ''],
            fill_color='lightgray',
        ),
        cells=dict(
            values=[
                ['Sector Average Bullish %','Sector Averge News Score', "Company News Score"],
                [response["sectorAverageBullishPercent"], response["sectorAverageNewsScore"], response["companyNewsScore"]],
            ]
        ))
    ])
    
    sectorFig.update_layout(
        margin=dict(l=20, r=20, t=30, b=20),
        height=150,
        #paper_bgcolor="LightSteelBlue",
    )    
    
    return [dcc.Graph(figure=sentimentFig), dcc.Graph(figure=buzzFig),dcc.Graph(figure=sectorFig),
           ]
    #return value
    #return html.Div(children=value)