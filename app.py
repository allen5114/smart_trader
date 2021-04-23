import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import finnhub
import configparser

from dash.dependencies import Input, Output

import json

#data = pd.read_csv("avocado.csv")
#data = data.query("type == 'conventional' and region == 'Albany'")
#data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
#data.sort_values("Date", inplace=True)

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

# Recommendation trends
#print(finnhub_client.recommendation_trends('AAPL'))

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
                html.Iframe(id="recommandation",
                    src="https://widget.finnhub.io/widgets/recommendation?symbol=AAPL",
                    style={"height": "500px", "width": "80%"})
            ]),
            dcc.Tab(label='Company News', value='company-news-tab', children=[
                html.Div(id='company-news-div'),
            ]),
        ]),
        html.Div(id='tabs-content'),
    ]
)

# import company news script logic
import company_news

# Symbols Dropdown event 
@app.callback(
    Output('recommandation', 'src'),
    [Input('symbols-dropdown', 'value')])
def update_recommendation(value):
    return 'https://widget.finnhub.io/widgets/recommendation?symbol={}'.format(value)


if __name__ == "__main__":
    app.run_server(debug=True, port=8000)