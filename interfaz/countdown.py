import flet as ft
import time, threading

class Countdown(ft.UserControl):
    def __init__(self, seconds, page ):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            time.sleep(1)
            self.seconds -= 1
            print(secs, end='\r')
            

    def build(self):
        self.countdown = ft.Text()
        return self.countdown
