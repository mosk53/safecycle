import kivy
import kivymd
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

Window.size =[390,844]



class myApp(MDApp):
    def build(self):
        return FloatLayout()
 
if __name__ == '__main__':
    myApp().run()