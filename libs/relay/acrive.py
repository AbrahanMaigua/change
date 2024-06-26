
try:
    import RPi.GPIO as GPIO
    class control_relay():
        def __init__(self) -> None:
            self.relay_ch = 21
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
 
        def start(self):

           
            GPIO.setup(self.relay_ch, GPIO.OUT)
            GPIO.output(self.relay_ch, GPIO.LOW)

        def stop(self):

            GPIO.output(self.relay_ch, GPIO.HIGH)
            GPIO.cleanup()


except ModuleNotFoundError as error:
    

    class control_relay():

        def __init__(self) -> None:
            self.relay_ch = 21
            
        def start(self):
           pass

        def stop(self):
            pass

control_relay().start()
