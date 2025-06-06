from typing import Optional
import gzip,io,json
import logging
import threading
from websocket import (
    ABNF,
    create_connection,
    WebSocketException,
    WebSocketConnectionClosedException,
    WebSocketTimeoutException,
)
from .utils import parse_proxies




class WebSocketManager(threading.Thread):
    def __init__(self,stream_url,on_message=None,on_open=None,on_close=None,on_error=None,on_ping=None,on_pong=None,logger=None,timeout=None, proxies: Optional[dict] = None,):
        threading.Thread.__init__(self)
        
        self.logger = logger if logger else logging.getLogger(__name__)
        self.stream_url =  stream_url 
        self.on_message = on_message
        self.on_open = on_open
        self.on_close = on_close
        self.on_ping = on_ping
        self.on_pong = on_pong
        self.on_error = on_error
        self.timeout = timeout
        self._proxy_params = parse_proxies(proxies) if proxies else {}
        

        self.create_ws_connection()

    def create_ws_connection(self):
        self.logger.debug(f"Creating connection with WebSocket Server: {self.stream_url}, proxies: {self._proxy_params}",)

        self.ws = create_connection(self.stream_url, timeout=self.timeout, **self._proxy_params)
        self.logger.debug(f"WebSocket connection has been established: {self.stream_url}, proxies: {self._proxy_params}",)
        self._callback(self.on_open)

    def run(self):
        self.read_data()

    def send_message(self, message):
        self.logger.debug("Sending message to Binance WebSocket Server: %s", message)
        self.ws.send(message)

    def ping(self):
        self.ws.ping()

    def read_data(self):
        data = ""
        while True:
            try:
                op_code, frame = self.ws.recv_data_frame(True)
                
            except WebSocketException as e:
                if isinstance(e, WebSocketConnectionClosedException):
                    self.logger.error("Lost websocket connection")
                elif isinstance(e, WebSocketTimeoutException):
                    self.logger.error("Websocket connection timeout")
                else:
                    self.logger.error("Websocket exception: {}".format(e))
                self._handle_exception(e)
                break
            except Exception as e:
                self.logger.error("Exception in read_data: {}".format(e))
                self._handle_exception(e)
                break
           
            
            if op_code == ABNF.OPCODE_CLOSE:
                # self.logger.warning("CLOSE frame received, closing websocket connection")
                self._callback(self.on_close)
                break
            self._handle_data(op_code, frame, data)
            self._handle_heartbeat(op_code, frame)
            
            

    def _handle_heartbeat(self, op_code, frame):
        if op_code == ABNF.OPCODE_PING:
            self._callback(self.on_ping, frame.data)
            self.ws.pong()
            self.logger.debug("Received Ping; PONG frame sent back")
        elif op_code == ABNF.OPCODE_PONG:
            self.logger.debug("Received PONG frame")
            self._callback(self.on_pong)

    
    def _to_dict(self,message):
        msg=message
        if isinstance(message,str):
            try:
                msg=json.loads(message)
            except:
                pass
        return msg

    
    def _handle_data(self, op_code, frame, data):
        
       
        if ABNF.OPCODE_BINARY:
            compressed_data = gzip.GzipFile(fileobj=io.BytesIO(frame.data), mode='rb')
            decompressed_data = compressed_data.read()
            data  = decompressed_data.decode('utf-8')
        
        elif op_code == ABNF.OPCODE_TEXT:
            data = frame.data.decode("utf-8")
            
        self._callback((self.on_message), self._to_dict(data))


    def close(self):
        if not self.ws.connected:
            self.logger.warning("Websocket already closed")
        else:
            self.ws.send_close()

    def _callback(self, callback, *args):
        if callback:
            try:
                callback(self, *args)
            except Exception as e:
                self.logger.error("Error from callback {}: {}".format(callback, e))
                self._handle_exception(e)

    def _handle_exception(self, e):
        if self.on_error:
            self.on_error(self, e)
        else:
            raise e