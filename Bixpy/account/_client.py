from ..utils.api_client import ApiClient as __api


 
   
class Account(__api):   
    
    
    
    
    from ._account import (
        balance,
        all_account_balance,
        transfer_asset,
        asset_transfer_records,
        internal_transfer,
        internal_transfer_records,
        generate_listen_Key,
        extend_listen_Key,
        delete_listen_Key)
     
    from ._wallet  import (
        withdraw,
        deposit_address,
        coin_info,
        deposit_history,
        withdraw_history,
        deposit_risk_records
    )
    
    from ._sub_account import (
        sub_account_create_api_key,
        sub_account_get_api_permissions,
        sub_account_get_account_uid,
        sub_account_list,
        sub_account_get_assets,
        sub_account_query_api_key,
        sub_account_edit_api_key,
        sub_account_delete_api_key,
        sub_account_update_status,
        sub_account_authorize_inner_transfer,
        sub_account_support_transfer_coins,
        sub_account_apply_inner_transfer,
        sub_account_get_inner_transfer_records,
        sub_account_get_transfer_history,
        sub_account_all_account_balance,
        sub_account_create_deposit_address,
        sub_account_get_deposit_address,
        sub_account_get_deposit_history,
        sub_account_transfer_asset
        )
    from ._agant import (
        get_invited_users,
        get_daily_commissions,
        get_invited_users_deposit,
        get_user_information,  
        get_api_commission,
        get_partner_data

    )