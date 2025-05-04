from typing import Optional

import json
import logging
from .ws_manager import WebSocketManager
import uuid

def generate_id() -> str:
    return uuid.uuid4().__str__()










class WebsocketClient:
    __SUBSCRIBE = "sub"
    __UNSUBSCRIBE = "unsub"

    def __init__( self,stream_url=None,on_message=None,on_open=None,on_close=None,on_error=None,on_ping=None,on_pong=None,logger=None,timeout=None,proxies: Optional[dict] = None ):
        self.logger = logger if logger else logging.getLogger(__name__)
        
        
        
        
        self.socket_manager = self._initialize_socket(stream_url,on_message,on_open,on_close,on_error,on_ping,on_pong,logger,timeout, proxies)

        # start the thread
        self.socket_manager.start()
        self.logger.debug("Binance WebSocket Client started.")

    def _initialize_socket( self,stream_url,on_message,on_open,on_close,on_error,on_ping, on_pong,logger, timeout, proxies):
        return WebSocketManager(
            stream_url,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            on_ping=on_ping,
            on_pong=on_pong,
            logger=logger,
            timeout=timeout,
            proxies=proxies
        )


    def send(self, message: dict):
        self.socket_manager.send_message(json.dumps(message))

    def send_message_to_server(self, message, action=None, id=None):
        if not id:
            id = generate_id()

        if action != self.__UNSUBSCRIBE:
            return self.subscribe(message, id=id)
        return self.unsubscribe(message, id=id)

    def subscribe(self, stream, id=None):
        if not id:
            id = generate_id()
        
        json_msg = json.dumps({ "id": id, "reqType": self.__SUBSCRIBE, "dataType": stream })
        self.socket_manager.send_message(json_msg)

    def unsubscribe(self, stream, id=None):
        if not id:
            id = generate_id()
        
        json_msg = json.dumps({ "id": id, "reqType": self.__UNSUBSCRIBE, "dataType": stream })
        self.socket_manager.send_message(json_msg)

    def ping(self):
        self.logger.debug("Sending ping to Binance WebSocket Server")
        self.socket_manager.ping()

    def stop(self, id=None):
        self.socket_manager.close()
        self.socket_manager.join()



   