
from ..utils.api_client import ApiClient as __api_client




class Account(__api_client):   
    """kwargs:
        - base_url='https://api.bingx.com'"""
    def __init__(self, api_key: str, secret_key: str, proxies: dict = None, timeout: int = None, demo: bool = False, **kwargs):
        if not api_key or not secret_key:
            raise ValueError("API key and secret must be provided.")

        base_url = kwargs.get("base_url")
        if not base_url:
            from ..utils.urls import SPOT
            kwargs["base_url"] = SPOT.REST_DEMO if demo else SPOT.REST

        kwargs["api_key"] = api_key
        kwargs["secret_key"] = secret_key
        kwargs["timeout"] = timeout
        kwargs["proxies"] = proxies
        super().__init__(**kwargs)

        self._fund = None
        self._agent = None
        self._sub_account = None
        self._wallet = None
        self._listen_key = None
    
    

    def server_time(self):
        """Check Server Time
        Test connectivity to the Rest API and get the current server time.
        GET /openApi/spot/v1/server/time
        """
        return self.send_request('GET','/openApi/spot/v1/server/time')
    @property
    def listen_key(self):
        if self._listen_key is None:
            from ._listen_key import ListenKey
            self._listen_key = ListenKey(self)
        
        return self._listen_key
    
    @property
    def fund(self):
        if self._fund is None:
            from ._fund import FundAccount
            self._fund = FundAccount(self)
        
        return self._fund
    
    @property
    def agent(self):
        if self._agent is None:
            from ._agant import Agent
            self._agent = Agent(self)
        
        return self._agent
    
    @property
    def wallet(self):
        if self._wallet is None:
            from ._wallet import Wallet
            self._wallet = Wallet(self)
        
        return self._wallet
   
    
    @property
    def sub_account(self):
        if self._sub_account is None:
            from ._sub_account import SubAccount
            self._sub_account = SubAccount(self)
        
        return self._sub_account


__all__ = ["Account"]