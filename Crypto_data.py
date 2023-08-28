import pandas as pd
import yfinance as yf
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
    crypto_data[symbol] = pd.DataFrame(prices).drop('date', axis=1).set_index('formatted_date')
    df = pd.DataFrame(prices).drop('date', axis=1).set_index('formatted_date')
    crypto_data[symbol] = df


# Print the first and last few rows of each cryptocurrency DataFrame
for symbol, df in crypto_data.items():
    print(f"{symbol}:\n{df.head()}\n")
    print(f"{symbol}:\n{df.tail()}\n")

# Save the DataFrame to a CSV file
for symbol, df in crypto_data.items():
    csv_filename = f"{symbol}_data.csv"
    df.to_csv(csv_filename)
    print(f"{symbol} data saved to {csv_filename}")




# Concatenate all DataFrames
combined_crypto_data = pd.concat(crypto_data.values(), keys=crypto_data.keys(), names=['Crypto', 'Date'])

# Save the combined DataFrame to a CSV file
combined_csv_filename = "combined_crypto_data.csv"
combined_crypto_data.to_csv(combined_csv_filename)
print(f"Combined cryptocurrency data saved to {combined_csv_filename}")