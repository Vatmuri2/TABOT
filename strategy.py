# trading_strategy.py
import alpaca_trade_api as tradeapi
import yfinance as yf
from config import BUY_THRESHOLD, SELL_THRESHOLD, PAPER_TRADING
from utils import get_account_balance


def execute_trade(symbol, percent_change):
    """Execute a trade based on the percentage change in stock price."""
    account_balance = get_account_balance()  # Get your account balance

    # Buy if price dropped by more than BUY_THRESHOLD
    if percent_change <= -BUY_THRESHOLD:
        # Proportional investment based on percentage drop
        amount_to_invest = abs(percent_change) * account_balance / 100
        print(f"Stock {symbol} dropped by {percent_change}%. Buying ${amount_to_invest:.2f} worth of stock.")
        
        if PAPER_TRADING:
            print("Paper Trading: Not executing real trades.")
        else:
            # Submit buy order to Alpaca
            api.submit_order(
                symbol=symbol,
                qty=amount_to_invest,  # Trading a dollar value here, adapt to share qty
                side='buy',
                type='market',
                time_in_force='gtc'
            )
        
    # Sell if price increased by more than SELL_THRESHOLD
    elif percent_change >= SELL_THRESHOLD:
        # Proportional selling based on percentage rise
        amount_to_sell = percent_change * account_balance / 100
        print(f"Stock {symbol} increased by {percent_change}%. Selling ${amount_to_sell:.2f} worth of stock.")
        
        if PAPER_TRADING:
            print("Paper Trading: Not executing real trades.")
        else:
            # Submit sell order to Alpaca
            api.submit_order(
                symbol=symbol,
                qty=amount_to_sell,  # Trading a dollar value here, adapt to share qty
                side='sell',
                type='market',
                time_in_force='gtc'
            )
    else:
        print(f"Stock {symbol} did not meet the trading thresholds.")
    

def monitor_tickers():
    """Check price changes and execute trades for each ticker."""
    # Read tickers from a file
    with open('tickers.txt', 'r') as f:
        tickers = f.readlines()
    
    for ticker in tickers:
        ticker = ticker.strip()  # Remove extra whitespace
        stock = yf.Ticker(ticker)
        
        # Get the stock's historical data (e.g., last 5 days)
        data = stock.history(period='5d')
        
        # Get the percentage change between the first and last price
        price_change = ((data['Close'][-1] - data['Close'][0]) / data['Close'][0]) * 100
        
        # Execute the trade based on price change
        execute_trade(ticker, price_change)

