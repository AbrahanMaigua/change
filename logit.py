import time

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
pago = 'ACTIVE'
aux = 0
while True:
    start = next(cronometro(inicio))
    print("Tiempo transcurrido:",start, pago, end="\r")

    if start == stop:
       if pago == 'ACTIVE':
            pago = 'COMPLETED'

    if  pago == 'COMPLETED' and aux == 0 :
       inicio = time.time()
       aux = 1
          

