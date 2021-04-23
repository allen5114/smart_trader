import dash
import dash_core_components as dcc
import dash_html_components as html
import finnhub
import configparser
import json

# Read configurations
config = configparser.ConfigParser()
config.read("./config/config-real.ini")

# Read symbols
with open('./config/symbols.json') as f:
  symbols = json.load(f)

# Setup Client
finnhub_client = finnhub.Client(api_key=config["finnhub.io"]["api_key"])
#finnhub_client = finnhub.Client(api_key=config["finnhub.io"]["sandbox_api_key"])

# News Sentiment
#print(finnhub_client.news_sentiment('AAPL'))

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Smart Trader",),
        dcc.Dropdown(
            id='symbols-dropdown',
            options=symbols,
            value=symbols[0]["value"],
            persistence=True,
            persistence_type='session'
        ),
        html.Br(),
        dcc.Tabs(id='tabs', value='recommendation-tab', children=[
            dcc.Tab(label='Recommendation Trends', value='recommendation-tab', children=[
                html.Div(id='recommendation-trends-div'),
            ]),
            dcc.Tab(label='Company News', value='company-news-tab', children=[
                html.Div(id='company-news-div'),
            ]),
            dcc.Tab(label='News Sentiment', value='news-sentiment-tab', children=[
                html.Span(children='to do'),
            ]),
        ]),
        html.Div(id='tabs-content'),
    ]
)

# import company news script logic
import company_news

# import recommendation trends logic
import recommendation_trends

if __name__ == "__main__":
    app.run_server(debug=True, port=8000)