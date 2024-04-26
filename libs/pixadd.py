import requests
import http.client
import random
import json

def create_cob(AppID:str, valor:str, cometdv:str) -> tuple:
    """
    Crea una solicitud de cobro (charge) en el servicio OpenPix.

    Args:
        AppID (str): ID de la aplicación utilizado para la autorización.
        valor (int): Valor del cobro.
        cometdv (str): Comentario o descripción del cobro.

    Returns:
        tuple: Una tupla que contiene la respuesta de la solicitud HTTP y el ID de la transacción generada.
    """
    
    valor = valor.replace('.','') 
    headers = {
        'Authorization': AppID,
        'content-type': 'application/json',
    }

    params = {
        'return_existing': 'true',
    }
    idpix = str(random.randrange(0,1000))
    json_data = {
        'correlationID':idpix,
        'value': valor ,
        'comment':cometdv,
    }

    response = requests.post('https://api.openpix.com.br/api/v1/charge', params=params, headers=headers, json=json_data)
    return response, idpix

def get_cob(appid:str, idpix:str) -> dict:
    """
    Obtiene detalles de un cobro específico mediante su ID de transacción.

    Args:
        appid (str): ID de la aplicación utilizado para la autorización.
        idpix (str): ID de la transacción de cobro.

    Returns:
        dict: Un diccionario con los detalles del cobro.
    """
    conn = http.client.HTTPSConnection("api.openpix.com.br")
    headers = { 'Authorization': appid }
    conn.request("GET", f"/api/v1/charge/{idpix}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()

    return dict(json.loads((data.decode("utf-8"))))

def get_list(appid:str, start:str, end:str, status:str) -> dict:
    """
    Obtiene una lista de cobros dentro de un rango de fechas y estado específico.

    Args:
        appid (str): ID de la aplicación utilizado para la autorización.
        start (str): Fecha y hora de inicio del rango de búsqueda (en formato ISO 8601).
        end (str): Fecha y hora de finalización del rango de búsqueda (en formato ISO 8601).
        status (str): Estado del cobro (ACTIVE, COMPLETED, EXPIRED).

    Returns:
        dict: Un diccionario con los detalles de los cobros encontrados.
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

def accountslist(appid:str) -> dict:
    """
    Obtiene una lista de cuentas asociadas a la aplicación.

    Args:
        appid (str): ID de la aplicación utilizado para la autorización.

    Returns:
        dict: Un diccionario con los detalles de las cuentas encontradas.
    """
    conn = http.client.HTTPSConnection("api.openpix.com.br")
    headers = { 'Authorization': appid }
    conn.request("GET", "/api/v1/account/", headers=headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()

    return dict(json.loads((data.decode("utf-8"))))

def accounts(appid:str, accountId:str) -> dict:
    """
    Obtiene detalles de una cuenta específica mediante su ID.

    Args:
        appid (str): ID de la aplicación utilizado para la autorización.
        accountId (str): ID de la cuenta.

    Returns:
        dict: Un diccionario con los detalles de la cuenta.
    """
    conn = http.client.HTTPSConnection("api.openpix.com.br")
    headers = { 'Authorization': appid }
    conn.request("GET", f"/api/v1/account/{accountId}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()

    return dict(json.loads((data.decode("utf-8"))))

