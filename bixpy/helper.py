from datetime import datetime,timezone

def kline_to_dict(kline: list) -> dict:
    """
    Convert a list of data returned from the `kline` method to a dictionary:
    ### return:
        { "open_time", "open", "high", "low", "close", "volume", "close_time", "quote_volume"}
    """
    
    return {
        "open_time": datetime.fromtimestamp (kline[0]//1000).isoformat(sep=' '),
        "open": kline[1],
        "high": kline[2],
        "low": kline[3],
        "close": kline[4],
        "volume": kline[5],
        "close_time":datetime.fromtimestamp (kline[6]//1000).isoformat(sep=' '),
        "quote_volume": kline[7]
    }
def klines_to_dict(klines: list[list]) -> list[dict]:
    """Convert a list of klines data to a list of dictionaries.
        ### return:
        [{ "open_time", "open", "high", "low", "close", "volume", "close_time", "quote_volume"}, ...]
    """
    return [kline_to_dict(kline) for kline in klines]