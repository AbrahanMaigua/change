import time
from lib.pixadd import *
from dotenv import dotenv_values
import os

def cronometro(inicio):
   
    while True:
        tiempo_pasado = time.time() - inicio
        minutos, segundos = divmod(tiempo_pasado, 60)
        horas, minutos = divmod(minutos, 60)
        tiempo_formateado = "{:02}:{:02}:{:02}".format(int(horas), int(minutos), int(segundos))
        time.sleep(1)
        yield tiempo_formateado  # Devuelve hora formatada
      

inicio = time.time()
stop = '00:00:10'

# Get the current date and time in ISO 8601 format
#YYYY-MM-DDTHH:MM:SS.ssssssZ
current_time_iso8601 = datetime.datetime.now().isoformat()
config = dotenv_values(".env") 
appid  = config['APP_ID']
reset  = False
cob = create_cob(appid, 50, 'test #2 de pago real')
status = 'ACTIVE'

while True:
    start  = next(cronometro(inicio))
    print("Tiempo transcurrido: ",start, status, end="\r")

    if status == 'ACTIVE':
        cobr   = get_cob(appid, cob[1] )
        print(cobr['charge']['qrCodeImage'])
        os.system('clear')
        time.sleep(10)
        status = cobr.get('charge')['status']
        reset  = True

    if  status == 'COMPLETED':
        if reset != False:
            inicio = time.time()
            reset  = False

        
        if start == stop:
         break
            

