import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period="1wk", interval="1d"):
    """
    Fetch historical stock data for the given ticker symbol.
    
    :param ticker: Stock ticker symbol
    :param period: Period for historical data (e.g., "1wk", "1mo", "1y")
    :param interval: Data interval (e.g., "1d", "1h")
    :return: DataFrame with stock data
    """
    stock_data = yf.Ticker(ticker)
    historical_data = stock_data.history(period=period, interval=interval)
    return historical_data

def calculate_percentage_change(historical_data):
    """
    Calculate the percentage change in stock price from start to end of the data period.
    
    :param historical_data: DataFrame with historical stock data
    :return: Percentage change in price
    """
    price_start = historical_data.iloc[0]["Close"]
    price_end = historical_data.iloc[-1]["Close"]
    percentage_change = ((price_end - price_start) / price_start) * 100
    return percentage_change

def get_weekly_percentage_change(ticker):
    """
    Get the percentage change of a stock over the past week.
    
    :param ticker: Stock ticker symbol
    :return: Percentage change in stock price over the past week
    """
    historical_data = fetch_stock_data(ticker, period="1wk", interval="1d")
    percentage_change = calculate_percentage_change(historical_data)
    return percentage_change
