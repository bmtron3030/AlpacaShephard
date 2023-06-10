# AlpacaShephard

(This project is NOT associated with the official Alpaca API. Visit https://alpaca.markets/ to use the official Alpaca API)

The AlpacaShephard file is an open-source Python class that works with the Alpaca API by adding a light layer of flexibility already established in the Alpaca API. This project aims to bring more security and protection for users that want to pursue algorithmic trading who seek more readability while maintaining low computing complexity as much as possible. I created this as part of my expirementation/journey in algorithmic trading and wanted a solution that was custom to my requirements.

**Requirements**

This class requires that the _alpaca-trade-api_ and _alpaca-py_ modules are installed in order to work properly. Without them, the class will not function as intended.
To download, visit https://alpaca.markets/ for more information.

**Installation**

1. Make sure that the latest version of Python is installed on your system
2. Download all of the required depndencies (_alpaca-trade-api_ and _alpaca-py_)
3. Download the _AlpacaShephard.py_ file
4. Save it to any desired directory


**Examples**

1. The following code snippet shows an example of the **checkForTradeEligibilty** function, which takes in an _API_KEY_ and _SECRET_KEY_ from any given Alpaca API dashboard, and checks to see if the given credentials are eligible for trading

````
import alpaca_trade_api as alpaca
from alpaca.trading.client import TradingClient
import AlpacaShepherd as AS


alpshep = AS.AlpacaShepherd()

#Not actual Alpaca API keys. Replace with working keys
API_KEY = 'PKIM2YJ1JDIF7VIP7UTB'
SECRET_KEY = 'z8NfOYVEZE8s33ePEU5gsEkbNGbhBeMvfUgJ5DRm'

if (alpshep.checkForTradeEligibility(API_KEY, SECRET_KEY)):
  print('Account is elgible for trading')
else:
  print(' Account is NOT elgible for trading')

````

2. The following code snippet shows an example of the **checkConnectionToAlpacaTradeAPI** function, which takes in an _API_KEY_ and _SECRET_KEY_ from any given Alpaca API dashboard along with a _BASE_URL_ for an endpoint, and checks to make sure that there is a valid connection can be established

````
import alpaca_trade_api as alpaca
from alpaca.trading.client import TradingClient
import AlpacaShepherd as AS


alpshep = AS.AlpacaShepherd()
BASE_URL = https://paper-api.alpaca.markets

#Not actual Alpaca API keys. Replace with working keys
API_KEY = 'PKIM2YJ1JDIF7VIP7UTB'
SECRET_KEY = 'z8NfOYVEZE8s33ePEU5gsEkbNGbhBeMvfUgJ5DRm'

if (alpshep.checkConnectionToAlpacaTradeAPI(API_KEY, SECRET_KEY, BASE_URL)):
  print('Able to connect to Alpaca API account')
else:
  print('Unable to connect to Alpaca API account')

````

3. The following code snippet shows an example of the **connectToAlpacaAPI** function, which takes in an _API_KEY_ and _SECRET_KEY_ from any given Alpaca API dashboard along with a _BASE_URL_ for an endpoint, and returns an _API_ object if successful

````
import alpaca_trade_api as alpaca
from alpaca.trading.client import TradingClient
import AlpacaShepherd as AS


alpshep = AS.AlpacaShepherd()
BASE_URL = https://paper-api.alpaca.markets

#Not actual Alpaca API keys. Replace with working keys
API_KEY = 'PKIM2YJ1JDIF7VIP7UTB'
SECRET_KEY = 'z8NfOYVEZE8s33ePEU5gsEkbNGbhBeMvfUgJ5DRm'

ACCOUNT = alpshep.connectToAlpacaAPI( API_KEY, SECRET_KEY, BASE_URL)

````

4. The following code snippet shows an example of the **checkForSymbolInPortfolio** function, which takes in an _API_ object along with any _SYMBOL_ in the form of a string, and then goes through the account portfolio to check if the _SYMBOL_ is in it. This returns True if the symbol is in the portfolio, False otherwise

````
import alpaca_trade_api as alpaca
from alpaca.trading.client import TradingClient
import AlpacaShepherd as AS


alpshep = AS.AlpacaShepherd()
BASE_URL = https://paper-api.alpaca.markets

#Not actual Alpaca API keys. Replace with working keys
API_KEY = 'PKIM2YJ1JDIF7VIP7UTB'
SECRET_KEY = 'z8NfOYVEZE8s33ePEU5gsEkbNGbhBeMvfUgJ5DRm'

ACCOUNT = alpshep.connectToAlpacaAPI( API_KEY, SECRET_KEY, BASE_URL)
SYMBOL = 'AAPL'

if (alpshep.checkForSymbolInPortfolio(ACCOUNT, SYMBOL)):
  print(f'{SYMBOL} is in this account portfolio')
else:
  print(f'{SYMBOL} is in not this account portfolio')

````
