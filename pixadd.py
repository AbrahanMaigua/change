import requests
import http.client

import random
import datetime
import json
import time

def create_cob(AppID:str, valor:int, cometdv:str):
    headers = {
        'Authorization': AppID,
        'content-type': 'application/json',
    }

    params = {
        'return_existing': 'true',
    }
    nun = str(random.randrange(0,1000))
    json_data = {
        'correlationID':nun,
        'value': valor,
        'comment':cometdv,
    }

    response = requests.post('https://api.openpix.com.br/api/v1/charge', params=params, headers=headers, json=json_data)
    return response, nun
def get_cob(appid, idpix):
    '''
    charge ID or correlation ID. You will 
    need URI encoding if your correlation ID has characters outside
     the ASCII set or reserved characters (%, #, /).
    '''
    conn = http.client.HTTPSConnection("api.openpix.com.br")
    headers = { 'Authorization': appid }
    conn.request("GET", f"/api/v1/charge/{idpix}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()

    return dict(json.loads((data.decode("utf-8"))))



def get_list(appid:str, start:str, end:str, status:str):

    ## date and time in ISO 8601 format
    ## YYYY-MM-DDTHH:MM:SS.ssssssZ

    """
    start	
        string <date-time> (Start Date)
        Example: start=2020-01-01T00:00:00Z

        Start date used in the query. Complies with RFC 3339.
    end	
        string <date-time> (End Date)
        Example: end=2020-12-01T17:00:00Z

        End date used in the query. Complies with RFC 3339.
    status	
        string
        Enum: "ACTIVE" "COMPLETED" "EXPIRED" 
    """
    start = start.replace(':', '&')
    end   = end.replace(':', '&')

    conn    = http.client.HTTPSConnection("api.openpix.com.br")
    headers = { 'Authorization': appid }
    conn.request("GET", f"/api/v1/charge?start={start}&end={end}Z&status={status}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()

    return dict(json.loads((data.decode("utf-8"))))


def accountslist(appid):

    conn = http.client.HTTPSConnection("api.openpix.com.br")
    headers = { 'Authorization': appid }
    conn.request("GET", "/api/v1/account/", headers=headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()

    return dict(json.loads((data.decode("utf-8"))))

def accounts(appid, accountId):

    conn = http.client.HTTPSConnection("api.openpix.com.br")
    headers = { 'Authorization': appid }
    conn.request("GET", f"/api/v1/account/{accountId}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()

    return dict(json.loads((data.decode("utf-8"))))

# Get the current date and time in ISO 8601 format
#YYYY-MM-DDTHH:MM:SS.ssssssZ
current_time_iso8601 = datetime.datetime.now().isoformat()
start = '2023-10-17T06:19:17.491966'
appid = 'APP_id'
cob = create_cob(appid, 5, 'test #2 de pago real')


accountsid = accountslist(appid).get('accounts')[0].get('accountId')
accountinfo = accounts(appid, accountsid )
print("Current time in ISO 8601 format:", current_time_iso8601)
print(get_list(appid, start, current_time_iso8601, 'ACTIVE'))
print(accountinfo)
print(cob)

while True:
    cobr   = get_cob(appid, cob[1] )
    status = cobr.get('charge')['status']
    print(cobr)
    if status == 'ACTIVE':
        time.sleep(5)
        print(status)

    else:
        break
