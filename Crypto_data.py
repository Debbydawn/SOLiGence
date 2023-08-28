import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials


yahoo_financials = YahooFinancials('BTC-USD')
data=yahoo_financials.get_historical_price_data("2019-07-10", "2021-05-30", "monthly")
btc_df = pd.DataFrame(data['BTC-USD']['prices'])
btc_df = btc_df.drop('date', axis=1).set_index('formatted_date')
btc_df.head()
