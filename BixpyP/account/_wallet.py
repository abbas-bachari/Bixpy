from ..utils._endpoints import WalletEndpoints as EP









def coin_info(self,coin: str=None, recv_window: int = None):
    """
    Retrieve information about a specific coin or all coins.

    Args:
        coin (str, optional): The coin symbol for which information is required. Defaults to None, which retrieves information for all coins.
        recv_window (int, optional): The receive window for the request.

    Returns:
        The response from the server containing the coin information.
    """

    ep=EP.all_configs

    payload = {"coin": coin, "recvWindow":recv_window}
    return self.send_request(ep.method, ep.path, payload)




def withdraw(self, coin: str, address: str, amount: float,wallet_type: int,network: str=None,address_tag: str=None,wallet_order_id: str=None, recv_window: int = None):
    
    
    """
    Apply a withdrawal.

    Args:
        coin (str): The coin to be withdrawn.
        address (str): The address to withdraw to.
        amount (float): The amount to be withdrawn.
        wallet_type (int): The type of account to withdraw from. 1 for a fund account, 2 for a standard account, 3 for a perpetual account.
        network (str, optional): The network to use for the withdrawal. Defaults to None.
        address_tag (str, optional): Tag or memo for the withdrawal. Defaults to None.
        wallet_order_id (str, optional): Customer-defined withdrawal ID. Defaults to None.
        "recvWindow":recv_window: Additional keyword arguments.

    Returns:
        The response from the server.
    """
    ep=EP.apply_withdraw

    payload = {
        "coin": coin,
        "network": network,
        "address":address,
        "addressTag": address_tag,
        "amount": amount,
        "walletType": wallet_type,
        "walletOrderId": wallet_order_id,
        "recvWindow":recv_window
        }
        
    
    return self.send_request(ep.method, ep.path, payload)


def deposit_history(self, coin: str = None, status: int = None, start_time: int = None, end_time: int = None, offset: int = None, limit: int = None, recv_window: int = None):
    """
    Get deposit history.

    Args:
        coin (str, optional): The coin to get deposit history for. Defaults to None.
        status (int, optional): The status of the deposit. Defaults to None.
        start_time (int, optional): The start time of the query. Defaults to None.
        end_time (int, optional): The end time of the query. Defaults to None.
        offset (int, optional): The offset of the query. Defaults to None.
        limit (int, optional): The limit of the query. Defaults to None.
        "recvWindow":recv_window: Additional keyword arguments.

    Returns:
        The response from the server.
    """
    ep = EP.deposit_history
    payload = {
        "coin": coin,
        "status": status,
        "startTime": start_time,
        "endTime": end_time,
        "offset": offset,
        "limit": limit,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, payload)


def withdraw_history(self, coin: str = None,id:str=None, withdraw_order_id: str = None, status: int = None, start_time: int = None, end_time: int = None, offset: int = None, limit: int = None, recv_window: int = None):
    """
    Get withdrawal history.

    Args:
        coin (str, optional): The coin to get withdrawal history for. Defaults to None.
        withdraw_order_id (str, optional): The ID of the withdrawal. Defaults to None.
        status (int, optional): The status of the withdrawal. Defaults to None.
        start_time (int, optional): The start time of the query. Defaults to None.
        end_time (int, optional): The end time of the query. Defaults to None.
        offset (int, optional): The offset of the query. Defaults to None.
        limit (int, optional): The limit of the query. Defaults to None.
        "recvWindow":recv_window: Additional keyword arguments.

    Returns:
        The response from the server.
    """
    ep = EP.withdraw_history
    payload = {
        "id":id,
        "coin": coin,
        "withdrawOrderId": withdraw_order_id,
        "status": status,
        "startTime": start_time,
        "endTime": end_time,
        "offset": offset,
        "limit": limit,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, payload)


def deposit_address(self, coin: str, offset: int = None, limit: int = None, recv_window: int = None):
    
    """
    Get deposit address.

    Args:
        coin (str): The coin to get deposit address for.
        offset (int, optional): The offset of the query. Defaults to None.
        limit (int, optional): The limit of the query. Defaults to None.
        "recvWindow":recv_window: Additional keyword arguments.

    Returns:
        The response from the server.
    """
    ep = EP.deposit_address
    payload = {
        "coin": coin,
        "offset": offset,
        "limit": limit,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, payload)



def deposit_risk_records(self, recv_window: int = None):
    """
    Retrieve risk records related to deposits.

    Args:
        recv_window (int, optional): The receive window for the request.

    Returns:
        The response from the server containing deposit risk information.
    """

    ep=EP.deposit_risk_records

    params = {"recvWindow":recv_window}

    return self.send_request(ep.method, ep.path, params)



