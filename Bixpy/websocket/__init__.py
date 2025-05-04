

from ..utils.ws_client import WebsocketClient as __wsc
from ..utils.urls import URL as __URL__



class SpotMarketWebsocket(__wsc):
    def __init__( self,on_message=None,on_open=None,on_close=None,on_error=None,on_ping=None,on_pong=None,logger=None,timeout=None,proxies:dict = None,demo:bool=False,**kwargs): 
        stream_url=kwargs.get("stream_url",None)
        if not stream_url:
            kwargs["stream_url"] = __URL__.SPOT_STREAM_DEMO if demo else __URL__.SPOT_STREAM
        
        
        kwargs["on_message"] = on_message
        kwargs["on_open"] = on_open
        kwargs["on_close"] = on_close
        kwargs["on_error"] = on_error
        kwargs["on_ping"] = on_ping
        kwargs["on_pong"] = on_pong
        kwargs["logger"] = logger
        kwargs["timeout"] = timeout
        kwargs["proxies"] = proxies
        super().__init__(**kwargs)

    from ._spot import (
        trade,
        kline,
        depth,
        price_24h,
        last_price,
        best_order_book,
        incremental_depth
        ) 
        
class SpotAcccountWebsocket(__wsc):
    def __init__( self,listen_key:str,on_message=None,on_open=None,on_close=None,on_error=None,on_ping=None,on_pong=None,logger=None,timeout=None,proxies:dict = None,demo:bool=False,**kwargs): 
        
        stream_url=kwargs.get("stream_url",None)
        if not stream_url:
            stream_url = __URL__.SPOT_STREAM_DEMO if demo else __URL__.SPOT_STREAM
            kwargs["stream_url"] = f"{stream_url}?listenKey={listen_key}"
        
        kwargs["on_message"] = on_message
        kwargs["on_open"] = on_open
        kwargs["on_close"] = on_close
        kwargs["on_error"] = on_error
        kwargs["on_ping"] = on_ping
        kwargs["on_pong"] = on_pong
        kwargs["logger"] = logger
        kwargs["timeout"] = timeout
        kwargs["proxies"] = proxies
        super().__init__(**kwargs)

    from ._spot import (
        order_update_data,
        account_balance_push
    )      


class PerpetualMarketWebsocket(__wsc):
    
    def __init__( self,on_message=None,on_open=None,on_close=None,on_error=None,on_ping=None,on_pong=None,logger=None,timeout=None,proxies:dict = None,demo:bool=False,**kwargs): 
        stream_url=kwargs.get("stream_url",None)
        if not stream_url:
            kwargs["stream_url"] = __URL__.PERPETUAL_STREAM_DEMO if demo else __URL__.PERPETUAL_STREAM
        
       
        kwargs["on_message"] = on_message
        kwargs["on_open"] = on_open
        kwargs["on_close"] = on_close
        kwargs["on_error"] = on_error
        kwargs["on_ping"] = on_ping
        kwargs["on_pong"] = on_pong
        kwargs["logger"] = logger
        kwargs["timeout"] = timeout
        kwargs["proxies"] = proxies
        super().__init__(**kwargs)
        
        
    
    def __initialize_client__(self,listen_key=None):
        
        
        stream_url=self.kwargs['stream_url']
        if listen_key:
            stream_url = f"{stream_url}?listenKey={listen_key}"
        
        
        
            
        if self.__stream_url == stream_url:
            return
        
       
        if self.__stream_url:
            self.stop()
        
        
        self.__stream_url=stream_url
        self.kwargs['stream_url'] = stream_url
        
        super().__init__(**self.kwargs)
    
    
        


    from ._perpetual import (
            market_depth,
            latest_trade_detail,
            kline_data,
            price_changes_24hour,
            latest_price_changes,
            latest_price_changes_mark,
            book_ticker_streams,
            incremental_depth_information
            
        )

class PerpetualAccountWebsocket(__wsc):
    def __init__( self,listen_key:str,on_message=None,on_open=None,on_close=None,on_error=None,on_ping=None,on_pong=None,logger=None,timeout=None,proxies:dict = None,demo:bool=False,**kwargs): 
        stream_url=kwargs.get("stream_url",None)
        if not stream_url:
            stream_url = __URL__.PERPETUAL_STREAM_DEMO if demo else __URL__.PERPETUAL_STREAM
            kwargs["stream_url"] = f"{stream_url}?listenKey={listen_key}"
       
        kwargs["on_message"] = on_message
        kwargs["on_open"] = on_open
        kwargs["on_close"] = on_close
        kwargs["on_error"] = on_error
        kwargs["on_ping"] = on_ping
        kwargs["on_pong"] = on_pong
        kwargs["logger"] = logger
        kwargs["timeout"] = timeout
        kwargs["proxies"] = proxies
        
        super().__init__(**kwargs)
        
        
    
        
        