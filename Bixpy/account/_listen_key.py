from ..utils._endpoints import AccountEndpoints as EP
class ListenKey:
    def __init__(self, client):
        self._client = client
    def generate(self):
        ep=EP.generate_listen_Key
        return self._client.send_request(ep.method, ep.path)

    def extend(self, listenKey: str=None):
        ep=EP.extend_listen_Key

        params = {"listenKey": listenKey} if listenKey else {}
        return self._client.send_request(ep.method, ep.path,params)
        
    def delete(self, listenKey: str=None):
        ep=EP.delete_listen_Key
        
        params = {"listenKey": listenKey} if listenKey else {}
        return self._client.send_request(ep.method, ep.path,params)
    
