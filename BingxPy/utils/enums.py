from enum import Enum, auto
import json

class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name




class TransferType:
    FUNDING_TO_STANDARD                  = "FUND_SFUTURES"       # Funding Account -> Standard Contract
    STANDARD_TO_FUNDING                  = "SFUTURES_FUND"       # Standard Contract -> Funding Account
    FUNDING_TO_PERPETUAL                 = "FUND_PFUTURES"       # Funding Account -> Perpetual Futures
    PERPETUAL_TO_FUNDING                 = "PFUTURES_FUND"       # Perpetual Futures -> Funding Account
    STANDARD_TO_PERPETUAL                = "SFUTURES_PFUTURES"   # Standard Contract -> Perpetual Futures
    PERPETUAL_TO_STANDARD                = "PFUTURES_SFUTURES"   # Perpetual Futures -> Standard Contract
    FUNDING_TO_GRID                      = "FUND_STRADING"       # Funding Account -> Grid Account
    GRID_TO_FUNDING                      = "STRADING_FUND"       # Grid Account -> Funding Account
    FUNDING_TO_COPY_TRADE                = "FUND_CTRADING"       # Funding Account -> Copy Trade Account
    STANDARD_TO_COPY_TRADE               = "SFUTURES_CTRADING"   # Standard Contract -> Copy Trade Account
    PERPETUAL_TO_COPY_TRADE              = "PFUTURES_CTRADING"   # Perpetual Futures -> Copy Trade Account
    COPY_TRADE_TO_FUNDING                = "CTRADING_FUND"       # Copy Trade Account -> Funding Account
    COPY_TRADE_TO_STANDARD               = "CTRADING_SFUTURES"   # Copy Trade Account -> Standard Contract
    COPY_TRADE_TO_PERPETUAL              = "CTRADING_PFUTURES"   # Copy Trade Account -> Perpetual Futures




class KlineType:
    MIN_1   = "1min"
    MIN_3   = "3min"
    MIN_5   = "5min"
    MIN_15  = "15min"
    MIN_30  = "30min"
    MIN_60  = "60min"
    HOUR_2  = "2hour"
    HOUR_4  = "4hour"
    HOUR_6  = "6hour"
    HOUR_8  = "8hour"
    HOUR_12 = "12hour"
    DAY_1   = "1day"
    DAY_3   = "3day"
    WEEK_1  = "1week"
    MONTH_1 = "1mon"

class Interval:
    MIN_1 = "1m"
    MIN_3 = "3m"
    MIN_5 = "5m"
    MIN_15 = "15m"
    MIN_30 = "30m"
    HOUR_1 = "1h"
    HOUR_2 = "2h"
    HOUR_4 = "4h"
    HOUR_6 = "6h"
    HOUR_8 = "8h"
    HOUR_12 = "12h"
    DAY_1  = "1d"
    DAY_3  = "3d"
    WEEK_1 = "1w"
    MONTH_1 = "1M"


