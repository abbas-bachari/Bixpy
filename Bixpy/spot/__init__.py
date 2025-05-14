
from ..utils.ws_client import WebsocketClient as __wsc
from ..utils.api_client import ApiClient as __api_client
from ..utils.objects  import SpotOrder
class Spot(__api_client):
    """kwargs:
        - base_url='https://api.bingx.com'
    """
    def __init__(self, api_key: str = None, secret_key: str = None, proxies: dict = None, timeout: int = None, demo: bool = False, **kwargs):
        """
        Initialize a Spot client.

        Parameters
        ----------
        api_key : str
            The API key to use.
        secret_key : str
            The API secret to use.
        proxies : dict
            The proxies to use.
        timeout : int
            The timeout to use.
        demo : bool
            Whether to use the demo API.
        """
        base_url = kwargs.get("base_url")
        if not base_url:
            from ..utils.urls import SPOT
            kwargs["base_url"] = SPOT.REST_DEMO if demo else SPOT.REST
        kwargs["api_key"] = api_key
        kwargs["secret_key"] = secret_key
        kwargs["timeout"] = timeout
        kwargs["proxies"] = proxies
        super().__init__(**kwargs)
        self._account = None
        self._market = None
        self._trade = None
    
    
    def server_time(self):
        """Check Server Time
        Test connectivity to the Rest API and get the current server time.
        GET /openApi/spot/v1/server/time
        """
        return self.send_request('GET','/openApi/spot/v1/server/time')
    @property
    def account(self):
        
        if not self._api_key or not self._secret_key:
            raise ValueError("API key and secret must be provided.")

        if not self._account:
            from ._account import SpotAccount
            self._account = SpotAccount(self)
        return self._account

    @property
    def market(self):
        if not self._market:
            from ._market import SpotMarket
            self._market = SpotMarket(self)
        return self._market

    @property
    def trade(self):
        if not self._api_key or not self._secret_key:
            raise ValueError("API key and secret must be provided.")
        if not self._trade:
            from ._trade import SpotTrade
            self._trade = SpotTrade(self)
        return self._trade

class SpotWebsocket(__wsc):
    """ Spot Websocket Public Client """
    def __init__(self,listen_key: str=None, on_message=None, on_open=None, on_close=None, on_error=None, on_ping=None, on_pong=None, logger=None, timeout=None, proxies=None, demo=False, **kwargs):
        stream_url = kwargs.get("stream_url")
        if not stream_url:
            from ..utils.urls import SPOT
            stream_url = SPOT.STREAM_DEMO if demo else SPOT.STREAM
            kwargs['stream_url'] = f'{stream_url}?listenKey={listen_key}' if listen_key else f'{stream_url}'
        self._listen_key = listen_key
        kwargs.update({
            "on_message": on_message,
            "on_open": on_open,
            "on_close": on_close,
            "on_error": on_error,
            "on_ping": on_ping,
            "on_pong": on_pong,
            "logger": logger,
            "timeout": timeout,
            "proxies": proxies
        })
        
        super().__init__(**kwargs)
    
    def trade(self, symbol: str, id=None, action=None):
        """
        Subscribe to trade events of a symbol.

        Parameters
        ----------
        symbol : str
            The symbol to subscribe to.
        id : str, optional
            The request id, if not provided, will be generated.
        action : str, optional
            The action to take, either 'sub' or 'unsub', if not provided, will default to 'sub'.
        

        Notes
        -----
        If `action` is not provided, will default to 'sub'.
        If `id` is not provided, will be generated.

        """
        stream_name = f"{symbol.upper()}@trade"

        self.send_message_to_server(stream_name, action=action, id=id)

    def kline(self, symbol: str, interval: str, id=None, action=None):
            
            """
            Subscribe to kline events of a symbol.

            Parameters
            ----------
            symbol : str
                The symbol to subscribe to.
            interval : str
                * The interval of the kline,
                * valid values are: 1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 8hour, 12hour, 1day, 3day, 1week, 1mon
            id : str, optional
                * The request id, if not provided, will be generated.
            action : str, optional
                * The action to take, either 'sub' or 'unsub', if not provided, will default to 'sub'.

            Notes
            -----
            If `action` is not provided, will default to 'sub'.
            If `id` is not provided, will be generated.

            """
            stream_name = f"{symbol.upper()}@kline_{interval}"

            self.send_message_to_server(stream_name, action=action, id=id)

    def depth(self, symbol: str, level:int=50, id=None, action=None):
            """

            Update level: 5,10,20,50,100

            Order book price and quantity depth updates used to locally manage an order book.
            """
            
            self.send_message_to_server(f"{symbol.upper()}@depth{level}", action=action, id=id)

    def price_24h(self, symbol: str,  id=None, action=None):
            
            """
            Subscribe to 24-hour rolling window price change statistics for a symbol.

            Parameters
            ----------
            symbol : str
                The symbol to subscribe to.
            id : str, optional
                The request id, if not provided, will be generated.
            action : str, optional
                The action to take, either 'sub' or 'unsub', if not provided, will default to 'sub'.

            Notes
            -----
            If `action` is not provided, will default to 'sub'.
            If `id` is not provided, will be generated.

            """
            self.send_message_to_server(f"{symbol.upper()}@ticker", action=action, id=id)
        
    def last_price(self, symbol: str,  id=None, action=None):
            
            """
            Subscribe to the last price for a symbol.

            Parameters
            ----------
            symbol : str
                The symbol to subscribe to.
            id : str, optional
                The request id, if not provided, will be generated.
            action : str, optional
                The action to take, either 'sub' or 'unsub', if not provided, will default to 'sub'.

            Notes
            -----
            If `action` is not provided, will default to 'sub'.
            If `id` is not provided, will be generated.
            """

            self.send_message_to_server(f"{symbol.upper()}@lastPrice", action=action, id=id)
    
    def best_order_book(self, symbol: str,  id=None, action=None):
            """
            Subscribe to the best order book for a symbol.

            Parameters
            ----------
            symbol : str
                The symbol to subscribe to.
            id : str, optional
                The request id, if not provided, will be generated.
            action : str, optional
                The action to take, either 'sub' or 'unsub', if not provided, will default to 'sub'.

            Notes
            -----
            If `action` is not provided, will default to 'sub'.
            If `id` is not provided, will be generated.
            """
            self.send_message_to_server(f"{symbol.upper()}@bookTicker", action=action, id=id)
    def incremental_depth(self, symbol: str,  id=None, action=None):
            """
            Subscribe to the incremental depth for a symbol.

            Parameters
            ----------
            symbol : str
                The symbol to subscribe to.
            id : str, optional
                The request id, if not provided, will be generated.
            action : str, optional
                The action to take, either 'sub' or 'unsub', if not provided, will default to 'sub'.

            Notes
            -----
            If `action` is not provided, will default to 'sub'.
            If `id` is not provided, will be generated.
            """
            self.send_message_to_server(f"{symbol.upper()}@incrDepth", action=action, id=id)
    def order_update_data(self,  id=None, action=None):
        if not self._listen_key:
            raise Exception("Listen key is required")

        self.send_message_to_server("spot.executionReport", action=action, id=id)

    def account_update(self, id=None, action=None):
        if not self._listen_key:
            raise ValueError("Listen key is required")
        self.send_message_to_server("ACCOUNT_UPDATE", action=action, id=id)



__all__ = ["Spot","SpotOrder" ,"SpotWebsocket"]
