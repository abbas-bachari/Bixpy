
from ..utils.api_client import ApiClient as __api
from ..utils.urls import URL as __URL__

class Perpetual(__api):
    def __init__(self, api_key:str=None, api_secret:str=None,proxies: dict= None,timeout: int =None, demo:bool=False, **kwargs):
        base_url=kwargs.get("base_url")
        if not base_url:
            kwargs["base_url"] = __URL__.PERPETUAL_BASE_DEMO if demo else __URL__.PERPETUAL_BASE
        
        kwargs["api_key"] = api_key
        kwargs["api_secret"] = api_secret
        kwargs["timeout"] = timeout
        kwargs["proxies"] = proxies
        super().__init__(**kwargs)
    
    from ._account import (
            balance,
            commission_rate,
            income,
            income_export,
            listen_key_delete,
            listen_key_new,
            listen_key_renew,
            positions,
        )
    from ._market import (
            get_server_time,
            get_symbols,
            get_order_book,
            get_recent_trades,
            price_and_funding_rate,
            get_funding_rate,
            get_klines,
            get_open_interest_Statistics,
            get_24hr_price_change,
            historical_transaction_orders,
            symbol_order_book_ticker,
            get_mark_price_klines,
            symbol_price_ticker
)
    from ._trade import (
            place_test_order,
            place_order,
            place_multiple_orders,
            close_all_positions,
            cancel_order,
            cancel_multiple_orders,
            cancel_all_open_orders,
            get_all_open_orders,
            get_pending_order_status,
            get_order_details,
            get_margin_type,
            set_margin_type,
            get_leverage,
            set_leverage,
            get_force_orders,
            get_order_history,
            modify_isolated_position_margin,
            get_historical_orders,
            set_position_mode,
            get_position_mode,
            cancel_and_replace_order,
            cancel_and_replace_batches_orders,
            cancel_all_after,
            close_position_by_position_id,
            get_all_orders,
            get_margin_ratio,
            get_historical_transaction_details,
            get_position_history,
            get_isolated_margin_change_history,
            get_vst,
            place_twap_order,
            get_twap_entrusted_order,
            get_twap_historical_orders,
            get_twap_order_details,
            cancel_twap_order,
            switch_multi_assets_mode,
            get_multi_assets_mode,
            get_multi_assets_rules,
            get_multi_assets_margin,
            one_click_reverse_position,
            automatic_margin_addition,
        )
