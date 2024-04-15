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

