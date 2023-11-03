import threading
import time

class Temporizador:
    def __init__(self, segundos):
        self.seconds = segundos
        self.running = True
        self.th = threading.Thread(target=self.update_timer, daemon=True)
        self.th.start()

    def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            tiempo_formateado = "{:02d}:{:02d}".format(mins, secs)
            print(tiempo_formateado)
            time.sleep(1)
            self.seconds -= 1

    def stop_timer(self):
        self.running = False


import flet as ft
import time, threading

class Countdown(ft.UserControl):
    def __init__(self, seconds, page):
        super().__init__()
        self.seconds = seconds
        self.page = page
        self.running = True
       


    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.e.value = "{:02d}:{:02d}".format(mins, secs)
            self.page.update()
            time.sleep(1)
            self.seconds -= 1

    def build(self, size=70):
        self.e = ft.Text('rr',size=size)
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start() 
        
        return self.e

