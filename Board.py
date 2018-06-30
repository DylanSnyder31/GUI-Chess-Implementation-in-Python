from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.app import App

from position_of_mouse import find_position

class board_setup(Screen):

    def on_mouse_pos(self, pos):
        #This function gets the position of the mouse, in chessboard labels
        position = find_position()
        print(position.chess_position(pos))


    def touched(self, id):
        print(id)


    def release(self):
        print("RRR")



    Window.bind(mouse_pos = on_mouse_pos)


#Builds the App
class window(App):
    def build(self):
        return board_setup()
