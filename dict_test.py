response = {"Body":{"stkCallback":{"MerchantRequestID":"18666-440437-1","CheckoutRequestID":"ws_CO_190520210856425749","ResultCode":17,"ResultDesc":"Rule limited."}}}

print(response['Body']['stkCallback']['MerchantRequestID'])