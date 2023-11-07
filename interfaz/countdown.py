import time, threading
from lib import pixadd
import flet as ft


class Countdown(ft.UserControl):
    def __init__(self, seconds, page=None,
                 pixid=None, appid=None, 
                 check_Trastion=False):
        super().__init__()
        self.seconds = seconds
        self.check_Trastion = check_Trastion
        self.pixid   = pixid
        self.appid   = appid


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
            #print(secs, end='\r')
            if self.check_Trastion:
                self.check()

    def check(self):
       status = pixadd.get_cob(self.appid,self.pixid )
       status = status['charge']['status']
       

       if status == 'ACTIVE':
          print('esperado pagamento', end='\r')
          if self.countdown.value == '00:01':
             self.page.go(f"/")
              

       else:
          print('pago! pago!', end='\r')
          self.page.go(f"/carga/1200")

           

    def build(self):
        self.countdown = ft.Text(size=70)
        return self.countdown
