

from ..utils._endpoints import PerpetualTradeEndpoints as EP
from ..utils.objects import PerpetualOrder, PerpetualOrderReplace
from time import time






def place_test_order(self,order: PerpetualOrder, recv_window: int = None):
    
    
    """
    Place a test order on the trading platform.

    Args:
        order (PerpetualOrder): An instance of PerpetualOrder containing order details.
        recv_window (int, optional): The receive window for the request.

    Returns:
        dict: The server's response to the test order request.
    """

    ep = EP.test_order
    params = order.to_dict()
    
    params["recvWindow"] = recv_window
    
    return self.send_request(ep.method, ep.path, params)








def place_order(self, order: PerpetualOrder, recv_window: int = None):

    
    
    ep = EP.place_order
    params = order.to_dict()
    params["recvWindow"] = recv_window
    
    return self.send_request(ep.method, ep.path, params)


def place_multiple_orders(self, orders: list[PerpetualOrder], recv_window: int = None):
    
    ep = EP.place_multiple_orders
    params = {
        "batchOrders": str( [ order.to_json() for order in orders ]),
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def close_all_positions(self,symbol=None, recv_window: int = None):
    ep = EP.close_all_positions
    params = {
        "symbol": symbol,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def cancel_order(self,symbol:str,order_id:int=None, recv_window: int = None):
    ep = EP.cancel_order
    params = {
        "symbol": symbol,
        "orderId": order_id,
        
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def cancel_multiple_orders(self,symbol:str,order_id_list:list[int]=None,client_order_id_list:list[str]=None, recv_window: int = None):
    ep = EP.cancel_multiple_orders
    params = {
        "symbol": symbol,
        "orderIdList": order_id_list,
        "clientOrderIdList": client_order_id_list,
  
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def cancel_all_open_orders(self,symbol:str=None,order_type:str=None, recv_window: int = None):
    
    """
    Cancel all open orders for a given symbol and order type.

    Args:
        symbol (str, optional): The symbol for which to cancel all open orders. 
                                If not provided, all open orders are cancelled.
        order_type (str, optional): The type of order to cancel.
                                    Options include 'LIMIT', 'MARKET', 'STOP_MARKET', 
                                    'TAKE_PROFIT_MARKET', 'STOP', 'TAKE_PROFIT', 
                                    'TRIGGER_LIMIT', 'TRIGGER_MARKET', 'TRAILING_STOP_MARKET', 
                                    'TRAILING_TP_SL'.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    
    """
    ep = EP.cancel_all_open_orders
    params = {
        "symbol": symbol,
        "orderType": order_type,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_all_open_orders(self,symbol:str=None,order_type:str=None, recv_window: int = None):
    
    """
    Get all open orders for a given symbol and order type.

    Args:
        symbol (str, optional): The symbol for which to cancel all open orders. 
                                If not provided, all open orders are cancelled.
        order_type (str, optional): The type of order to cancel.
                                    Options include 'LIMIT', 'MARKET', 'STOP_MARKET', 
                                    'TAKE_PROFIT_MARKET', 'STOP', 'TAKE_PROFIT', 
                                    'TRIGGER_LIMIT', 'TRIGGER_MARKET', 'TRAILING_STOP_MARKET', 
                                    'TRAILING_TP_SL'.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    """
    ep = EP.get_all_open_orders
    params = {
        "symbol": symbol,
        "orderType": order_type,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_pending_order_status(self,symbol:str,order_id:int=None,client_order_id:str=None, recv_window: int = None):
    ep = EP.get_pending_order_status
    params = {
        "symbol": symbol,
        "orderId": order_id,
        "clientOrderId": client_order_id,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_order_details(self,symbol:str,order_id:int=None,client_order_id:str=None, recv_window: int = None):
    ep = EP.get_order_details
    params = {
       
        "symbol": symbol,
        "orderId": order_id,
        "clientOrderId": client_order_id,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_margin_type(self,symbol:str, recv_window: int = None):
    ep = EP.get_margin_type
    params = {
        "symbol": symbol,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def set_margin_type(self,symbol:str,margin_type:str, recv_window: int = None):
    
    """
    Set margin type for a symbol.

    Args:
        symbol (str): The symbol to set margin type for.
        margin_type (str): The type of margin to set. Options include "ISOLATED", "CROSSED", "SEPARATE_ISOLATED".
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        dict: The server's response to the request.

    """
    
    ep = EP.set_margin_type
    params = {
        "symbol": symbol,
        "marginType": margin_type,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_leverage(self,symbol:str, recv_window: int = None):
    ep = EP.get_leverage
    params = {
        "symbol": symbol,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def set_leverage(self,symbol:str,side:str,leverage:int, recv_window: int = None):
    #Leverage for long or short positions. In the Hedge mode, LONG for long positions, SHORT for short positions. In the One-way mode, only supports BOTH.
    """
    Set the leverage for a given symbol.

    Args:
        symbol (str): The symbol to set the leverage for.
        side (str): The side to set the leverage for. Options include "LONG", "SHORT".
        leverage (int): The leverage to set.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        dict: The server's response to the request.

    """
    ep = EP.set_leverage
    params = {
        "symbol": symbol,
        "side": side,
        "leverage": leverage,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_force_orders(self, symbol: str = None, currency: str = None, auto_close_type: str = None,
                     start_time: int = None, end_time: int = None, limit: int = None, recv_window: int = None):
    """
    Get force liquidation orders.

    Args:
        symbol (str, optional): The symbol for which to get force liquidation orders. Defaults to None.
        currency (str, optional): The currency for which to get force liquidation orders. Defaults to None.
        auto_close_type (str, optional): The type of auto close orders. Options include "LIQUIDATION", "ADL". Defaults to None.
        start_time (int, optional): The start time for which to get force liquidation orders. Defaults to None.
        end_time (int, optional): The end time for which to get force liquidation orders. Defaults to None.
        limit (int, optional): The number of force liquidation orders to return. Defaults to None.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        dict: The server's response to the request.

    """
    ep = EP.force_orders
    params = {
        "symbol": symbol,
        "currency": currency,
        "autoCloseType": auto_close_type,
        "startTime": start_time,
        "endTime": end_time,
        "limit": limit,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_order_history(self, limit: int, symbol: str = None, currency: str = None, order_id: int = None, start_time: int = None, end_time: int = None, recv_window: int = None):
    ep = EP.get_order_history

    # Validate the input parameters
    

    params = {
        "limit": limit,
        "symbol": symbol,
        "currency": currency,
        "orderId": order_id,
        "startTime": start_time,
        "endTime": end_time,
        "recvWindow":recv_window
    }

    try:
        return self.send_request(ep.method, ep.path, params)
    except Exception as e:
        raise RuntimeError(f"Failed to get order history: {e}")

def modify_isolated_position_margin(self,symbol:str,amount:str,position_type:int,position_side:str=None,position_id:int=None, recv_window: int = None):
    ep = EP.modify_isolated_position_margin
    params = {
        "symbol": symbol,
        "amount": amount,
        "type": position_type,
        "positionSide": position_side,
        "positionId": position_id,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_historical_orders(self,trading_unit: str,start_ts: int,end_ts: int,order_id: int = None,currency: str = None,symbol: str = None,recv_window: int = None) -> str:
    """Get historical orders
    Parameters:
    trading_unit (str): Trading unit, optional values: COIN,CONT; COIN directly represent assets such as BTC and ETH, and CONT represents the number of contract sheets
    start_ts (int): Starting timestamp in milliseconds
    end_ts (int): Starting timestamp in milliseconds
    order_id (int): If orderId is provided, only the filled orders of that orderId are returned
    currency (str): USDC or USDT
    
    """
    ep = EP.get_order_history 
    params = {
        "orderId": order_id,
        "symbol": symbol,
        "currency": currency,
        "tradingUnit": trading_unit,
        "startTs": start_ts,
        "endTs": end_ts,
        
        "recvWindow":recv_window,
    }
    return self.send_request(ep.method, ep.path, params)

def set_position_mode(self,dual_side_position: bool , recv_window: int = None):
    #"true": dual position mode; "false": single position mode
    """
    Set the position mode for trading.

    Args:
        dual_side_position (bool): Determines the position mode. 
                                   Use `True` for dual position mode and `False` for single position mode.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    
    """

    ep = EP.set_position_mode
    params = {
        "dualSidePosition": "true" if dual_side_position else "false" ,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_position_mode(self, recv_window: int = None):
    ep = EP.get_position_mode
    params = {
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def cancel_and_replace_order(self,order:PerpetualOrderReplace , recv_window: int = None):
    
    ep = EP.cancel_and_replace_order
    

    
    params = order.to_dict()
    
    params["recvWindow"] = recv_window

    return self.send_request(ep.method, ep.path, params)

def cancel_and_replace_batches_orders(self,orders:list[PerpetualOrderReplace] , recv_window: int = None):
    ep = EP.cancel_and_replace_batches_orders
    params = {
        'batchOrders': str( [ order.to_json() for order in orders ]),
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def cancel_all_after(self, request_type: str, time_out: int, recv_window: int = None) -> str:
    """Cancel all open orders after a specified time.

    Args:
        request_type (str): The type of request. Options include 'ACTIVATE' and 'CLOSE'.
        time_out (int): The countdown time in seconds. Range: 10s-120s.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        str: The server's response to the request.
    """
    ep = EP.cancel_all_after
    params = {
        "type": request_type,
        "timeOut": time_out,
        "recvWindow":recv_window,
    }
    return self.send_request(ep.method, ep.path, params)

def close_position_by_position_id(self,position_id:int, recv_window: int = None):
    ep = EP.close_position_by_position_id
    params = {
        "positionId": position_id,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_all_orders(self, limit: int ,symbol: str = None, order_id: int = None, start_time: int = None, end_time: int = None,  recv_window: int = None) -> str:
    """Get all open orders.

    Args:
        symbol (str, optional): The symbol for which to get all open orders. If not provided, all open orders are returned.
        order_id (int, optional): The id of the order to retrieve. If not provided, all open orders are returned.
        start_time (int, optional): The start time in milliseconds. If not provided, all open orders are returned.
        end_time (int, optional): The end time in milliseconds. If not provided, all open orders are returned.
        limit (int, required): The maximum number of orders to return. If not provided, all open orders are returned.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        str: The server's response to the request.
    """
    ep = EP.get_all_orders
    params = {
        "symbol": symbol,
        "orderId": order_id,
        "startTime": start_time,
        "endTime": end_time,
        "limit": limit,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_margin_ratio(self,symbol:str, recv_window: int = None):
    ep = EP.position_and_maintenance_margin_ratio
    params = {
        "symbol":symbol,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_historical_transaction_details(self,symbol:str,start_ts:int,end_ts:int,currency:str=None,order_id:int=None,last_fill_id:int=None,page_index:int=None,page_size:int=None, recv_window: int = None):
    ep = EP.get_historical_transaction_details
    params = {
        "symbol": symbol,
        "currency": currency,
        "orderId": order_id,
        "lastFillId": last_fill_id,
        "startTs": start_ts,
        "endTs": end_ts,
        "pageIndex": page_index,
        "pageSize": page_size,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_position_history(self, symbol: str, start_ts: int, end_ts: int, currency: str = None, position_id: int = None, page_index: int = None, page_size: int = None, recv_window: int = None) -> str:
    """Get the position history.

    Args:
        symbol (str): The symbol to get the position history for.
        start_ts (int): The start timestamp for the position history.
        end_ts (int): The end timestamp for the position history.
        currency (str, optional): The currency for the position history. Defaults to None.
        position_id (int, optional): The position ID for the position history. Defaults to None.
        page_index (int, optional): The page index for pagination. Defaults to None.
        page_size (int, optional): The page size for pagination. Defaults to None.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        str: The server's response to the request.
    """
    ep = EP.get_position_history
    params = {
        "symbol": symbol,
        "currency": currency,
        "positionId": position_id,
        "startTs": start_ts,
        "endTs": end_ts,
        "pageIndex": page_index,
        "pageSize": page_size,
        "recvWindow":recv_window,
    }
    return self.send_request(ep.method, ep.path, params)

def get_isolated_margin_change_history(self, symbol: str, position_id: str, start_time: int, end_time: int, page_index: int, page_size: int, recv_window: int = None) -> str:
    """Get the isolated margin change history.

    Args:
        symbol (str): The symbol to get the isolated margin change history for.
        position_id (str): The position ID for the isolated margin change history.
        start_time (int): The start timestamp for the isolated margin change history.
        end_time (int): The end timestamp for the isolated margin change history.
        page_index (int): The page index for pagination.
        page_size (int): The page size for pagination.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        str: The server's response to the request.
    """
    ep = EP.get_isolated_margin_change_history
    params = {
        "symbol": symbol,
        "positionId": position_id,
        "startTime": start_time,
        "endTime": end_time,
        "pageIndex": page_index,
        "pageSize": page_size,
        "recvWindow":recv_window,
    }
    return self.send_request(ep.method, ep.path, params)

def get_vst(self, recv_window: int = None):
    ep = EP.get_vst
    params = {
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def place_twap_order(self, symbol: str, side: str, position_side: str, price_type: str, price_variance: str, trigger_price: str, interval: int, amount_per_order: str, total_amount: str, recv_window: int = None) -> str:
    """Create a Time Weighted Order (TWAP) order. This function will help you execute large orders in batches within 24 hours, thereby reducing the impact of large orders on market prices, making the average transaction price closer to the actual market price, and reducing your transaction costs.

    Args:
        symbol (str): The symbol to place the order for.
        side (str): The side of the order (BUY or SELL).
        position_side (str): The position side of the order (LONG or SHORT).
        price_type (str): The price type of the order (LIMIT or MARKET).
        price_variance (str): The price variance of the order.
        trigger_price (str): The trigger price of the order.
        interval (int): The interval of the order.
        amount_per_order (str): The amount per order of the order.
        total_amount (str): The total amount of the order.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        str: The server's response to the request.
    """
    


    ep = EP.place_twap_order
    params = {
        "symbol": symbol,
        "side": side,
        "positionSide": position_side,
        "priceType": price_type,
        "priceVariance": price_variance,
        "triggerPrice": trigger_price,
        "interval": interval,
        "amountPerOrder": amount_per_order,
        "totalAmount": total_amount,
        "recvWindow":recv_window,
    }
    return self.send_request(ep.method, ep.path, params)

def get_twap_entrusted_order(self,symbol: str=None, recv_window: int = None):
    ep = EP.get_twap_entrusted_order
    params = {
        "symbol": symbol,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_twap_historical_orders(self, symbol: str = None, page_index: int = 1, page_size: int = 100, start_time: int = int(time() * 1000) - (24 * 60 * 60 * 1000), end_time: int = int(time() * 1000), recv_window: int = None) -> str:
    
    """
    Get historical TWAP orders.

    Args:
        symbol (str, optional): The symbol to get the historical TWAP orders for. Defaults to None.
        page_index (int, optional): The page index for pagination. Defaults to 1.
        page_size (int, optional): The page size for pagination. Defaults to 100.
        start_time (int, optional): The start timestamp for the historical TWAP orders. Defaults to 24 hours ago.
        end_time (int, optional): The end timestamp for the historical TWAP orders. Defaults to current time.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        str: The server's response to the request.
    """
    ep = EP.get_twap_historical_orders
    params = {
        "symbol": symbol,
        "pageIndex": page_index,
        "pageSize": page_size,
        "startTime": start_time,
        "endTime": end_time,
        "recvWindow":recv_window,
    }
    return self.send_request(ep.method, ep.path, params)

def get_twap_order_details(self, main_order_id: str, recv_window: int = None) -> str:
    """Get TWAP order details.

    Args:
        main_order_id (str): The main order ID of the TWAP order.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        str: The server's response to the request.
    """
    ep = EP.get_twap_order_details
    params = {
        "mainOrderId": main_order_id,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def cancel_twap_order(self,main_order_id: str, recv_window: int = None):
    ep = EP.cancel_twap_order
    params = {
        "mainOrderId": main_order_id,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def switch_multi_assets_mode(self, asset_mode: str, recv_window: int = None):
    """
    Switch between single and multi-assets mode.

    Args:
        asset_mode (str): The asset mode to switch to. Use 'singleAssetMode' or 'multiAssetsMode'.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        str: The server's response to the request.
    """
    endpoint = EP.switch_multi_assets_mode
    params = {
        "assetMode": asset_mode,
        "recvWindow":recv_window
    }
    return self.send_request(endpoint.method, endpoint.path, params)

def get_multi_assets_mode(self, recv_window: int = None):
    ep = EP.get_multi_assets_mode
    params = {

        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_multi_assets_rules(self, recv_window: int = None):
    ep = EP.get_multi_assets_rules
    params = {
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def get_multi_assets_margin(self, recv_window: int = None):
    ep = EP.get_multi_assets_margin
    params = {
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)

def one_click_reverse_position(self, symbol: str, reverse_method: str = 'Reverse', trigger_price: float = None, price_type: str = 'MARK_PRICE', recv_window: int = None):
    """
    Reverse a position with a single click.

    Args:
        symbol (str): The symbol of the position to reverse.
        reverse_method (str): The method of reversal ('Reverse' for immediate, 'TriggerReverse' for planned).
        trigger_price (float): The trigger price, required for planned reversal.
        price_type (str): The type of trigger price ('MARK_PRICE', 'CONTRACT_PRICE', 'INDEX_PRICE').
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        str: The server's response to the request.
    """

    endpoint = EP.one_click_reverse_position
    params = {
        'type': reverse_method,
        'symbol': symbol,
        'triggerPrice': trigger_price,
        'workingType': price_type,
        "recvWindow":recv_window
    }
    return self.send_request(endpoint.method, endpoint.path, params)

def automatic_margin_addition(self, symbol: str, position_id: int, function_switch: bool, amount: str=None, recv_window: int = None):
    """
    Automatically add margin to a position.

    Args:
        symbol (str): The trading symbol.
        position_id (int): The ID of the position to add margin to.
        function_switch (str): Whether to enable the automatic margin addition feature, true: enable, false: disable
        amount (str): Amount of margin to be added, in USDT. Must be specified when enabling the feature.
        "recvWindow":recv_window: Additional keyword arguments for the request.

    Returns:
        str: The server's response to the request.
    """
    endpoint = EP.automatic_margin_addition
    params = {
        "symbol": symbol,
        "positionId": position_id,
        "functionSwitch": 'true' if function_switch else 'false' ,
        "amount": amount,
        "recvWindow":recv_window
    }
    return self.send_request(endpoint.method, endpoint.path, params)



    