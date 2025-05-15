<h1 align="center">BingX API Connector Python (Bixpy)</h1>
<p align="center">
<a href="https://github.com/abbas-bachari/Bixpy"><img src="https://img.shields.io/badge/Python%20-3.7+-green?style=plastic&logo=Python" alt="Python"></a>
  <a href="https://pypi.org/project/Bixpy/"><img src="https://img.shields.io/pypi/v/Bixpy?style=plastic" alt="PyPI - Version"></a>
  <a href="https://pypi.org/project/Bixpy/"><img src="https://img.shields.io/pypi/l/Bixpy?style=plastic" alt="License"></a>
  <a href="https://pepy.tech/project/Bixpy"><img src="https://pepy.tech/badge/Bixpy?style=flat-plastic" alt="Downloads"></a>
</p>

### This is a lightweight library that works as a connector to [BingX public API](https://Bingx-api.github.io/docs/)

## 🛠️ Version 1.0.3

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
from Bixpy.account import Account

account=Account(api_key=api_key,secret_key= secret_key, proxies=proxies)
get_listen_key=account.listen_key.generate()
listen_key=get_listen_key["listenKey"]





#  SPOT
from Bixpy.spot  import Spot
from Bixpy.spot import SpotWebsocket
from Bixpy.spot import SpotOrder

spot=Spot(api_key=api_key,secret_key= secret_key, proxies=proxies)

ws_spot_account=SpotWebsocket(listen_key=listen_key, on_message=on_message, proxies=proxies)

ws_spot_market=SpotWebsocket( on_message=on_message, proxies=proxies)




# PERPETUAL FUTURES
from Bixpy.perpetual  import Perpetual
from Bixpy.perpetual import PerpetualWebsocket
from Bixpy.perpetual import PerpetualOrder,PerpetualOrderReplace

perpetual=Perpetual(api_key=api_key,secret_key= secret_key, proxies=proxies)

ws_perpetual_account=PerpetualWebsocket(listen_key=listen_key, on_message=on_message, proxies=proxies)

ws_perpetual_market=PerpetualWebsocket(on_message=on_message, proxies=proxies)





# STANDARD FUTURES
from Bixpy.standard import Standard

standard=Standard(api_key=api_key,secret_key= secret_key, proxies=proxies)



# COPY TRADING
from Bixpy.copy_trading import CopyTrading

copy_trading=CopyTrading(api_key=api_key,secret_key= secret_key, proxies=proxies)
```

## Spot

Usage examples:

```python
from Bixpy.spot  import Spot,SpotOrder

spot=Spot(proxies=proxies)
# Get server timestamp
print(spot.server_time())
# Get klines of BTCUSDT at 1m interval
print(spot.market.klines("BTC-USDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
print(spot.market.klines("BNB-USDT", "1h", limit=10))

# API key/secret are required for trade endpoints
spot = Spot(api_key='<api_key>', secret_key='<secret_key>')

order=SpotOrder(symbol="BTC-USDT",side="BUY",order_type="LIMIT",quantity=0.002,price=9500,time_in_force="GTC")

print(spot.trade.place_order(order))
```

### Proxy

Proxy is supported.

```python
from Bixpy.spot import Spot

proxies ={ 'https': 'http://127.0.0.1:10809' }

client= Spot(proxies=proxies)
```

### Account & Wallet

```python
from Bixpy.account  import Account


proxies ={ 'https': 'http://127.0.0.1:10809' }
api_key="YOUR API KEY"
secret_key="YOUR API SECRET"

account=Account(api_key=api_key,secret_key= secret_key, proxies=proxies)

balance=account.fund.balance()

print(f'Asset{"":<10}Available{"":<16}Locked')

print("_"*50)

for coin in balance["data"]["balances"]:
    print(f'{coin["asset"]:<15}{float(coin["free"]):<25.8f}{float(coin["locked"]):.8f}')

"""
Asset          Available                Locked
__________________________________________________
ZAT            3.00000000               0.00000000
USDT           0.00000001               0.00000000
VST            100008.04091207          0.00000000
DOGS           0.00000000               0.00000000
MAJOR          0.00000000               0.00000000
RAY            0.00000000               0.00000000
ICE            0.00000000               0.00000000
NOT            0.00000000               0.00000000
TONCOIN        0.00065405               0.00000000
SUI            0.00000000               0.00000000
MEMEFI         0.00000000               0.00000000
GOAT           0.00000000               0.00000000
HMSTR          0.00000000               0.00000000
TRX            0.00000000               0.00000000
SSE            0.00000000               0.00000000
XRP            0.00000000               0.00000000
BNB            0.00000000               0.00000000
AIDOGE         0.00000000               0.00000000
""" 

```

### Websocket

```python

from Bixpy.spot  import SpotWebsocket
from time import sleep

proxies ={ 'https': 'http://127.0.0.1:10809' }


def fitch_kline_data(response: dict) -> None:
    """
    Event handler for SpotWebsocket messages
    """
   
    data=response.get("K",{})
    kline_data={
        "event_time": datetime.fromtimestamp(response.get("E")//1000).replace(microsecond=0) if response.get("E") else None,
        "kline": {
            "symbol": data.get("s"),
            "interval": data.get("i"),
            "open_time": datetime.fromtimestamp(data.get("t")//1000).replace(microsecond=0) if data.get("t") else None,
            "close_time": datetime.fromtimestamp(data.get("T")//1000).replace(microsecond=0) if data.get("T") else None,
            "open": f'{float(data.get("o")):.8f}' if data.get("o") else None,
            "high": f'{float(data.get("h")):.8f}' if data.get("h") else None,
            "low": f'{float(data.get("l")):.8f}' if data.get("l") else None,
            "close": f'{float(data.get("c")):.8f}' if data.get("c") else None,
            "volume": f'{float(data.get("v")):.8f}' if data.get("v") else None,
            "quote_volume": f'{float(data.get("q")):.8f}' if data.get("q") else None,
            "trade_count": data.get("n")
        },
        "event_type": response.get("e"),
        "symbol": response.get("s")
    }
    return kline_data


def on_message(ws, response: dict) -> None:
    """
    Event handler for SpotWebsocket messages
    """
    data=response.get("data")
    msg=response.get("msg")
    if msg:
        # print(f"Response Message:   {msg}" ) 
        pass
    elif data:
        # print(data)
        kline_data=fitch_kline_data(data)['kline']
        kline_data.pop('close_time',None)
        kline_data.pop('symbol',None)
        kline_data.pop('interval',None)
        values=''.join([f"│ {str(value):<22}" for value in kline_data.values()]).strip()
        print(f"{values:<{len(head)-1}}│")


        
ws=SpotWebsocket( on_message=on_message,proxies=proxies )
kline_data=fitch_kline_data({})['kline']
kline_data.pop('close_time',None)
kline_data.pop('symbol',None)
kline_data.pop('interval',None)
head=''.join([f"│ {key:<22}" for key in kline_data.keys()]).strip()+"  │"
print("—"*len(head))
print(head)
print("—"*len(head))
ws.kline("BTC-USDT","1min")
sleep(10)

ws.stop()
print("—"*len(head))
```

### Result:

```bash
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
│ open_time             │ open                  │ high                  │ low                   │ close                 │ volume                │ quote_volume          │ trade_count  │
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103505.53000000       │ 103492.33000000       │ 103505.53000000       │ 0.08083400            │ 8366.39132100         │ 127          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103505.53000000       │ 103492.33000000       │ 103505.51000000       │ 0.08407100            │ 8701.38695200         │ 132          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103505.53000000       │ 103492.33000000       │ 103505.51000000       │ 0.08417600            │ 8712.25503000         │ 134          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103505.53000000       │ 103492.33000000       │ 103505.51000000       │ 0.08417600            │ 8712.25503000         │ 134          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103505.86000000       │ 103492.33000000       │ 103505.86000000       │ 0.08538900            │ 8837.80763800         │ 136          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103505.86000000       │ 103492.33000000       │ 103505.86000000       │ 0.08588800            │ 8889.50881500         │ 138          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103505.86000000       │ 103492.33000000       │ 103505.85000000       │ 0.08746900            │ 9053.09981600         │ 140          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103505.86000000       │ 103492.33000000       │ 103505.85000000       │ 0.08746900            │ 9053.09981600         │ 140          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.40000000       │ 0.08922600            │ 9234.96056100         │ 142          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.40000000       │ 0.08922600            │ 9234.96056100         │ 142          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.39000000       │ 0.08950200            │ 9249.24444300         │ 144          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.39000000       │ 0.08950200            │ 9263.52832500         │ 144          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.38000000       │ 0.09022800            │ 9338.67395700         │ 146          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.38000000       │ 0.09022800            │ 9338.67395700         │ 146          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.38000000       │ 0.09050700            │ 9367.55223700         │ 148          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.38000000       │ 0.09050700            │ 9367.55223700         │ 148          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.37000000       │ 0.09121400            │ 9440.73124000         │ 150          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.37000000       │ 0.09192100            │ 9513.91024400         │ 150          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.38000000       │ 0.09301000            │ 9626.62869200         │ 152          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.38000000       │ 0.09329200            │ 9655.81749100         │ 154          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.38000000       │ 0.09329200            │ 9655.81749100         │ 154          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.39000000       │ 0.09432000            │ 9762.27381300         │ 155          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.38000000       │ 0.09625900            │ 9962.92094100         │ 158          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.38000000       │ 0.09775700            │ 10117.97349800        │ 162          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.38000000       │ 0.09734100            │ 10074.91484400        │ 160          │
│ 2025-05-16 02:26:00   │ 103499.52200000       │ 103506.40000000       │ 103492.33000000       │ 103506.38000000       │ 0.09775700            │ 10117.97349800        │ 162          │
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

```

### Donate

**TonCoin and other tokens of the TON network:**

**Wallet:** **abbas-bachari.ton**

_If you are planning to send another token, please contact me._

### Sponsor

Alternatively, sponsor me on Github using [Github Sponsors](https://github.com/sponsors/abbas-bachari).
