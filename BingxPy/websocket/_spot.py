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
        """stream_url: wss://open-api-ws.bingx.com/market?listenKey="""
        
        self.send_message_to_server("spot.executionReport", action=action, id=id)

def account_balance_push(self, id=None, action=None):
        
        """stream_url: strimwss://open-api-ws.bingx.com/market?listenKey="""
        self.send_message_to_server("ACCOUNT_UPDATE", action=action, id=id)

    

