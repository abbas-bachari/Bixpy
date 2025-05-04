from ..utils._endpoints import StandardEndpoints as EP
def server_time(self):
        ep=EP.get_server_time
        return self.send_request(ep.method,ep.path)
    
def get_positions(self,recv_window: int = None):
        ep=EP.get_positions
        params={
            "recvWindow":recv_window
        }
        return self.send_request(ep.method,ep.path,params)
    
def get_orders(self,symbol: str,order_id: int = None,start_time: int = None,end_time: int = None,limit: int = None, recv_window: int = None):
        """Get a list of orders.

        Parameters
        ----------
        symbol : str
            The symbol of the market.
        order_id : int
            The ID of the order.
        start_time : int
            The start time of the order.
        end_time : int
            The end time of the order.
        limit : int
            The maximum number of orders to return.

        Returns
        -------
        dict
            The server's response to the request.
        """
        ep = EP.get_orders
        params = {
            "symbol": symbol,
            "orderId": order_id,
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "recvWindow": recv_window
        }
        return self.send_request(ep.method, ep.path, params)