from ..utils.api_client import ApiClient as __api
from ..utils.urls import URL

 
   
class CopyTrading(__api):
    def __init__(self, api_key:str, api_secret:str,proxies: dict= None,timeout: int =None, demo:bool=False, **kwargs):
        
        base_url=kwargs.get("base_url")
        if not base_url:
            kwargs["base_url"] = URL.COPY_TRADING_BASE_DEMO if demo else URL.COPY_TRADING_BASE
        
        kwargs["api_key"] = api_key
        kwargs["api_secret"] = api_secret
        kwargs["timeout"] = timeout
        kwargs["proxies"] = proxies
        super().__init__(**kwargs)
        
       
    from ._interface import (
        get_current_order,
        close_positions,
        set_profit_and_loss,
        sell_order
    )

    