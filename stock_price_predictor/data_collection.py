import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, start_data, end_data):

    try:
        stock_data = yf.download(ticker, start=start_data, end=end_data)
        data = pd.DataFrame(stock_data)
        print(data)
        if stock_data.empty:
            raise ValueError(f"No data found for {ticker}")

        return stock_data['Close']

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

fetch_stock_data('AAPL', '2022-01-01', '2023-12-31')