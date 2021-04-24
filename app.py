import dash
import dash_core_components as dcc
import dash_html_components as html
import finnhub
import configparser
import json

from datetime import date
import datetime

# Read configurations
config = configparser.ConfigParser()
config.read("./config/config-real.ini")

# Read symbols
with open('./config/symbols.json') as f:
  symbols = json.load(f)

# Read resolutions
with open('./config/resolutions.json') as f:
  resolutions = json.load(f)

# Setup Client
finnhub_client = finnhub.Client(api_key=config["finnhub.io"]["api_key"])
#finnhub_client = finnhub.Client(api_key=config["finnhub.io"]["sandbox_api_key"])

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    #'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'lightgray',
    #'color': 'white',
    'padding': '6px'
}

app = dash.Dash(__name__)
app.title = 'Stock Analyzer'
#app = dash.Dash(title='Test')
app.layout = html.Div(
    children=[
        html.H1(children="Stock Analyzer / Auto Trader",),
        dcc.Dropdown(
            id='symbols-dropdown',
            options=symbols,
            value=symbols[0]["value"],
            persistence=True,
            persistence_type='session'
        ),
        html.Br(),
        dcc.Tabs(id='tabs', value='company-news-tab', children=[
            dcc.Tab(label='Company News', value='company-news-tab', style=tab_style, selected_style=tab_selected_style, children=[
                html.Div(id='company-news-div'),
            ]),
            dcc.Tab(label='Recommendation Trends', value='recommendation-tab', style=tab_style, selected_style=tab_selected_style, children=[
                html.Div(id='recommendation-trends-div'),
            ]),
            dcc.Tab(label='News Sentiment', value='news-sentiment-tab', style=tab_style, selected_style=tab_selected_style, children=[
                html.Div(id='news-sentiment-div'),
            ]),
            dcc.Tab(label='Candlestick', value='candlestick-tab', style=tab_style, selected_style=tab_selected_style, children=[
                html.Div(
                    children=[
                        html.Br(),
                        html.Span("Resolution"),
                        dcc.Dropdown(
                            id='resolutions-dropdown',
                            options=resolutions,
                            value=resolutions[1]["value"],
                            persistence=True,
                            persistence_type='session'
                        ),
                    ]
                ,style={'display': 'inline-block', 'width': '30%', 'verticalAlign': 'top'}),
                html.Div(children=[]
                ,style={'display': 'inline-block', 'width': '20%', 'verticalAlign': 'top'}),
                html.Div(
                    children=[
                        html.Br(),
                        html.Span("Date range"),
                        html.Br(),
                        dcc.DatePickerRange(
                            id='date-picker-range',
                            min_date_allowed=date.today() - datetime.timedelta(days = 365),
                            max_date_allowed=date.today() + datetime.timedelta(days = 1),
                            initial_visible_month=date.today(),
                            start_date=date.today() - datetime.timedelta(days = 5),
                            end_date=date.today() + datetime.timedelta(days = 1),
                        ),
                    ]
                ,style={'display': 'inline-block', 'width': '50%', 'verticalAlign': 'top'}),
                html.Div(id='candlestick-div'),
            ]),
        ]),
        html.Div(id='tabs-content'),
    ]
)

# import company news script logic
import company_news

# import recommendation trends logic
import recommendation_trends

# import news sentiment logic
import news_sentiment

# import candlestick logic
import candlestick

if __name__ == "__main__":
    app.run_server(debug=True, port=8000)