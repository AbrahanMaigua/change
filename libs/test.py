from pixadd import *
from dotenv import dotenv_values
import os
import datetime

config = dotenv_values(".env") 
current_time_iso8601 = datetime.datetime.now().isoformat()
start = '2023-10-17T06:19:17.491966'
appid = config['APP_ID']
cob = create_cob(appid, 50, 'test #2 de pago test')
accountsid = accountslist(appid).get('accounts')[0].get('accountId')
accountinfo = accounts(appid, accountsid )
ultima_trastion = get_cob(appid, cob[1])


print("Current time in ISO 8601 format:", current_time_iso8601)
print(get_list(appid, start, current_time_iso8601, 'ACTIVE'))
print(accountinfo)
print(cob)
print(ultima_trastion['charge']['pixKey'])
print(ultima_trastion['charge']['qrCodeImage'])
print(ultima_trastion['charge']['pixKey'])

