

from ..utils._endpoints import PerpetualMarketEndpoints as EP




 
    
    
    
    
        
def get_server_time(self,recv_window: int = None):
        ep=EP.get_server_time
        params={"recvWindow":recv_window}
        return self.send_request(ep.method,ep.path, params)
    
def get_symbols(self,symbol: str = None,recv_window: int = None):
        ep=EP.get_symbols
        params={
            "symbol":symbol,
            "recvWindow":recv_window
            }
        return self.send_request(ep.method,ep.path, params)
    
def get_order_book(self,symbol: str,limit: int = None,recv_window: int = None):
        """
        limit:
        Default 20, optional value:[5, 10, 20, 50, 100, 500, 1000]
        """
        ep=EP.order_book
        params={
                "symbol": symbol,
                "limit": limit,
                "recvWindow":recv_window
                }
        return self.send_request(ep.method,ep.path, params)
    
def get_recent_trades(self,symbol: str,limit: int = None,recv_window: int = None):
        """
        limit:
        Default 500, maximum 1000
        """
        ep=EP.recent_trades_list
        params={
                "symbol": symbol,
                "limit": limit,
                "recvWindow":recv_window
                }
        return self.send_request(ep.method,ep.path, params)
    
def price_and_funding_rate(self,symbol: str=None,recv_window: int = None):
        ep=EP.mark_price_and_funding_rate 
        params={
                symbol:symbol,
                "recvWindow":recv_window
                }
        return self.send_request(ep.method,ep.path, params)
    
def get_funding_rate(self,symbol: str=None,recv_window: int = None):
        ep=EP.get_funding_rate_history
        params={
                symbol:symbol,
                "recvWindow":recv_window
                }
        return self.send_request(ep.method,ep.path, params)
    
def get_klines(self, symbol: str, interval: str, start_time: int = None, end_time: int = None, limit: int = None, recv_window: int = None):
    """ 
    interval:
    "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"
    limit:
    Default: 500 maximum: 1440
    """
    ep = EP.kline_data
    params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": start_time,
        "endTime": end_time,
        "limit": limit,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)
    
def get_open_interest_Statistics(self,symbol: str,recv_window: int = None):
        ep=EP.open_interest_statistics

        params={
                symbol:symbol,
                "recvWindow":recv_window}
        return self.send_request(ep.method,ep.path, params)

def get_24hr_price_change(self,symbol: str=None,recv_window: int = None):
        ep=EP.get_24hr_ticker_price_change
        params={
                symbol:symbol,
                "recvWindow":recv_window}
        return self.send_request(ep.method,ep.path, params)



      
def historical_transaction_orders(self,from_id: int = None,symbol: str = None,limit: int = None,recv_window: int = None):
        ep=EP.historical_transaction_orders
        params={
                "fromId": from_id,
                "symbol": symbol,
                "limit": limit,
                "recvWindow":recv_window}
        return self.send_request(ep.method,ep.path, params)




def symbol_order_book_ticker(self,symbol: str,recv_window: int = None):
        ep=EP.symbol_order_book_ticker
        params={
                symbol:symbol,
                "recvWindow":recv_window}
        return self.send_request(ep.method,ep.path, params)

    
def get_mark_price_klines(self, symbol: str, interval: str, start_time: int = None, end_time: int = None, limit: int = None, recv_window: int = None):
        """
        Get mark price klines.
        Parameters:
        symbol (str): required
        interval (str): required. "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"
        start_time (int): optional
        end_time (int): optional
        limit (int): optional. Default: 500, max: 1440

        
        """
        ep = EP.mark_price_kline
        params = {
            "symbol": symbol,
            "interval": interval,
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "recvWindow":recv_window
        }
        return self.send_request(ep.method, ep.path, params)
    
def symbol_price_ticker(self,symbol: str=None, recv_window: int = None):
        ep=EP.symbol_price_ticker
        params={
                symbol:symbol,
                "recvWindow":recv_window}
        return self.send_request(ep.method,ep.path, params)








