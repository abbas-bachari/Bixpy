from ..utils.api_client import ApiClient as __api_client


 
   
class Standard(__api_client):
    def __init__(self, api_key:str, secret_key:str,proxies: dict= None,timeout: int =None, demo:bool=False, **kwargs):
        base_url=kwargs.get("base_url")
        if not base_url:
            from ..utils.urls import STANDARD
            kwargs["base_url"] = STANDARD.REST_DEMO if demo else STANDARD.REST
        
        kwargs["api_key"] = api_key
        kwargs["secret_key"] = secret_key
        kwargs["timeout"] = timeout
        kwargs["proxies"] = proxies
        super().__init__(**kwargs)
        
       
        self._interface = None
    
    @property
    def interface(self):
        if self._interface is None:
            from ._interface import Interface
            self._interface = Interface(self)
        
        return  self._interface

__all__ = ["Standard"]