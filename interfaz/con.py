import time

def temporizador_con_contador(segundos):
    print(f"Temporizador configurado para {segundos} segundos.")
    for i in range(1, segundos + 1):
        time.sleep(1)  # Espera 1 segundo
        print(f"Segundos transcurridos: {i}")
    print("¡Tiempo expirado! El temporizador ha terminado.")

# Ejemplo de uso:
segundos = int(input("Ingrese la cantidad de segundos para el temporizador: "))
temporizador_con_contador(segundos)
