from ..utils._endpoints import AgentEndpoints as EP
from time import time






class Agent:
    def __init__(self,client):
        self._client=client





    def get_invited_users(self, start_time: int = None, end_time: int = None, last_uid: int = None, page_index: int = 1, page_size: int = 100, recv_window: int = None):
        
        
        """
        Retrieve a list of invited users.

        Parameters:
            start_time (int, optional): The start timestamp (milliseconds). The maximum query window is 30 days. Defaults to None.
            end_time (int, optional): The end timestamp (milliseconds). The maximum query window is 30 days. Defaults to None.
            last_uid (int, optional): The last user UID. Defaults to None.
            page_index (int, optional): Page number for pagination, must be greater than 0. Defaults to 1.
            page_size (int, optional): The number of pages. Defaults to 100 maximum 200.
            recv_window (int, optional): The receive window for the request. Defaults to None.

    
        """
    

        ep = EP.get_invited_users
        params = {
            "startTime": start_time,
            "endTime": end_time,
            "lastUid": last_uid,
            "pageIndex": page_index,
            "pageSize": page_size,
            "recvWindow": recv_window
        }
        return self._client.send_request(ep.method, ep.path, params)
    def get_daily_commissions(
        self,
        uid: int = None,
        start_time: int = int(time()*1000)-(10*24*60*60*1000), end_time: int = int(time()*1000),
        page_index: int = 1,
        page_size: int = 100,
        recv_window: int = None,
    ):
        """
        Retrieve daily commissions.

        Parameters:
            start_time (int): Start timestamp, in days, with a maximum query window of 30 days and a sliding range of the last 365 days.
            end_time (int): End timestamp, in days, with a maximum query window of 30 days and a sliding range of the last 365 days.
            uid (int, optional): The user ID. Defaults to None.
            page_index (int, optional): Page number for pagination, must be greater than 0. Defaults to 1.
            page_size (int, optional): The number of pages. Defaults to 100 maximum 200.
            recv_window (int, optional): The receive window for the request. Defaults to None.

        Returns:
            The response from the server.
        """
        ep = EP.get_daily_commission
        params = {
            "startTime": start_time,
            "endTime": end_time,
            "uid": uid,
            "pageIndex": page_index,
            "pageSize": page_size,
            "recvWindow": recv_window,
        }
        return self._client.send_request(ep.method, ep.path, params)
    def get_user_information(self,uid:int,recv_window: int = None):
        ep =EP.get_user_info
        params = {
            "uid": uid,
            "recvWindow":recv_window
        }
        return self._client.send_request(ep.method, ep.path, params)

    def get_invited_users_deposit(self, uid: int, start_time: int = int(time()*1000)-(30*24*60*60*1000), end_time: int = int(time()*1000), biz_type: int = 1, page_index: int = 1, page_size: int = 100, recv_window: int = None):
        """
        Retrieve deposit information for invited users.

        Parameters:
            uid (int): User ID.
            start_time (int): Start timestamp in days (last 90 days).
            end_time (int): End timestamp in days (last 90 days).
            biz_type (int, optional): Business type, default is 1 for Deposit.
            page_index (int, optional): Page number for pagination, must be greater than 0 and max is 100. Defaults to 1.
            page_size (int, optional): Number of items per page. Defaults to 100.
            recv_window (int, optional): The receive window for the request. Defaults to None.

        Returns:
            The response from the server.
        """
        ep = EP.get_invited_users_deposit
        params = {
            "uid": uid,
            "bizType": biz_type,
            "startTime": start_time,
            "endTime": end_time,
            "pageIndex": page_index,
            "pageSize": page_size,
            "recvWindow": recv_window
        }
        return self._client.send_request(ep.method, ep.path, params)
    def get_api_commission(self,  commission_biz_type: int,uid: int=None, start_time: int = int(time()*1000)-(30*24*60*60*1000), end_time: int = int(time()*1000), page_index: int = 1, page_size: int = 100, recv_window: int = None):
        """
        Retrieve API commission details.

        Parameters:
            
            commission_biz_type (int): Commission business type ( 81 for perpetual contract, 82 for spot trading).
            start_time (int): Start timestamp (days), Only supports querying data after December 1, 2023.
            end_time (int): End timestamp (days). Only supports querying data after December 1, 2023.
            uid (int, optional): User ID.
            page_index (int, optional): Page number for pagination. Defaults to 1.
            page_size (int, optional): The number of pages must be greater than 0 and the maximum value is 100. Defaults to 100.
            recv_window (int, optional): The receive window for the request. Defaults to None.

        Returns:
            The response from the server.
        """
        ep = EP.get_api_commission
        params = {
            "uid": uid,
            "commissionBizType": commission_biz_type,
            "startTime": start_time,
            "endTime": end_time,
            "pageIndex": page_index,
            "pageSize": page_size,
            "recvWindow": recv_window
        }
        return self._client.send_request(ep.method, ep.path, params)
    def get_partner_data(
        self,
        uid: int = None,
        start_time: int = int(time() * 1000) - (30 * 24 * 60 * 60 * 1000),
        end_time: int = int(time() * 1000),
        page_index: int = 1,
        page_size: int = 100,
        recv_window: int = None,
        ) -> dict:
        """Retrieve partner data.

        Parameters:
            uid (int, optional): User ID. Defaults to None.
            start_time (int, optional): Start timestamp (milliseconds). Defaults to 30 days ago.
            end_time (int, optional): End timestamp (milliseconds). Defaults to current time.
            page_index (int, optional): Page number for pagination. Defaults to 1.
            page_size (int, optional): The number of pages must be greater than 0 and the maximum value is 100. Defaults to 100.
            recv_window (int, optional): The receive window for the request. Defaults to None.

        Returns:
            dict: The server's response to the request.
        """

        ep = EP.get_partner_data
        params = {
            "uid": uid,
            "startTime": start_time,
            "endTime": end_time,
            "pageIndex": page_index,
            "pageSize": page_size,
            "recvWindow": recv_window,
        }

        return self._client.send_request(ep.method, ep.path, params)
