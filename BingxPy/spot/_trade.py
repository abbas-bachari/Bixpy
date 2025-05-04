from ..utils._endpoints  import SpotTradesEndpoints as EP
from ..utils.objects import SpotOrder



def new_order( self,order: SpotOrder,recv_window: int = None):
    

    ep = EP.place_order

    params=order.to_dict()
    params["recvWindow"] = recv_window

    return self.send_request(ep.method, ep.path, params)

def order_details(self, symbol: str, order_id: int = None, client_order_id: str = None, recv_window: int = None):
    """Get the details of a specific order.

    Args:
        symbol (str): The symbol for which to retrieve the order details.
        order_id (int, optional): The order ID to retrieve.
        client_order_id (str, optional): The client order ID to retrieve.
        recv_window (int, optional): The receive window for the request.

    Returns:
        dict: The server's response to the request.
    """
    ep = EP.get_order

    params = {
        "symbol": symbol,
        "orderId": order_id,
        "clientOrderId": client_order_id,
        "recvWindow":recv_window
    }

    return self.send_request(ep.method, ep.path, params)

def place_multiple_orders(self, orders: list[SpotOrder],sync:bool=None, recv_window: int = None):
    "The request array for placing orders, limited to 5 orders."
    ep=EP.place_multiple_orders
    params = {
        "data": str( [ order.to_json() for order in orders ]),
        "sync": sync,
        "recvWindow":recv_window
    }
    

    
    
    return self.send_request(ep.method, ep.path, params)
def cancel_order(self, symbol: str = None, order_id: int = None, client_order_id: str = None, cancel_restrictions: str = None, recv_window: int = None):
    ep = EP.cancel_order

    payload = {
        "symbol": symbol,
        "orderId": order_id,
        "clientOrderID": client_order_id,
        "cancelRestrictions": cancel_restrictions,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, payload)

def cancel_open_orders(self, symbol: str=None, recv_window: int = None):
    
    """
    Cancel all open orders for the given symbol.

    Args:
        symbol (str, optional): The symbol for which to cancel all open orders. 
                                If not provided, all open orders are cancelled.
        "recvWindow":recv_window: Additional parameters for the request.

    Returns:
        dict: The server's response to the request.
    """
    ep=EP.cancel_all_open_orders
    

    
    payload = {"symbol": symbol, "recvWindow":recv_window}
    return self.send_request(ep.method, ep.path, payload)

def cancel_and_replace(self, symbol: str,cancel_replace_mode: str,side: str, type: str, stop_price: float,  price: float=None,quote_order_qty: float=None,quantity: float=None,  cancel_order_id: int=None, cancel_client_order_id: str=None, cancel_restrictions: str=None,   new_client_order_id: str=None, recv_window: int = None):
    """
    Cancel an active order and place a new order.

    Args:
        symbol (str): The symbol for which to cancel and replace an order.
        cancel_replace_mode (str): The mode for canceling and replacing an order.
        side (str): The side on which to place the new order.
        type (str): The type of the new order.
        stop_price (float): The stop price for the new order.
        price (float, optional): The price for the new order.
        quote_order_qty (float, optional): The quote order quantity for the new order.
        quantity (float, optional): The quantity for the new order.
        cancel_order_id (int, optional): The order ID of the order to cancel.
        cancel_client_order_id (str, optional): The client order ID of the order to cancel.
        cancel_restrictions (str, optional): The restrictions for canceling the order.
        new_client_order_id (str, optional): The client order ID for the new order.
        recv_window (int, optional): The receive window for the request.

   
    """
    ep = EP.cancel_replace_order

    payload = {
        "symbol": symbol,
        "cancelOrderId": cancel_order_id,
        "cancelClientOrderID": cancel_client_order_id,
        "cancelRestrictions": cancel_restrictions,
        "cancelReplaceMode": cancel_replace_mode,
        "side": side,
        "type": type,
        "stopPrice": stop_price,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id,
        "recvWindow":recv_window,
    }

    return self.send_request(ep.method, ep.path, payload)

def cancel_multiple_orders(self, symbol: str, order_ids: list, process: int = None , client_order_ids: list = None, recv_window: int = None):
    
    
    
    """
    Cancel multiple orders.

    Args:
        symbol (str): The symbol for which to cancel multiple orders.
        order_ids (list): List of order IDs to cancel.
        process (int, optional): Whether to handle valid order IDs partially. Defaults to 0.
            - 0: If one of the order IDs is invalid, all will fail.
            - 1: Will handle valid order IDs partially, and return invalid order IDs in the `fails` list.
        client_order_ids (list, optional): List of client order IDs to cancel.
        recv_window (int, optional): The receive window for the request.

    Returns:
        dict: The server's response to the request.
    """
    endpoint = EP.cancel_multiple_orders

    params = {
        "symbol": symbol,
        "process": process,
        "orderIds": ','.join(order_ids) if isinstance(order_ids, list) else order_ids,
        "clientOrderIDs":','.join(client_order_ids) if isinstance(client_order_ids, list) else client_order_ids,
        "recvWindow":recv_window
    }
    
    return self.send_request(endpoint.method, endpoint.path, params)

def cancel_all_orders_after_time(self,type:str, timeOut:int,  recv_window: int = None):
    
    """
    Cancel all open orders after a specified time.

    Args:
        type (str): Request type: ACTIVATE-Activate, CLOSE-Close.
        timeOut (int): Activate countdown time (seconds), range: 10s-120s.
        recv_window (int, optional): The receive window for the request.

    Returns:
        dict: The server's response to the request.
    """
    ep=EP.cancel_all_after_time

    

    params = {
            "type": type,
            "timeOut": timeOut,
            "recvWindow":recv_window
            }
    
    return self.send_request(ep.method, ep.path, params)

def transaction_details(self, symbol: str, order_id: int=None, start_time: int=None, end_time: int=None, from_id: int=None, limit: int=None, recv_window: int = None):
    endpoint = EP.transaction_details

    params = {
        "symbol": symbol,
        "orderId": order_id,
        "startTime": start_time,
        "endTime": end_time,
        "fromId": from_id,
        "limit": limit,
        "recvWindow":recv_window
    }
    return self.send_request(endpoint.method, endpoint.path, params)


def get_open_orders(self, symbol: str = None, recv_window: int = None):
    """
    Retrieve open orders for a specific symbol or all symbols.

    Args:
        symbol (str, optional): The trading symbol. Defaults to None.
        "recvWindow":recv_window: Additional parameters for the request.

    Returns:
        dict: The server's response to the request.
    """
    endpoint = EP.get_open_orders
    params = {"symbol": symbol, "recvWindow":recv_window}
    return self.send_request(endpoint.method, endpoint.path, params)

def get_order_history(self, symbol: str=None,order_id: int=None, start_time: int=None, end_time: int=None, page_index: int=None, page_size: int=None, status: str=None, type: str=None, recv_window: int = None):
    ep=EP.get_order_history
    
    payload = {
        "symbol": symbol,
        "orderId": order_id,
        "startTime": start_time,
        "endTime": end_time,
        "pageIndex": page_index,
        "pageSize": page_size,
        "status": status,
        "type": type,
         
          "recvWindow":recv_window}
    return self.send_request(ep.method, ep.path, payload)

def get_commission_rates(self, symbol: str, recv_window: int = None):
    """Get the commission rates for the given symbol.

    Args:
        symbol (str): The symbol for which to retrieve the commission rates.
        recv_window (int, optional): The receive window for the request.

    Returns:
        dict: The server's response to the request.
    """
    ep = EP.get_user_commission_rate

    params = {"symbol": symbol, "recvWindow":recv_window}
    
    return self.send_request(ep.method, ep.path, params)

def new_oco_order(self, symbol: str, side: str, quantity: float, limit_price: float, order_price: float, trigger_price: float, list_client_order_id: str = None, above_client_order_id: str = None, below_client_order_id: str = None, recv_window: int = None):
    """
    Place a new OCO (One Cancels the Other) order.

    Args:
        symbol (str): The symbol for which to place the OCO order.
        side (str): The side of the OCO order.
        quantity (float): The quantity for the OCO order.
        limit_price (float): The limit price for the OCO order.
        order_price (float): The order price for the OCO order.
        trigger_price (float): The trigger price for the OCO order.
        list_client_order_id (str, optional): The client order ID for the OCO order.
        above_client_order_id (str, optional): The above client order ID for the OCO order.
        below_client_order_id (str, optional): The below client order ID for the OCO order.
        recv_window (int, optional): The receive window for the request.

    Returns:
        dict: The server's response to the request.
    """
    endpoint = EP.place_oco_order

    params = {
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "limitPrice": limit_price,
        "orderPrice": order_price,
        "triggerPrice": trigger_price,
        "listClientOrderId": list_client_order_id,
        "aboveClientOrderId": above_client_order_id,
        "belowClientOrderId": below_client_order_id,
        "recvWindow":recv_window,
    }

    return self.send_request(endpoint.method, endpoint.path, params)

def cancel_oco_order(self, order_id: str = None, client_order_id: str = None, recv_window: int = None):
    """
    Cancel an OCO order.

    Args:
        order_id (str): The order ID of the OCO order to cancel.
        client_order_id (str): The client order ID of the OCO order to cancel.
        recv_window (int, optional): The receive window for the request.

    Returns:
        dict: The server's response to the request.
    """
    endpoint = EP.cancel_oco_order

    payload = {
        "orderId": order_id,
        "clientOrderId": client_order_id,
        "recvWindow":recv_window,
    }

    return self.send_request(endpoint.method, endpoint.path, payload)

def get_oco_order_list(self, order_list_id: str = None, client_order_id: str = None, recv_window: int = None):
    """Get an OCO order.

    Args:
        order_list_id (str, optional): The ID of the OCO order list.
        client_order_id (str, optional): The client order ID of the OCO order.
        recv_window (int, optional): The receive window for the request.

    Returns:
        dict: The server's response to the request.
    """
    ep = EP.get_oco_order_list

    payload = {
        "orderListId": order_list_id,
        "clientOrderId": client_order_id,
        "recvWindow":recv_window,
    }

    return self.send_request(ep.method, ep.path, payload)

def get_oco_order_history(self, page_index: int = 1, page_size: int = 100, start_time: int = None, end_time: int = None, recv_window: int = None):
    """Get OCO order history.

    Args:
        page_index (int, optional): The page index to retrieve.
        page_size (int, optional): The page size of the result.
        start_time (int, optional): The start time of the query.
        end_time (int, optional): The end time of the query.
        recv_window (int, optional): The receive window for the request.

    Returns:
        dict: The server's response to the request.
    """
    ep = EP.get_oco_order_history

    payload = {
        "pageIndex": page_index,
        "pageSize": page_size,
        "startTime": start_time,
        "endTime": end_time,
        "recvWindow":recv_window
    }

    return self.send_request(ep.method, ep.path, payload)

def get_oco_open_orders(self, page_index: int = 1, page_size: int = 100, recv_window: int = None):
    """Get open OCO orders.

    Args:
        page_index (int, optional): The page index to retrieve.
        page_size (int, optional): The page size of the result.
        recv_window (int, optional): The receive window for the request.

    Returns:
        dict: The server's response to the request.
    """
    ep = EP.get_oco_open_order_list

    payload = {
        "pageIndex": page_index,
        "pageSize": page_size,
        "recvWindow":recv_window,
    }

    return self.send_request(ep.method, ep.path, payload)






