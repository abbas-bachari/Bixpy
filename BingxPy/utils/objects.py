import json

class PerpetualOrder:
    """
    ### order_type : str
        - LIMIT: Limit Order 
        - MARKET: Market Order 
        - STOP_MARKET: Stop Market Order
        - TAKE_PROFIT_MARKET: Take Profit Market Order 
        - STOP: Stop Limit Order 
        - TAKE_PROFIT: Take Profit Limit Order 
        - TRIGGER_LIMIT: Stop Limit Order with Trigger 
        - TRIGGER_MARKET: Stop Market Order with Trigger 
        - TRAILING_STOP_MARKET: Trailing Stop Market Order 
        - TRAILING_TP_SL: Trailing TakeProfit or StopLoss
                
    ### side : str
        - Side of the order (BUY or SELL).
    ### position_side : str
        - Position direction, required for single position as BOTH, for both long and short positions only LONG or SHORT can be chosen, defaults to LONG if empty
        
    ### time_in_force : str, optional
        - Time in force of the order (GTC, IOC, FOK).
    ### working_type : str, optional
        - StopPrice trigger price types: MARK_PRICE, INDEX_PRICE or CONTRACT_PRICE default MARK_PRICE.
        - When the type is STOP or STOP_MARKET, and stopGuaranteed is true, the workingType must only be CONTRACT_PRICE.
    
    """
    def __init__(self, symbol: str, order_type: str, side: str, position_side: str=None, reduce_only: str=None,
                 price: float=None, quantity: float=None, stop_price: float=None, price_rate: float=None, stop_loss: str=None,
                 take_profit: str=None, working_type: str=None,  client_order_id: str=None,
                  time_in_force: str=None, close_position: bool=None,
                 activation_price: float=None, stop_guaranteed:bool=None):
        
        
        
        self.symbol = symbol
        self.type = order_type
        self.side = side
        self.positionSide = position_side
        self.reduceOnly = reduce_only
        self.price = price
        self.quantity = quantity
        self.stopPrice = stop_price
        self.priceRate = price_rate
        self.stopLoss = stop_loss
        self.takeProfit = take_profit
        self.workingType = working_type
        self.clientOrderId = client_order_id
        self.timeInForce = time_in_force
        self.closePosition = close_position
        self.activationPrice = activation_price
        self.stopGuaranteed = stop_guaranteed
        
    def to_dict(self, clean_none=True)->dict:
        """
        Convert the order object to a dictionary.

        Args:
            clean_none (bool): If True, remove keys with None values.

        Returns:
            dict: The order dictionary.
        """
        order_dict = {
            "symbol": self.symbol,
            "type": self.type,
            "side": self.side,
            "positionSide": self.positionSide,
            "reduceOnly":"true" if self.reduceOnly is True else 'false' if self.reduceOnly is False else None ,
            "price": self.price,
            "quantity": self.quantity,
            "stopPrice": self.stopPrice,
            "priceRate": self.priceRate,
            "stopLoss": self.stopLoss,
            "takeProfit": self.takeProfit,
            "workingType": self.workingType,
            "clientOrderId": self.clientOrderId,
            "timeInForce": self.timeInForce,
            "closePosition":"true" if self.closePosition is True else 'false' if self.closePosition is False else None ,
            "activationPrice": self.activationPrice,
            "stopGuaranteed": "true" if self.stopGuaranteed is True else 'false' if self.stopGuaranteed is False else None
        }

        if clean_none:
            order_dict = {k: v for k, v in order_dict.items() if v is not None}

        return order_dict
    
    def to_json(self,clean_none=True)->str: 
        """
        Convert the order object to a JSON string.

        Args:
            clean_none (bool): If True, remove keys with None values.

        Returns:
            str: The order JSON string.
        """
        return json.dumps(self.to_dict(clean_none))
        

    def __str__(self):
        return self.to_json()


class PerpetualOrderReplace:
    """
    Cancel an active order and place a new order.

    
        ### cancel_replace_mode (str): The mode for canceling and replacing an order.
            - STOP_ON_FAILURE: If the order cancellation fails, the replacement order will not continue.
            - ALLOW_FAILURE: Regardless of the success of the order cancellation, the replacement order will proceed.
        ### cancel_client_order_id (str, optional): 
            - The original client-defined order ID to be canceled.
            - The system will convert this field to lowercase. Either `cancelClientOrderId` or `cancelOrderId` must be provided.
            - If both parameters are provided, `cancelOrderId` takes precedence.
        ### cancel_order_id (int, optional): The platform order ID to be canceled.
            - Either `cancelClientOrderId` or `cancelOrderId` must be provided. If both parameters are provided, `cancelOrderId` takes precedence.
        ### cancel_restrictions (str, optional): The restrictions for canceling the order.
            - ONLY_NEW: If the order status is NEW, the cancellation will succeed.
            - ONLY_PENDING: If the order status is PENDING, the cancellation will succeed.
            - ONLY_PARTIALLY_FILLED: If the order status is PARTIALLY_FILLED, the cancellation will succeed.
        ### order_type  (str):
            - LIMIT: Limit Order 
            - MARKET: Market Order 
            - STOP_MARKET: Stop Market Order
            - TAKE_PROFIT_MARKET: Take Profit Market Order 
            - STOP: Stop Limit Order 
            - TAKE_PROFIT: Take Profit Limit Order 
            - TRIGGER_LIMIT: Stop Limit Order with Trigger 
            - TRIGGER_MARKET: Stop Market Order with Trigger 
            - TRAILING_STOP_MARKET: Trailing Stop Market Order 
            - TRAILING_TP_SL: Trailing TakeProfit or StopLoss
                
        ### side : str
            - Side of the order (BUY or SELL).
        ### position_side : str
            - Position direction, required for single position as BOTH, for both long and short positions only LONG or SHORT can be chosen, defaults to LONG if empty
        
        ### time_in_force : str, optional
            - Time in force of the order (GTC, IOC, FOK).
        ### working_type : str, optional
            - StopPrice trigger price types: MARK_PRICE, INDEX_PRICE or CONTRACT_PRICE default MARK_PRICE.
            - When the type is STOP or STOP_MARKET, and stopGuaranteed is true, the workingType must only be CONTRACT_PRICE.

        ### Returns:
            dict: The server's response to the request.
    """
    def __init__(self,
                cancel_replace_mode: str , symbol: str,
                order_type: str, side: str,cancel_client_order_id: str =None,
                cancel_order_id: int=None ,cancel_restrictions: str=None, position_side: str=None, reduce_only: str=None,
                price: float=None, quantity: float=None, stop_price: float=None, price_rate: float=None, stop_loss: str=None,
                take_profit: str=None, working_type: str=None,  client_order_id: str=None,
                time_in_force: str=None, close_position: bool=None,
                activation_price: float=None, stop_guaranteed:bool=None):
        
        if cancel_client_order_id is None and cancel_order_id is None:
            raise ValueError("Either `cancelClientOrderId` or `cancelOrderId` must be provided.")
        self.symbol = symbol
        self.type = order_type
        self.side = side
        self.positionSide = position_side
        self.reduceOnly = reduce_only
        self.price = price
        self.quantity = quantity
        self.stopPrice = stop_price
        self.priceRate = price_rate
        self.stopLoss = stop_loss
        self.takeProfit = take_profit
        self.workingType = working_type
        self.clientOrderId = client_order_id
        self.timeInForce = time_in_force
        self.closePosition = close_position
        self.activationPrice = activation_price
        self.stopGuaranteed = stop_guaranteed
        self.cancelReplaceMode= cancel_replace_mode
        self.cancelClientOrderId= cancel_client_order_id
        self.cancelOrderId= cancel_order_id
        self.cancelRestrictions= cancel_restrictions
    def to_dict(self, clean_none=True)->dict:
        """
        Convert the order object to a dictionary.

        Args:
            clean_none (bool): If True, remove keys with None values.

        Returns:
            dict: The order dictionary.
        """
        order_dict = {
            "cancelReplaceMode": self.cancelReplaceMode,
            "cancelClientOrderId": self.cancelClientOrderId,
            "cancelOrderId": self.cancelOrderId,
            "cancelRestrictions": self.cancelRestrictions,
            "symbol": self.symbol,
            "type": self.type,
            "side": self.side,
            "positionSide": self.positionSide,
            "reduceOnly":"true" if self.reduceOnly is True else 'false' if self.reduceOnly is False else None ,
            "price": self.price,
            "quantity": self.quantity,
            "stopPrice": self.stopPrice,
            "priceRate": self.priceRate,
            "stopLoss": self.stopLoss,
            "takeProfit": self.takeProfit,
            "workingType": self.workingType,
            "clientOrderId": self.clientOrderId,
            "timeInForce": self.timeInForce,
            "closePosition":"true" if self.closePosition is True else 'false' if self.closePosition is False else None ,
            "activationPrice": self.activationPrice,
            "stopGuaranteed": "true" if self.stopGuaranteed is True else 'false' if self.stopGuaranteed is False else None
        }

        if clean_none:
            order_dict = {k: v for k, v in order_dict.items() if v is not None}

        return order_dict
    
    def to_json(self,clean_none=True)->str: 
        """
        Convert the order object to a JSON string.

        Args:
            clean_none (bool): If True, remove keys with None values.

        Returns:
            str: The order JSON string.
        """
        return json.dumps(self.to_dict(clean_none))
        

    def __str__(self):
        return self.to_json()

class SpotOrder:
    
    """
        Initialize a SpotOrder object.

        Args:
            symbol (str): The trading symbol (e.g., 'BTC-USDT').
            side (str): Order side, either 'BUY' or 'SELL'.
            order_type (str): Type of the order. Options include 'MARKET', 'LIMIT', 
                            'TAKE_STOP_LIMIT', 'TAKE_STOP_MARKET', 'TRIGGER_LIMIT', 'TRIGGER_MARKET'.
            stop_price (float, optional): The trigger price for the order, used in specific order types 
                                        like 'TAKE_STOP_LIMIT', 'TAKE_STOP_MARKET', 'TRIGGER_LIMIT', 
                                        and 'TRIGGER_MARKET'.
            quantity (float, optional): The quantity of the asset to trade, e.g., 0.1 BTC.
            quote_order_qty (float, optional): The quote order quantity, e.g., 100 USDT. If both 
                                            `quantity` and `quote_order_qty` are provided, `quantity` 
                                            takes precedence.
            price (float, optional): The price at which the order is placed. Required for limit orders.
            new_client_order_id (str, optional): Custom order ID for the user, containing only letters, 
                                                numbers, and underscores. Must be 1 to 40 characters in 
                                                length. Each order must have a unique ID within a 2-hour 
                                                query range.
            time_in_force (str, optional): The time in force policy for the order. Options include 
                                        'PostOnly', 'GTC', 'IOC', 'FOK'. Defaults to 'GTC' if not specified.
    """
    def __init__(self,
                 symbol: str,
                 side: str,
                 order_type: str,
                 stop_price: float = None,
                 quantity: float = None,
                 quote_order_qty: float = None,
                 price: float = None,
                 new_client_order_id: str = None,
                 time_in_force: str = None):
        
        
        

        if order_type=="LIMIT" and price is None:   
            raise ValueError("Price is required for LIMIT orders.")

        if order_type in ["TAKE_STOP_LIMIT", "TAKE_STOP_MARKET", "TRIGGER_LIMIT", "TRIGGER_MARKET"] and stop_price is None:
            raise ValueError("Stop price is required for TAKE_STOP_LIMIT, TAKE_STOP_MARKET, TRIGGER_LIMIT, and TRIGGER_MARKET orders.")

        if quantity is None and quote_order_qty is None:
            raise ValueError("Either quantity or quote_order_qty must be provided.")

          

        self.symbol = symbol
        self.side = side
        self.type = order_type
        self.stopPrice = stop_price
        self.quantity = quantity
        self.quoteOrderQty = quote_order_qty
        self.price = price
        self.newClientOrderId = new_client_order_id
        self.timeInForce = time_in_force

    def to_dict(self, clean_none=True) -> dict:
        order_dict = {
            "symbol": self.symbol,
            "side": self.side,
            "type": self.type,
            "stopPrice": self.stopPrice,
            "quantity": self.quantity,
            "quoteOrderQty": self.quoteOrderQty,
            "price": self.price,
            "newClientOrderId": self.newClientOrderId,
            "timeInForce": self.timeInForce
        }
        return {k: v for k, v in order_dict.items() if v is not None} if clean_none else order_dict

    def to_json(self, clean_none=True) -> str:
        return json.dumps(self.to_dict(clean_none))



