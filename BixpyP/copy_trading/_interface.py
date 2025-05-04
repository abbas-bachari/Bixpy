from ..utils._endpoints import CopyTradingEndpoints as EP


def get_current_order(self,symbol: str,offset: int = None,limit: int = None,recv_window: int = None):
        ep=EP.get_current_order
        params={
                "symbol": symbol,
                "offset": offset,
                "limit": limit,
            "recvWindow":recv_window
        }
        return self.send_request(ep.method,ep.path,params)
    
def close_positions(self,position_id: int, recv_window: int = None):
        
        ep = EP.close_positions
        params = {
            "positionId": position_id,
            "recvWindow": recv_window
        }
        return self.send_request(ep.method, ep.path, params)
def set_profit_and_loss(self,position_id: int,take_profit_mark_price: float,stop_loss_mark_price: float,recv_window: int = None):
        ep=EP.set_profit_and_loss
        params={
            "positionId": position_id,
            "takeProfitMarkPrice":take_profit_mark_price,
            "stopLossMarkPrice": stop_loss_mark_price,
            "recvWindow":recv_window
        }
        return self.send_request(ep.method,ep.path,params)
def sell_order(self,order_id: int,recv_window: int = None):
        ep=EP.sell_order
        params={
                "orderId": order_id,
                "recvWindow":recv_window
        }
        return self.send_request(ep.method,ep.path,params)