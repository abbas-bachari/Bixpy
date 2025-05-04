from ..utils.api_client import ApiClient as __api
from ..utils.urls import URL as __URL__

class Spot(__api):
    """kwargs:
        - base_url='https://api.bingx.com'"""
    def __init__(self, api_key:str=None, api_secret:str=None,proxies: dict= None,timeout: int =None, demo:bool=False, **kwargs):
        base_url=kwargs.get("base_url")
        if not base_url:

            kwargs["base_url"] = __URL__.SPOT_BASE_DEMO if demo else __URL__.SPOT_BASE
        
        kwargs["api_key"] = api_key
        kwargs["api_secret"] = api_secret
        kwargs["timeout"] = timeout
        kwargs["proxies"] = proxies
        super().__init__(**kwargs)
        
        
    from ._market import (
        server_time,
        order_book_aggregation,
        order_book,
        recent_trades,
        historical_klines,
        klines,
        old_trade_lookup,
        order_book_ticker,
        symbols,
        ticker_24hr,
        price_ticker

    )
    from ._trade import (
        new_order,
        order_details,
        place_multiple_orders,
        cancel_order,
        cancel_open_orders,
        transaction_details,
        cancel_and_replace,
        get_open_orders,
        get_order_history,
        cancel_multiple_orders,
        cancel_all_orders_after_time,
        get_commission_rates,
        new_oco_order,
        cancel_oco_order,
        get_oco_order_list,
        get_oco_order_history,
        get_oco_open_orders
    )
        
    
         