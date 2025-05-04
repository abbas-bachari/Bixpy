

from ..utils._endpoints import PerpetualAccountEndpoints as EP




def balance(self,recv_window: int = None):
    ep =EP.get_balance
    params = {
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)


def positions(self,symbol: str = None,  recv_window: int = None):
        



    ep =EP.get_positions


    params = {
        symbol:symbol,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)


def income(self,symbol: str = None,income_type: str = None,start_time: int = None,end_time: int = None,limit: int = 100,recv_window: int = None) -> dict:
    
    """Get income records.

    Parameters
    ----------
    symbol : str, optional
        Symbol.
    income_type : str, optional
        Income type. e.g. "TRANSFER", "REALIZED_PNL", "FUNDING_FEE", "TRADING_FEE", "INSURANCE_CLEAR", "TRIAL_FUND", "ADL", "SYSTEM_DEDUCTION", "GTD_PRICE".
    start_time : int, optional
        
    end_time : int, optional
        
    limit : int, optional
        Limit of records. Default is 100.
    **kwargs
        Extra parameters.

    

    
    """

    ep = EP.get_income

    params = {
        "symbol": symbol,
        "incomeType": income_type,
        "startTime": start_time,
        "endTime": end_time,
        "limit": limit,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)


def income_export(self,symbol: str = None,income_type: str = None,start_time: int = None,end_time: int = None,limit: int = 100,recv_window: int = None) -> bytes:
    """Export income records to Excel File.

    Parameters
    ----------
    symbol : str, optional
       
    income_type : str, optional
        Income type. e.g. REALIZED_PNL, FUNDING_FEE, TRADING_FEE, INSURANCE_CLEAR, TRIAL_FUND, ADL, SYSTEM_DEDUCTION
    start_time : int, optional
        
    end_time : int, optional
        
    limit : int, optional
        Limit of records. Default is 100.
    **kwargs
        Extra parameters.

    Returns
    -------
    dict
        Response as a dictionary.

    """
    ep = EP.get_income_export
    params = {
        "symbol": symbol,
        "incomeType": income_type,
        "startTime": start_time,
        "endTime": end_time,
        "limit": limit,
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path, params)



def commission_rate(self, recv_window: int = None):
    ep =EP.get_commission_rate


    params = {
        
        "recvWindow":recv_window
    }
    return self.send_request(ep.method, ep.path,params)



def listen_key_new(self):
    ep=EP.generate_listen_Key
    return self.send_request(ep.method, ep.path)

def listen_key_renew(self, listenKey: str=None):
    ep=EP.extend_listen_Key
    params = {"listenKey": listenKey} if listenKey else {}
    return self.send_request(ep.method, ep.path,params)



def listen_key_delete(self, listenKey: str=None):
    ep=EP.delete_listen_Key 
    params = {"listenKey": listenKey} if listenKey else {}
    return self.send_request(ep.method, ep.path,params)