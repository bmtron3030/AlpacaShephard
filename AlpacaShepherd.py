import alpaca_trade_api as alpaca
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


class AlpacaShepherd():

    # Function that checks if the connection to Alpaca
    # returns True if connection is successful, False otherwise
    def checkConnectionToAlpacaTradeAPI(self, API_KEY, SECRET_KEY, BASE_URL):
        canConnect = False
        try:
            API = alpaca.REST(API_KEY, SECRET_KEY, BASE_URL)
        except:
           print('Failed to connect Alpaca. Please check account credentials and internet connection.')
        else:
            canConnect = True
        return canConnect
    
    # Function that checks if the account provided is eligible for trading
    # returns True if account is eligible for trading, False otherwise
    def checkForTradeEligibility(self, API_KEY, SECRET_KEY):   
        canTrade = False
        trading_client = TradingClient(API_KEY, SECRET_KEY)
        account = trading_client.get_account()
        try:
            account.trading_blocked
        except Exception as e:
            print('This account is not eligible to trade:', e)
        else:
            canTrade = True

        return canTrade
    
    # Function that connects to Alpaca with an API key, secret key, and base URL
    # returns the connection as an object
    def getConnectionToAlpacaTradeAPI(self, API_KEY, SECRET_KEY, BASE_URL):
            API = alpaca.REST(API_KEY, SECRET_KEY, BASE_URL)
            return API
    
    # Function that tests for both connection and trade eligibility for a given account
    # returns the connnection as an object ONLY IF the account is eligible for trading and there is a valid connection to Alpaca
    def connectToAlpacaAPI(self, API_KEY, SECRET_KEY, BASE_URL):
        tradingapiconnection = None
        
        if (self.checkConnectionToAlpacaTradeAPI(API_KEY, SECRET_KEY, BASE_URL) and 
            self.checkForTradeEligibility(API_KEY, SECRET_KEY)):
            
            tradingapiconnection = self.getConnectionToAlpacaTradeAPI(API_KEY, SECRET_KEY, BASE_URL)
            print('Successfully connected to Alpaca with account eligible for trading.')
                
        return tradingapiconnection

    # Function that gets the buying power for a given account
    # Returns the buying power as a float
    def getAccountBuyingPower(self, API):
        accountbuyingpower = API.get_account().buying_power
        return accountbuyingpower
    
    # Function that checks if a given symbol is in the portfolio
    # Returns True if the symbol is in the portfolio, False otherwise
    def checkForSymbolInPortfolio(self, API, symbol):
        symbolinportfolio = False
        portfolio = API.list_positions()
        for i in portfolio:
            if i.symbol == symbol:
                symbolinportfolio = True
        return symbolinportfolio
    
    # Function that prepares market BUY order data for a given symbol and quantity, then submits a market order to Alpaca
    def submitFractionableBuyOrderToAlpaca(self, API_KEY, SECRET_KEY, API, Symbol, quantity):
        tc = TradingClient(API_KEY, SECRET_KEY)
        assetdetails = API.get_asset(Symbol)
        marketOrderData = ''
        if assetdetails.fractionable:
             marketOrderData = MarketOrderRequest(symbol = Symbol, qty = quantity, 
                                                  side=OrderSide.BUY, time_in_force = TimeInForce.DAY)
        else:
             marketOrderData = MarketOrderRequest(symbol = Symbol, qty = 1, 
                                                  side=OrderSide.BUY, time_in_force = TimeInForce.DAY)
        try:
            tc.submit_order(marketOrderData)
        except Exception as e:
            print('Failed to submit market order to Alpaca.', e)
        else:
            print(f'Market order submitted to buy {Symbol} at {quantity} share(s) to Alpaca successfully.')

    # Function that prepares market SELL order data for a given symbol and quantity, then submits a market order to Alpaca
    def submitSellOrderToAlpaca(self, API_KEY, SECRET_KEY, API, Symbol, quantity):
        tc = TradingClient(API_KEY, SECRET_KEY)
        assetdetails = API.get_asset(Symbol)
        marketOrderData = ''
        if assetdetails.fractionable:
             marketOrderData = MarketOrderRequest(symbol = Symbol, qty = quantity, side=OrderSide.SELL, time_in_force = TimeInForce.DAY)
        else:
             marketOrderData = MarketOrderRequest(symbol = Symbol, qty = 1, side=OrderSide.SELL, time_in_force = TimeInForce.DAY)
        try:
            tc.submit_order(marketOrderData)
        except Exception as e:
            print('Failed to submit market order to Alpaca.', e)
        else:
            print(f'Market order submitted to sell {Symbol} at {quantity} share(s) to Alpaca successfully.')