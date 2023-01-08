import kivy
import kivymd
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.recycleview import RecycleView

Window.size =[390,844]

class login_screen(MDScreen):
    pass

class booking_screen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(RV(rv_id='rv'))
        self.ids.rv.data = [{'text': str(x)} for x in range(20)]
    pass

class RV(RecycleView):
    def __init__(self, rv_id, **kwargs):
        super().__init__(**kwargs)
        self.rv_id = rv_id

    pass


class screen_manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition()
        self.add_widget(login_screen(name='login_s'))
        self.add_widget(booking_screen(name='booking_s'))
    pass

class myApp(MDApp):

    def build(self):
        return screen_manager()
 
if __name__ == '__main__':
    myApp().run()