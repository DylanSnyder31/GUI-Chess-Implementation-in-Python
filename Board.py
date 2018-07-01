from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

from position_of_mouse import find_position

class Scatter_Text_widget(FloatLayout):


    def on_touch_down(self, touch):
        position = find_position()
        pos_chess = position.chess_position(touch.pos)
        print(pos_chess)

    def on_touch_up(self, touch):
        position = find_position()
        pos_chess = position.chess_position(touch.pos)
        print(pos_chess)

#Builds the App
class window(App):
    def build(self):
        return Scatter_Text_widget()
