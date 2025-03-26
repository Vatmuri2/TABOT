import alpaca_trade_api as tradeapi
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, PAPER_TRADING
import logging

class AlpacaTrader:
    def __init__(self):
        # Set up Alpaca API connection
        self.api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_BASE_URL)

    def check_account(self):
        """
        Check the account balance and available buying power.
        """
        try:
            account = self.api.get_account()
            return account.cash, account.cash_with_held_for_orders
        except Exception as e:
            logging.error(f"Error checking account: {e}")
            return 0, 0

    def place_trade(self, action, ticker, amount):
        """
        Place a buy or sell trade via Alpaca.

        :param action: "buy" or "sell"
        :param ticker: Stock ticker symbol
        :param amount: Amount in dollars to buy or sell
        """
        try:
            # Check account balance
            cash, _ = self.check_account()
            
            if action == "buy":
                if cash >= amount:
                    logging.info(f"Placing buy order for {amount} dollars of {ticker}")
                    self.api.submit_order(
                        symbol=ticker,
                        qty=amount // self.get_stock_price(ticker),
                        side='buy',
                        type='market',
                        time_in_force='gtc'
                    )
                else:
                    logging.warning(f"Insufficient funds for buy order of {ticker}. Available cash: {cash}")
            
            elif action == "sell":
                logging.info(f"Placing sell order for {amount} dollars of {ticker}")
                self.api.submit_order(
                    symbol=ticker,
                    qty=amount // self.get_stock_price(ticker),
                    side='sell',
                    type='market',
                    time_in_force='gtc'
                )
        except tradeapi.rest.APIError as e:
            logging.error(f"API error occurred when placing {action} order for {ticker}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error occurred when placing {action} order for {ticker}: {e}")

    def get_stock_price(self, ticker):
        """
        Get the current price of the stock.

        :param ticker: Stock ticker symbol
        :return: Current stock price
        """
        try:
            stock = self.api.get_barset(ticker, "minute", limit=1)
            return stock[ticker][0].c
        except Exception as e:
            logging.error(f"Error fetching price for {ticker}: {e}")
            return 0
