<<<<<<< HEAD
import RPi.GPIO as GPIO
import os
os.getcwd()
=======

try:
    import RPi.GPIO as GPIO
    class control_relay():
        def __init__(self) -> None:
            self.relay_ch = 21
            
        def start(self):

            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)

            GPIO.setup(self.relay_ch, GPIO.OUT)
            GPIO.output(self.relay_ch, GPIO.LOW)

        def stop(self):

            GPIO.output(self.relay_ch, GPIO.HIGH)
            GPIO.cleanup()

>>>>>>> 44229fab7276430a9ea22cbe55cc3da6d4336fdc

except ModuleNotFoundError as error:
    

    class control_relay():

        def __init__(self) -> None:
            self.relay_ch = 21
            
        def start(self):
           pass

        def stop(self):
            pass
