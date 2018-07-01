from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from position_of_mouse import find_position
from kivy.uix.floatlayout import FloatLayout

class Scatter_Text_widget(FloatLayout):
    pass



#Builds the App
class window(App):
    def build(self):
        return Scatter_Text_widget()
