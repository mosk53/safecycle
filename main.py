import kivy
import kivymd
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix.screen import MDScreen

Window.size =[390,844]

class main_screen(MDScreen):
    pass

class search_screen(MDScreen):
    pass

class myApp(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(main_screen(name='main_s'))
        sm.add_widget(search_screen(name='search_s'))
        return sm
 
if __name__ == '__main__':
    myApp().run()