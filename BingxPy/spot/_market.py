
from ..utils._endpoints  import SpotMarketEndpoints as EP





def server_time(self):
    """Check Server Time
    Test connectivity to the Rest API and get the current server time.
    GET /openApi/spot/v1/server/time
    """
    ep=EP.server_time
    params={}
    return self.send_request(ep.method,ep.path, params)





def symbols(self, symbol: str = None, recv_window: int = None):
    ep=EP.common_symbols
    

    params = {
        "symbol": symbol,
        "recvWindow":recv_window,
        
    }
    return self.send_request(ep.method,ep.path, params)


def recent_trades(self, symbol: str,limit: int = 100, recv_window: int = None):
    
    ep=EP.market_trades
    
    params = {"symbol": symbol, "limit": limit, "recvWindow":recv_window}
    return self.send_request(ep.method,ep.path, params)


def order_book(self, symbol: str,limit: int = 20, recv_window: int = None):
    ep=EP.order_book
    
    params = {"symbol": symbol, "limit": limit, "recvWindow":recv_window}
    return self.send_request(ep.method,ep.path, params)


def order_book_aggregation(self, symbol: str, recv_window: int = None):
    ep=EP.order_book_aggregation
    
    params = {"symbol": symbol, "recvWindow":recv_window}
    return self.send_request(ep.method,ep.path, params)


def historical_klines(self, symbol: str, interval: str, limit: int = 500, start_time: int = None, end_time: int = None,recv_window: int = None):
    """ 
    Historical data after 2024 is supported only
    - limit: Default value: 500 Maximum value: 500
    """
    ep=EP.historical_kline
    
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit,
        "startTime": start_time,
        "endTime": end_time,
        "recvWindow":recv_window}
    
    
    return self.send_request(ep.method,ep.path, params)

def klines(self, symbol: str, interval: str, start_time: int = None, end_time: int = None, limit: int = 500,recv_window: int = None):
    """Up to 15 days of data can be returned"""
    ep=EP.market_kline
    
    params = {
         "symbol": symbol,
        "interval": interval,
        "startTime": start_time,
        "endTime": end_time,
        "limit": limit,
        "recvWindow":recv_window}
    
    
    return self.send_request(ep.method,ep.path, params)


def price_ticker (self, symbol: str, recv_window: int = None):
    ep=EP.price_ticker
  

    params = {"symbol": symbol,  "recvWindow":recv_window}
    return self.send_request(ep.method,ep.path, params)


def order_book_ticker(self, symbol: str,  recv_window: int = None):
    ep=EP.order_book_ticker

    
    params = {"symbol": symbol,  "recvWindow":recv_window}
    return self.send_request(ep.method,ep.path, params)


def ticker_24hr(self, symbol: str , recv_window: int = None):
    ep=EP.ticker_24hr

    
    
    params = {
        "symbol": symbol,
       
        "recvWindow":recv_window,
    }
    return self.send_request(ep.method,ep.path, params)


def old_trade_lookup(self, symbol: str,limit: int=100, fromId: str=None , recv_window: int = None):
    ep=EP.old_trade_lookup
    
    
    params = {
        "symbol": symbol,
        "limit":limit,
        "fromId":fromId,
        "recvWindow":recv_window}
    return self.send_request(ep.method,ep.path, params)







