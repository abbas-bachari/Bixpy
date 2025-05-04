
from ..utils._endpoints import AccountEndpoints as EP




def balance(self,recv_window: int = None):
    ep =EP.account_balance
    params = {
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)


def transfer_asset(self,  type: str, asset: str, amount: float,recv_window: int = None):
    """
    Transfers a specified amount of an asset between different types of accounts.

    Params:
        type (str): The type of transfer to perform. It should be one of the predefined
                    transfer types such as FUND_SFUTURES, SFUTURES_FUND, FUND_PFUTURES,
                    PFUTURES_FUND, SFUTURES_PFUTURES, or PFUTURES_SFUTURES.
        asset (str): The asset to be transferred.
        amount (float): The amount of the asset to be transferred.
        recv_window (int, optional): The receive window for the request.

    Returns:
        The response from the server after attempting the transfer.
    """

    
    
    ep =EP.asset_transfer
    
    
    params = {
        "type": type,
        "asset": asset,
        "amount": amount,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)


def asset_transfer_records(self,  type: str,tranId:int=None, startTime: int = None, endTime: int = None,current:int=None,size:int=None,recv_window: int = None):
    """
    Retrieves asset transfer records based on specified criteria.

    Params:
        type (str): The type of transfer to filter records by. Must be one of the predefined
                    transfer types such as "FUND_SFUTURES", "SFUTURES_FUND", "FUND_PFUTURES",
                    "PFUTURES_FUND", "SFUTURES_PFUTURES", "PFUTURES_SFUTURES", "FUND_STRADING",
                    "STRADING_FUND", "FUND_CTRADING", "SFUTURES_CTRADING", "PFUTURES_CTRADING",
                    "CTRADING_FUND", "CTRADING_SFUTURES", or "CTRADING_PFUTURES".
  
        tranId (int, optional): The transaction ID to filter records.
        startTime (int, optional): The start time in milliseconds for filtering records.
        endTime (int, optional): The end time in milliseconds for filtering records.
        current (int, optional): The current page number for pagination.
        size (int, optional): The number of records to retrieve per page.
        recv_window (int, optional): The receive window for the request.

    Returns:
        The response from the server containing the transfer records that match the specified criteria.
    """

    
    ep =EP.asset_transfer_records


    params = {
        "type": type,
        "tranId": tranId,
        "startTime": startTime,
        "endTime": endTime,
        "current": current,
        "size": size,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)


def internal_transfer(self,coin: str,user_account_type: int, user_account: str,amount: float,wallet_type: int,calling_code: str=None,transfer_client_id: str=None,recv_window: int = None) -> dict:
    """Performs an internal transfer of assets.

    Args:
        coin (str): The coin to be transferred.
        user_account_type (int): The type of user account. Can be 0 for a spot wallet, 1 for a margin wallet, or 2 for a futures wallet.
        user_account (str): The user account to receive the transferred assets.
        amount (float): The amount of assets to be transferred.
        calling_code (str): The calling code of the user.
        wallet_type (int): The type of wallet. Can be 0 for a spot wallet, 1 for a margin wallet, or 2 for a futures wallet.
        transfer_client_id (str): The client ID of the transfer.
        recv_window (int, optional): The receive window for the request.

    Returns:
        The response from the server after attempting the internal transfer.
    """
    ep = EP.internal_transfer

    params = {
        "coin": coin,
        "userAccountType": user_account_type,
        "userAccount": user_account,
        "amount": amount,
        "callingCode": calling_code,
        "walletType": wallet_type,
        "transferClientId": transfer_client_id,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)


def internal_transfer_records(self, coin: str, transferClientId: str= None, startTime: int = None, endTime: int = None,offset: int = None,limit: int = None,recv_window: int = None):
    ep =EP.internal_transfer_records
    

    params = {
        "coin": coin,
        "transferClientId": transferClientId,
        "startTime": startTime,
        "endTime": endTime,
        "offset": offset,
        "limit": limit,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path,params)





def all_account_balance(self, accountType: str= None,recv_window: int = None):
   
    """
    Account type, if left blank, all assets of the account will be checked by default.
    - spot: spot (fund account),
    - stdFutures: standard futures account,
    - coinMPerp: coin base account,
    - USDTMPerp: U base account,
    - copyTrading: copy trading account,
    - grid: grid account,
    - eran: wealth account,
    - c2c: c2c account.
    """
    ep =EP.all_account_balance
    

    params = {
        "accountType": accountType,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)





def generate_listen_Key(self):
    ep=EP.generate_listen_Key
    return self.send_request(ep.method, ep.path)

def extend_listen_Key(self, listenKey: str=None):
    ep=EP.extend_listen_Key

    params = {"listenKey": listenKey} if listenKey else {}
    return self.send_request(ep.method, ep.path,params)
    


def delete_listen_Key(self, listenKey: str=None):
    ep=EP.delete_listen_Key
    
    params = {"listenKey": listenKey} if listenKey else {}
    return self.send_request(ep.method, ep.path,params)