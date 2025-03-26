import time
from config import TICKERS_FILE, BUY_THRESHOLD, SELL_THRESHOLD, BUY_AMOUNT, SELL_AMOUNT, PAPER_TRADING
from data_fetcher import get_weekly_percentage_change
from strategy import TradingStrategy
from trader import AlpacaTrader
import logging

# Set up logging
logging.basicConfig(filename='trading_log.txt', level=logging.INFO)

def load_tickers(tickers_file):
    """
    Load the list of tickers from a file.
    
    :param tickers_file: Path to the file containing tickers
    :return: List of stock tickers
    """
    with open(tickers_file, 'r') as f:
        tickers = f.read().splitlines()
    return tickers

def execute_trades():
    """
    Main function to execute the trading strategy.
    """
    # Initialize the strategy and trader
    strategy = TradingStrategy(BUY_THRESHOLD, SELL_THRESHOLD, BUY_AMOUNT, SELL_AMOUNT)
    trader = AlpacaTrader()

    # Load tickers
    tickers = load_tickers(TICKERS_FILE)

    # Loop through each ticker and apply strategy
    for ticker in tickers:
        try:
            # Get the percentage change for the ticker
            percentage_change = get_weekly_percentage_change(ticker)
            logging.info(f"{ticker}: {percentage_change}% change")

            # Determine the trade action
            action, trade_amount = strategy.determine_trade(ticker)

            # Execute the trade if it's a buy or sell action
            if action != "hold":
                if PAPER_TRADING:
                    logging.info(f"Executing {action} for {trade_amount} of {ticker}")
                    trader.place_trade(action, ticker, trade_amount)
                else:
                    logging.info(f"Paper trading mode: {action} for {trade_amount} of {ticker}")

        except Exception as e:
            logging.error(f"Error with {ticker}: {e}")
        
        # Wait to avoid hitting rate limits and overloading API calls
        time.sleep(1)

if __name__ == "__main__":
    execute_trades()
