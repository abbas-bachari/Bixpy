from ..utils._endpoints import SubAccountEndpoints as EP


def sub_account_create(self, subAccountString: str,note: str=None,recv_window: int = None):
    """
    Create sub-account.

    Parameters
    ----------
    subAccountString : str
        Sub account username,Starting with a letter, containing a number, and longer than 6 characters.
    note : str, optional
        Note of sub-account. Default is None.
    recv_window : int, optional
        The request and response timeout period in seconds.

    Returns
    -------
    dict
        Response from the server.
    """
    ep =EP.create
    params = {
            "subAccountString": subAccountString,
            "note": note,
            "recvWindow":recv_window
            }
    return self.send_request(ep.method,ep.path, params)

def sub_account_get_api_permissions(self, subAccountName: str):
    ep =EP.api_permissions
    params = {
        "subAccountName": subAccountName,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_get_account_uid(self, subAccountName: str):
    ep =EP.account_uid
    params = {
        "subAccountName": subAccountName,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_list(self, email: str, page: int = 1, limit: int = 50):
    ep =EP.list_sub_accounts
    params = {
        "email": email,
        "page": page,
        "limit": limit,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_get_assets(self, subAccountName: str):
    ep =EP.get_assets
    params = {
        "subAccountName": subAccountName,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_create_api_key(self, subAccountName: str, permissions: list):
    ep =EP.create_api_key
    params = {
        "subAccountName": subAccountName,
        "permissions": permissions,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_query_api_key(self, subAccountName: str):
    ep =EP.query_api_key
    params = {
        "subAccountName": subAccountName,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_edit_api_key(self, subAccountName: str, permissions: list):
    ep =EP.edit_api_key
    params = {
        "subAccountName": subAccountName,
        "permissions": permissions,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_delete_api_key(self, subAccountName: str):
    ep =EP.delete_api_key
    params = {
        "subAccountName": subAccountName,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_update_status(self, subAccountName: str, status: str):
    ep =EP.update_status
    params = {
        "subAccountName": subAccountName,
        "status": status,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_authorize_inner_transfer(self, fromSubAccountName: str, toSubAccountName: str):
    ep =EP.authorize_inner_transfer
    params = {
        "fromSubAccountName": fromSubAccountName,
        "toSubAccountName": toSubAccountName,
    }
    return self.send_request(ep.method,ep.path, params)


def sub_account_apply_inner_transfer(self, fromSubAccountName: str, toSubAccountName: str, amount: float, symbol: str):
    ep =EP.apply_inner_transfer
    params = {
        "fromSubAccountName": fromSubAccountName,
        "toSubAccountName": toSubAccountName,
        "amount": amount,
        "symbol": symbol,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_create_deposit_address(self, subAccountName: str, coin: str):
    ep =EP.create_deposit_address
    params = {
        "subAccountName": subAccountName,
        "coin": coin,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_get_deposit_address(self, subAccountName: str, coin: str):
    ep =EP.deposit_address
    params = {
        "subAccountName": subAccountName,
        "coin": coin,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_get_deposit_history(self, subAccountName: str, coin: str, startTime: int, endTime: int, limit: int):
    ep =EP.deposit_history
    params = {
        "subAccountName": subAccountName,
        "coin": coin,
        "startTime": startTime,
        "endTime": endTime,
        "limit": limit,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_get_inner_transfer_records(self, subAccountName: str, startTime: int, endTime: int, limit: int):
    ep =EP.inner_transfer_records
    params = {
        "subAccountName": subAccountName,
        "startTime": startTime,
        "endTime": endTime,
        "limit": limit,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_get_transfer_history(self, subAccountName: str, symbol: str, startTime: int, endTime: int, limit: int):
    ep =EP.transfer_history
    params = {
        "subAccountName": subAccountName,
        "symbol": symbol,
        "startTime": startTime,
        "endTime": endTime,
        "limit": limit,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_support_transfer_coins(self, subAccountName: str):
    ep =EP.support_transfer_coins
    params = {
        "subAccountName": subAccountName,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_transfer_asset(self, subAccountName: str, symbol: str, amount: float, transferType: str):
    ep =EP.transfer_asset
    params = {
        "subAccountName": subAccountName,
        "symbol": symbol,
        "amount": amount,
        "transferType": transferType,
    }
    return self.send_request(ep.method,ep.path, params)

def sub_account_all_account_balance(self,page_index: int , page_size: int , sub_uid: int=None, account_type: str=None,  recv_window: int = None):
    endpoint = EP.all_account_balance
    params = {
        "subUid": sub_uid,
        "accountType": account_type,
        "pageIndex": page_index,
        "pageSize": page_size,
        "recvWindow":recv_window
    }
    return self.send_request(endpoint.method, endpoint.path, params)

