import time, threading
from lib import pixadd
import flet as ft


class Countdown(ft.UserControl):
    def __init__(self, seconds, page=None,
                 pixid=None, appid=None, 
                 check_Trastion=False,
                 time=1200
                 ):
        super().__init__()
        self.seconds = seconds
        self.check_Trastion = check_Trastion
        self.pixid   = pixid
        self.appid   = appid
        self.time = time
        print(self.time)
        


    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            hour, min = divmod(mins, 60) 
            self.countdown.value = "%d:%02d:%02d" % (hour, min, secs) 
            self.update()
            time.sleep(1)
            self.seconds -= 1
            #print(secs, end='\r')
            if self.check_Trastion:
                self.check()
                if type(self.time) != int:
                    self.time = self.time[:-2]
                    self.time = int(self.time)

    def check(self):
       status = pixadd.get_cob(self.appid,self.pixid )
       status = status['charge']['status']
       

       if status == 'ACTIVE':
          print('esperado pagamento', end='\r')
          if self.countdown.value == '00:01':
             self.page.go(f"/")
              

       else:
          print('pago! pago!', end='\r')
          self.page.go(f"/carga/{self.time}")

           

    def build(self):
        self.countdown = ft.Text(size=70)
        return self.countdown
