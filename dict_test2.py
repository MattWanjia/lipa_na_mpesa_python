response = {"Body":{"stkCallback":{"MerchantRequestID":"8322-4140483-1","CheckoutRequestID":"ws_CO_190520210905266754","ResultCode":0,"ResultDesc":"The service request is processed successfully.","CallbackMetadata":{"Item":[{"Name":"Amount","Value":1.00},{"Name":"MpesaReceiptNumber","Value":"PEJ64N5FAO"},{"Name":"Balance"},{"Name":"TransactionDate","Value":20210519090542},{"Name":"PhoneNumber","Value":254793483810}]}}}}

transactionId = response['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
customerNumber = response['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']
amount = response['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
datePaid = response['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']

print(f'{customerNumber} paid kshs{amount} on {datePaid} on this receipt:{transactionId}')