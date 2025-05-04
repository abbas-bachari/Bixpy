
# -*- coding: utf-8 -*-
"""List of available endpoints.

This module contains the list of available endpoints in the Binance API.
These endpoints are used by the :class:`BinanceClient` to interact with the API.
"""

class Endpoint:
    def __init__(self, path, method):
        self.path = path
        self.method = method


class AccountEndpoints:
    account_balance             = Endpoint("/openApi/spot/v1/account/balance", "GET")
    asset_transfer              = Endpoint("/openApi/api/v3/post/asset/transfer", "POST")
    asset_transfer_records      = Endpoint("/openApi/api/v3/asset/transfer", "GET")
    internal_transfer           = Endpoint("/openApi/wallets/v1/capital/innerTransfer/apply", "POST")
    internal_transfer_records   = Endpoint("/openApi/wallets/v1/capital/innerTransfer/records", "GET")
    all_account_balance         = Endpoint("/openApi/account/v1/allAccountBalance", "GET")
    generate_listen_Key         = Endpoint("/openApi/user/auth/userDataStream",'POST')
    extend_listen_Key           = Endpoint("/openApi/user/auth/userDataStream",'PUT')
    delete_listen_Key           = Endpoint("/openApi/user/auth/userDataStream",'DELETE')

class SubAccountEndpoints:
    # Create a sub-account
    create= Endpoint("/openApi/subAccount/v1/create", "POST")

    # Get sub-account information and permissions
    api_permissions = Endpoint("/openApi/v1/account/apiPermissions", "GET")
    account_uid = Endpoint("/openApi/account/v1/uid", "GET")
    list_sub_accounts = Endpoint("/openApi/subAccount/v1/list", "GET")
    get_assets = Endpoint("/openApi/subAccount/v1/assets", "GET")

    # API key management
    create_api_key = Endpoint("/openApi/subAccount/v1/apiKey/create", "POST")
    query_api_key = Endpoint("/openApi/account/v1/apiKey/query", "GET")
    edit_api_key = Endpoint("/openApi/subAccount/v1/apiKey/edit", "POST")
    delete_api_key = Endpoint("/openApi/subAccount/v1/apiKey/del", "POST")

    # Update sub-account status
    update_status = Endpoint("/openApi/subAccount/v1/updateStatus", "POST")

    # Inner transfers and permissions
    authorize_inner_transfer = Endpoint("/openApi/account/v1/innerTransfer/authorizeSubAccount", "POST")
    apply_inner_transfer = Endpoint("/openApi/wallets/v1/capital/subAccountInnerTransfer/apply", "POST")
    

    # Deposit address and deposit history
    create_deposit_address = Endpoint("/openApi/wallets/v1/capital/deposit/createSubAddress", "POST")
    deposit_address = Endpoint("/openApi/wallets/v1/capital/subAccount/deposit/address", "GET")
    deposit_history = Endpoint("/openApi/wallets/v1/capital/deposit/subHisrec", "GET")
    inner_transfer_records = Endpoint("/openApi/wallets/v1/capital/subAccount/innerTransfer/records", "GET")

    # Asset transfer history
    transfer_history = Endpoint("/openApi/account/transfer/v1/subAccount/asset/transferHistory", "GET")
    support_transfer_coins = Endpoint("/openApi/account/transfer/v1/subAccount/transferAsset/supportCoins", "POST")
    transfer_asset = Endpoint("/openApi/account/transfer/v1/subAccount/transferAsset", "POST")

    # Get balance of all accounts
    all_account_balance = Endpoint("/openApi/subAccount/v1/allAccountBalance", "GET")

class WalletEndpoints:
    deposit_history = Endpoint("/openApi/api/v3/capital/deposit/hisrec", "GET")
    withdraw_history = Endpoint("/openApi/api/v3/capital/withdraw/history", "GET")
    all_configs = Endpoint("/openApi/wallets/v1/capital/config/getall", "GET")
    apply_withdraw = Endpoint("/openApi/wallets/v1/capital/withdraw/apply", "POST")
    deposit_address = Endpoint("/openApi/wallets/v1/capital/deposit/address", "GET")
    deposit_risk_records = Endpoint("/openApi/wallets/v1/capital/deposit/riskRecords", "GET")
   
class AgentEndpoints:
    get_invited_users           = Endpoint("/openApi/agent/v1/account/inviteAccountList", "GET")
    get_daily_commission        = Endpoint("/openApi/agent/v1/reward/commissionDataList", "GET")
    get_user_info               = Endpoint("/openApi/agent/v1/account/inviteRelationCheck", "GET")
    get_invited_users_deposit   = Endpoint("/openApi/agent/v1/account/inviteRelationCheck", "GET")
    get_api_commission          = Endpoint("/openApi/agent/v1/reward/third/commissionDataList", "GET")
    get_partner_data            = Endpoint("/openApi/agent/v1/asset/partnerData", "GET")




class SpotMarketEndpoints:
    server_time     = Endpoint("/openApi/spot/v1/server/time", "GET")
    common_symbols  = Endpoint("/openApi/spot/v1/common/symbols", "GET")
    market_trades   = Endpoint("/openApi/spot/v1/market/trades", "GET")
    order_book   = Endpoint("/openApi/spot/v1/market/depth", "GET")
    order_book_aggregation = Endpoint("/openApi/spot/v2/market/depth", "GET")
    market_kline = Endpoint("/openApi/spot/v2/market/kline", "GET")
    historical_kline    = Endpoint("/openApi/market/his/v1/kline", "GET")
    
    price_ticker    = Endpoint("/openApi/spot/v1/ticker/price", "GET")
    order_book_ticker     = Endpoint("/openApi/spot/v1/ticker/bookTicker", "GET")
    ticker_24hr     = Endpoint("/openApi/spot/v1/ticker/24hr", "GET")
    old_trade_lookup   = Endpoint("/openApi/market/his/v1/trade", "GET")

class SpotTradesEndpoints:
    place_order = Endpoint("/openApi/spot/v1/trade/order", "POST")
    place_multiple_orders = Endpoint("/openApi/spot/v1/trade/batchOrders", "POST")
    cancel_order = Endpoint("/openApi/spot/v1/trade/cancel", "POST")
    cancel_multiple_orders = Endpoint("/openApi/spot/v1/trade/cancelOrders", "POST")
    cancel_all_open_orders = Endpoint("/openApi/spot/v1/trade/cancelOpenOrders", "POST")
    cancel_replace_order = Endpoint("/openApi/spot/v1/trade/order/cancelReplace", "POST")
    order_details = Endpoint("/openApi/spot/v1/trade/query", "GET")
    get_open_orders = Endpoint("/openApi/spot/v1/trade/openOrders", "GET")
    get_order_history = Endpoint("/openApi/spot/v1/trade/historyOrders", "GET")
    transaction_details = Endpoint("/openApi/spot/v1/trade/myTrades", "GET")
    get_user_commission_rate = Endpoint("/openApi/spot/v1/user/commissionRate", "GET")
    cancel_all_after_time = Endpoint("/openApi/spot/v1/trade/cancelAllAfter", "POST")
    place_oco_order = Endpoint("/openApi/spot/v1/oco/order", "POST")
    cancel_oco_order = Endpoint("/openApi/spot/v1/oco/cancel", "POST")
    get_oco_order_list = Endpoint("/openApi/spot/v1/oco/orderList", "GET")
    get_oco_open_order_list = Endpoint("/openApi/spot/v1/oco/openOrderList", "GET")
    get_oco_order_history = Endpoint("/openApi/spot/v1/oco/historyOrderList", "GET")








class PerpetualAccountEndpoints:
    get_balance         = Endpoint("/openApi/swap/v3/user/balance", "GET")
    get_positions       = Endpoint("/openApi/swap/v2/user/positions", "GET")
    get_income          = Endpoint("/openApi/swap/v2/user/income", "GET")
    get_income_export   = Endpoint("/openApi/swap/v2/user/income/export", "GET")
    get_commission_rate = Endpoint("/openApi/swap/v2/user/commissionRate", "GET")

    generate_listen_Key= Endpoint("/openApi/user/auth/userDataStream",'POST')
    extend_listen_Key= Endpoint("/openApi/user/auth/userDataStream",'PUT')
    delete_listen_Key= Endpoint("/openApi/user/auth/userDataStream",'DELETE')
    
class PerpetualMarketEndpoints:
    get_server_time          = Endpoint("/openApi/swap/v2/server/time", "GET")
    
    get_symbols                     = Endpoint("/openApi/swap/v2/quote/contracts","GET")
    order_book                      = Endpoint("/openApi/swap/v2/quote/depth","GET")
    recent_trades_list              = Endpoint("/openApi/swap/v2/quote/trades","GET")
    mark_price_and_funding_rate     = Endpoint("/openApi/swap/v2/quote/premiumIndex","GET")
    get_funding_rate_history        = Endpoint("/openApi/swap/v2/quote/fundingRate","GET")
    kline_data                      = Endpoint("/openApi/swap/v3/quote/klines","GET")
    open_interest_statistics        = Endpoint("/openApi/swap/v2/quote/openInterest","GET")
    get_24hr_ticker_price_change    = Endpoint("/openApi/swap/v2/quote/ticker","GET")
    historical_transaction_orders   = Endpoint("/openApi/swap/v1/market/historicalTrades","GET")
    symbol_order_book_ticker        = Endpoint("/openApi/swap/v2/quote/bookTicker","GET")
    mark_price_kline                = Endpoint("/openApi/swap/v1/market/markPriceKlines","GET")
    symbol_price_ticker             = Endpoint("/openApi/swap/v1/ticker/price","GET")

class PerpetualTradeEndpoints:
    test_order                              = Endpoint("/openApi/swap/v2/trade/order/test","POST")
    place_order                             = Endpoint("/openApi/swap/v2/trade/order","POST")
    
    place_multiple_orders                   = Endpoint("/openApi/swap/v2/trade/batchOrders","POST")
    close_all_positions                     = Endpoint("/openApi/swap/v2/trade/closeAllPositions","POST")
    cancel_order                            = Endpoint("/openApi/swap/v2/trade/order","DELETE")
    cancel_multiple_orders                  = Endpoint("/openApi/swap/v2/trade/batchOrders","DELETE")
    cancel_all_open_orders                  = Endpoint("/openApi/swap/v2/trade/allOpenOrders","DELETE")
    get_all_open_orders                     = Endpoint("/openApi/swap/v2/trade/openOrders","GET")
    get_pending_order_status                = Endpoint("/openApi/swap/v2/trade/openOrder","GET")
    get_order_details                       = Endpoint("/openApi/swap/v2/trade/order","GET")
    get_margin_type                         = Endpoint("/openApi/swap/v2/trade/marginType","GET")
    set_margin_type                         = Endpoint("/openApi/swap/v2/trade/marginType","POST")
    get_leverage                            = Endpoint("/openApi/swap/v2/trade/leverage","GET")
    set_leverage                            = Endpoint("/openApi/swap/v2/trade/leverage","POST")
    force_orders                            = Endpoint("/openApi/swap/v2/trade/forceOrders","GET")
    get_order_history                       = Endpoint("/openApi/swap/v2/trade/allOrders","GET")
    modify_isolated_position_margin         = Endpoint("/openApi/swap/v2/trade/positionMargin","POST")
    get_historical_transaction_orders       = Endpoint("/openApi/swap/v2/trade/allFillOrders","GET")
    set_position_mode                       = Endpoint("/openApi/swap/v1/positionSide/dual","POST")
    get_position_mode                       = Endpoint("/openApi/swap/v1/positionSide/dual","GET")
    cancel_and_replace_order                = Endpoint("/openApi/swap/v1/trade/cancelReplace","POST")
    cancel_and_replace_batches_orders       = Endpoint("/openApi/swap/v1/trade/batchCancelReplace","POST")
    cancel_all_after                        = Endpoint("/openApi/swap/v2/trade/cancelAllAfter","POST")
    close_position_by_position_id           = Endpoint("/openApi/swap/v1/trade/closePosition","POST")
    get_all_orders                          = Endpoint("/openApi/swap/v1/trade/fullOrder","GET")
    position_and_maintenance_margin_ratio   = Endpoint("/openApi/swap/v1/maintMarginRatio","GET")
    get_historical_transaction_details      = Endpoint("/openApi/swap/v2/trade/fillHistory","GET")
    get_position_history                    = Endpoint("/openApi/swap/v1/trade/positionHistory","GET")
    get_isolated_margin_change_history      = Endpoint("/openApi/swap/v1/positionMargin/history","GET")
    get_vst                                 = Endpoint("/openApi/swap/v1/trade/getVst","POST")
    place_twap_order                        = Endpoint("/openApi/swap/v1/twap/order","POST")
    get_twap_entrusted_order                = Endpoint("/openApi/swap/v1/twap/openOrders","GET")
    get_twap_historical_orders              = Endpoint("/openApi/swap/v1/twap/historyOrders","GET")
    get_twap_order_details                  = Endpoint("/openApi/swap/v1/twap/orderDetail","GET")
    cancel_twap_order                       = Endpoint("/openApi/swap/v1/twap/cancelOrder","POST")
    switch_multi_assets_mode                = Endpoint("/openApi/swap/v1/trade/assetMode","POST")
    get_multi_assets_mode                   = Endpoint("/openApi/swap/v1/trade/assetMode","GET")
    get_multi_assets_rules                  = Endpoint("/openApi/swap/v1/trade/multiAssetsRules","GET")
    get_multi_assets_margin                 = Endpoint("/openApi/swap/v1/user/marginAssets","GET")
    one_click_reverse_position              = Endpoint("/openApi/swap/v1/trade/reverse","POST")
    automatic_margin_addition               = Endpoint("/openApi/swap/v1/trade/autoAddMargin","POST")
   



class StandardEndpoints:
    get_positions   = Endpoint("/openApi/contract/v1/allPosition", "GET")
    get_orders      = Endpoint("/openApi/contract/v1/allOrders", "GET")
    get_server_time = Endpoint("/openApi/spot/v1/server/time", "GET")


class CopyTradingEndpoints:
    get_current_order = Endpoint("/openApi/copyTrading/v1/swap/trace/currentTrack", "GET")
    close_positions = Endpoint("/openApi/copyTrading/v1/swap/trace/closeTrackOrder", "POST")
    set_profit_and_loss = Endpoint("/openApi/copyTrading/v1/swap/trace/setTPSL", "POST")
    sell_order = Endpoint("/openApi/copyTrading/v1/spot/trader/sellOrder", "POST")

    

