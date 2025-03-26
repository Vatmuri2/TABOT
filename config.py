import os

# Alpaca API credentials (store in environment variables for security)
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY", "PKHKF7S44AUSRYOVE5PP")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY", "aMA57wngvLLzNcG6PmBTZbr88ZNPyVctgAhi8PcM")
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"  # Use live URL if trading real money

# List of stock tickers (load from a file or define here)
TICKERS_FILE = "tickers.txt"  # A file containing 4000 stock tickers, one per line

TICKERS_FILE = 'tickers.txt'
BUY_THRESHOLD = 5  # 5% drop to trigger a buy
SELL_THRESHOLD = 10  # 10% rise to trigger a sell
PAPER_TRADING = True  # Set True for paper trading

# Data fetching settings
YFINANCE_INTERVAL = "1d"  # Daily interval to compute weekly changes
LOOKBACK_DAYS = 7  # Number of days to look back

# Alpaca trading settings


# Logging settings
LOG_FILE = "trading_log.txt"
