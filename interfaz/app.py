from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.lang import Builder

class IncrediblyCrudeClock(MDLabel):
    a = NumericProperty(120)  # seconds

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)
        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "FINISHED"
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

    def on_a(self, instance, value):
        mins, secs = divmod(value, 60)
        hour, mins = divmod(mins, 60) 
        self.text = "%d:%02d:%02d" % (hour, mins, secs) 

class TimeApp(MDApp):
    def build(self):
        kv = Builder.load_file('btn.kv')
        #crudeclock = IncrediblyCrudeClock()
        #crudeclock.start()
        return kv

if __name__ == "__main__":
    TimeApp().run()
