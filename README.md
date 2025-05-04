# BingX API Connector Python (Bixpy)

[![PyPI version](https://img.shields.io/pypi/v/Bixpy)](https://pypi.python.org/pypi/Bixpy)
[![Python version](https://img.shields.io/pypi/pyversions/Bixpy)](https://www.python.org/downloads/)
[![Documentation](https://img.shields.io/badge/docs-latest-blue)](https://github.com/abbas-bachari/Bixpy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



This is a lightweight library that works as a connector to [BingX public API](https://Bingx-api.github.io/docs/)

## Installation

```bash
pip install Bixpy
```

## Supported functionality

### Account & Wallet API

- Spot account
- Sub-account
- Wallet deposits and withdrawals
- Agant

### Spot API

- Market Interface
- Trade interface
- Websocket Market Data
- Websocket Account Data

### Perpetual Futures API

- Market Interface
- Account Interface
- Trade Interface
- Websocket Market Data
- Websocket Account Data

### Standard Contract API

- Standard Contract Interface

### Copy Trading API

- Copy Trading Interface

### Importing

```python
def on_message(ws, data: dict) -> None:
    """
    Event handler for SpotWebsocket messages
    """
    print(data)


proxies ={ 'https': 'http://127.0.0.1:10809' }
api_key="YOUR API KEY"
secret_key="YOUR API SECRET"


# ACCOUNT AND WALLET  
from Bixpy  import Account

account=Account(api_key=api_key,api_secret= secret_key, proxies=proxies)
get_listen_key=account.generate_listen_Key()
listen_key=get_listen_key["listenKey"]





#  SPOT
from Bixpy  import Spot
from Bixpy  import SpotAcccountWebsocket
from Bixpy  import SpotMarketWebsocket
from Bixpy  import SpotOrder

spot=Spot(api_key=api_key,api_secret= secret_key, proxies=proxies)
ws_spot_account=SpotAcccountWebsocket(listen_key=listen_key, on_message=on_message, proxies=proxies)
ws_spot_market=SpotMarketWebsocket( on_message=on_message, proxies=proxies)



# PERPETUAL FUTURES
from Bixpy  import Perpetual
from Bixpy import PerpetualMarketWebsocket
from Bixpy import PerpetualAccountWebsocket
from Bixpy import PerpetualOrder,PerpetualOrderReplace

perpetual=Perpetual(api_key=api_key,api_secret= secret_key, proxies=proxies)

ws_perpetual_market=PerpetualMarketWebsocket(on_message=on_message, proxies=proxies)

ws_perpetual_account=PerpetualAccountWebsocket(listen_key=listen_key, on_message=on_message, proxies=proxies)



# STANDARD FUTURES
from Bixpy import Standard

standard=Standard(api_key=api_key,api_secret= secret_key, proxies=proxies)



# COPY TRADING
from Bixpy import CopyTrading

copy_trading=CopyTrading(api_key=api_key,api_secret= secret_key, proxies=proxies)
```

## Spot

Usage examples:

```python
from Bixpy  import Spot,SpotOrder

spot=Spot()
# Get server timestamp
print(spot.server_time())
# Get klines of BTCUSDT at 1m interval
print(spot.kline("BTC-USDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
print(spot.kline("BNB-USDT", "1h", limit=10))

# API key/secret are required for trade endpoints
spot = Spot(api_key='<api_key>', api_secret='<api_secret>')

order=SpotOrder(symbol="BTC-USDT",side="BUY",order_type="LIMIT",quantity=0.002,price=9500,time_in_force="GTC")

print(spot.new_order(order))
```

### Proxy

Proxy is supported.

```python
from Bixpy import Spot

proxies ={ 'https': 'http://127.0.0.1:10809' }

client= Spot(proxies=proxies)
```

### Account & Wallet

```python
from Bixpy  import Account


proxies ={ 'https': 'http://127.0.0.1:10809' }
api_key="YOUR API KEY"
secret_key="YOUR API SECRET"

account=Account(api_key=api_key,api_secret= secret_key, proxies=proxies)

balance=account.balance()

print(f'Asset{"":<10}Available{"":<20}Locked')

print("_"*50)

for coin in balance["data"]["balances"]:
    print(f'{coin["asset"]:<15}{coin["free"]:<30}{coin["locked"]}')

"""
Asset          Available                    Locked
__________________________________________________
USDT           2.2821580243871558            0
ZAT            3                             0
TONCOIN        0.0006540539999999999         0
SUI            0                             0
GOAT           0                             0
BNB            0                             0
DOGS           0                             0
MAJOR          0                             0
SSE            0                             0
ICE            0                             0
MEMEFI         0                             0
VST            100008.04091207               0
AIDOGE         0                             0
HMSTR          0                             0
XRP            0                             0
NOT            0                             0
TRX            0                             0
RAY            0                             0
""" 

```

### Websocket

```python
from Bixpy  import SpotMarketWebsocket
from time import sleep

proxies ={ 'https': 'http://127.0.0.1:10809' }

def on_message(ws, data: dict) -> None:
    """
    Event handler for SpotWebsocket messages
    """
    print(data)

ws=SpotMarketWebsocket( on_message=on_message,proxies=proxies )
ws.kline("BTC-USDT","1min")
sleep(30)
ws.stop()
```

### Donate

**TonCoin and other tokens of the TON network:**

**Wallet:** **abbas-bachari.ton**

_If you are planning to send another token, please contact me._

### Sponsor

Alternatively, sponsor me on Github using [Github Sponsors](https://github.com/sponsors/abbas-bachari).
