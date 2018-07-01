from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

from position_of_mouse import find_position

class Scatter_Text_widget(FloatLayout):
    def on_mouse_pos(self, pos):
        #This function gets the position of the mouse, in chessboard labels
        position = find_position()
        pos_chess = position.chess_position(pos)
        print(pos_chess)


    Window.bind(mouse_pos = on_mouse_pos)



#Builds the App
class window(App):
    def build(self):
        return Scatter_Text_widget()
