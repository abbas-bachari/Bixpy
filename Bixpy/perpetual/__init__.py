
from ..utils.api_client import ApiClient as __api_client
from ..utils.ws_client import WebsocketClient as __wsc
from ..utils.objects import PerpetualOrder,PerpetualOrderReplace

class Perpetual(__api_client):
    def __init__(self, api_key: str = None, secret_key: str = None, proxies: dict = None, timeout: int = None, demo: bool = False, **kwargs):
        if "base_url" not in kwargs:
            from ..utils.urls import  PERPETUAL
            kwargs["base_url"] = PERPETUAL.REST_DEMO if demo else PERPETUAL.REST
        
        kwargs.update({
            "api_key": api_key,
            "secret_key": secret_key,
            "timeout": timeout,
            "proxies": proxies
        })
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
        
        if self._account is None:
            from ._account import PerpetualAccount
            self._account = PerpetualAccount(self)
        return self._account

    @property
    def market(self):
        if self._market is None:
            from ._market import PerpetualMarket
            self._market = PerpetualMarket(self)
        return self._market

    @property
    def trade(self):
        if not self._api_key or not self._secret_key:
            raise ValueError("API key and secret must be provided.")
        if self._trade is None:
            from ._trade import PerpetualTrade
            self._trade = PerpetualTrade(self)
        return self._trade
    




class PerpetualWebsocket(__wsc):
    """Perpetual Websocket Public API."""
    
    def __init__(
        self,
        listen_key: str=None,
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
        on_ping=None,
        on_pong=None,
        logger=None,
        timeout=None,
        proxies=None,
        demo=False,
        **kwargs
    ):
        

        stream_url = kwargs.get("stream_url")
        if not stream_url:
            from ..utils.urls import PERPETUAL
           
            stream_url = PERPETUAL.STREAM_DEMO if demo else PERPETUAL.STREAM
            kwargs["stream_url"] = f"{stream_url}?listenKey={listen_key}" if listen_key else stream_url
            
        self._listen_key = listen_key
        kwargs.update(
            {
                "on_message": on_message,
                "on_open": on_open,
                "on_close": on_close,
                "on_error": on_error,
                "on_ping": on_ping,
                "on_pong": on_pong,
                "logger": logger,
                "timeout": timeout,
                "proxies": proxies,
            }
        )
        super().__init__(**kwargs)
        
        


    def market_depth(self, symbol: str, level: int = 50, id: str = None, action: str = None):
        """Subscribe to market depth of a symbol.

        Parameters
        ----------
        symbol : str
            The symbol to subscribe to.
        level : int, optional
            The depth level, such as 5, 10, 20, 50, 100. Defaults to 50.
        id : str, optional
            The request id, if not provided, will be generated.
        action : str, optional
            The action to take, either 'sub' or 'unsub', if not provided, will default to 'sub'.
        **kwargs
            Additional keyword arguments.

        Notes
        -----
        If `action` is not provided, will default to 'sub'.
        If `id` is not provided, will be generated.
        """
        self.send_message_to_server(f"{symbol.upper()}@depth{level}", action=action, id=id)
    def latest_trade_detail(self, symbol: str, id=None, action=None):
        self.send_message_to_server(f"{symbol.upper()}@trade", action=action, id=id)

    def kline_data(self, symbol: str, interval: str, id=None, action=None):
            
    

        """Subscribe to kline data of a symbol.

        Parameters
        ----------
        symbol : str
            The symbol to subscribe to.
        interval : str
            The interval of the kline, such as 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M.
        id : str, optional
            The request id, if not provided, will be generated.
        action : str, optional
            The action to take, either 'sub' or 'unsub', if not provided, will default to 'sub'.

        Notes
        -----
        If `action` is not provided, will default to 'sub'.
        If `id` is not provided, will be generated.
        """
        self.send_message_to_server(f"{symbol.upper()}@kline_{interval}", action=action, id=id)

    def  price_changes_24hour (self, symbol: str,  id=None, action=None):
            
        
        self.send_message_to_server(f"{symbol.upper()}@ticker", action=action, id=id)
        
    def latest_price_changes(self, symbol: str,  id=None, action=None):
            
            
        self.send_message_to_server(f"{symbol.upper()}@lastPrice", action=action, id=id)
    
    def latest_price_changes_mark(self, symbol: str,  id=None, action=None):
            
        self.send_message_to_server(f"{symbol.upper()}@markPrice", action=action, id=id)

    def book_ticker_streams(self, symbol: str,  id=None, action=None):
        
        self.send_message_to_server(f"{symbol.upper()}@bookTicker", action=action, id=id)
    def incremental_depth_information(self, symbol: str,  id=None, action=None):
        
        self.send_message_to_server(f"{symbol.upper()}@incrDepth", action=action, id=id)

    def account_update(self):
        
        if not self._listen_key:
            raise ValueError("Listen key is not provided.")
       





__all__ = ['Perpetual', 'PerpetualWebsocket',"PerpetualOrder","PerpetualOrderReplace"]