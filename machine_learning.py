import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from yahoofinancials import YahooFinancials
import datetime


# List of cryptocurrency symbols
crypto_symbols = ['BTC-GBP', 'ETH-GBP', 'LTC-GBP']

# Dictionary to store cryptocurrency data
crypto_data = {}

# Loop through each cryptocurrency symbol
for symbol in crypto_symbols:
    yahoo_financials = YahooFinancials(symbol)
    
    # Calculate the current date in YYYY-MM-DD format
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # Get historical price data up to the current date
    data = yahoo_financials.get_historical_price_data("2019-07-10", end_date, "daily")
    prices = data[symbol]['prices']
    df = pd.DataFrame(prices).drop('date', axis=1).set_index('formatted_date')
    
    # Explicitly set the frequency to 'D' (daily)
    df.index = pd.DatetimeIndex(df.index, freq='D')
    
    crypto_data[symbol] = df

# Fit ARIMA models and make forecasts for each symbol
order = (5, 1, 0)  # (p, d, q)
forecast_steps = 30



for symbol in crypto_symbols:
    crypto_series = crypto_data[symbol]['close']
    arima_model = ARIMA(crypto_series, order=order)
    arima_results = arima_model.fit()
    forecast = arima_results.forecast(steps=forecast_steps)
    
    print(forecast)
    
    
    # ... (Previous code)

for symbol in crypto_symbols:
    crypto_series = crypto_data[symbol]['close']
    arima_model = ARIMA(crypto_series, order=order)
    arima_results = arima_model.fit()
    forecast = arima_results.forecast(steps=forecast_steps)
    
    # Plot the original data and the forecast for each symbol
    plt.figure(figsize=(12, 6))
    
    # Plot the original data
    plt.plot(crypto_series.index, crypto_series, label='Original Data', color='blue')
    
    # Plot the forecast
    forecast_index = pd.date_range(start=crypto_series.index[-1], periods=forecast_steps + 1, freq='D', tz='UTC')[1:]
    plt.plot(forecast_index, forecast, label='Forecast', color='red')
    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'ARIMA Cryptocurrency Price Forecast for {symbol}')
    plt.legend()
    plt.grid(True)
    plt.show()

    

# Create a figure and axis for the plot
plt.figure(figsize=(12, 6))

for symbol in crypto_symbols:
    crypto_series = crypto_data[symbol]['close']
    arima_model = ARIMA(crypto_series, order=order)
    arima_results = arima_model.fit()
    forecast = arima_results.forecast(steps=forecast_steps)
    
    # Plot the forecast for each symbol
    forecast_index = pd.date_range(start=crypto_series.index[-1], periods=forecast_steps + 1, freq='D', tz='UTC')[1:]
    plt.plot(forecast_index, forecast, label=f'Forecast for {symbol}')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('ARIMA Cryptocurrency Price Forecasts')
plt.legend()
plt.grid(True)
plt.show()

