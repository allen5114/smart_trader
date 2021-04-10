## Dependency Setup

https://realpython.com/python-dash/

## Create Python 3 virtual environment
````
# cd to repo
python -m venv venv

# on Windows
venv\Scripts\activate.bat

# on Linux
source venv/bin/activate

# upgrade pip
python -m pip install --upgrade pip
````

## Install required libraries
````
# Dash framework
python -m pip install dash==1.13.3 pandas==1.0.5

# finnhub API
pip install finnhub-python
````

## Update keys in config file

Examples
````
# API usage
https://github.com/Finnhub-Stock-API/finnhub-python

# Existing widgets
https://widget.finnhub.io/widgets/recommendation?symbol=AAPL
https://widget.finnhub.io/widgets/eps-estimate?symbol=AAPL
https://widget.finnhub.io/widgets/historical-eps?symbol=AAPL
https://widget.finnhub.io/widgets/stocks/chart?symbol=AAPL
https://widget.finnhub.io/widgets/etf-holdings?symbol=ARKK
https://widget.finnhub.io/widgets/stocks/chart?symbol=OANDA:EUR_USD
https://widget.finnhub.io/widgets/stocks/chart?symbol=BINANCE:BTCUSDT
````