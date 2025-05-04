
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





    


