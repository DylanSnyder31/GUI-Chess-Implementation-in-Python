
from kivy.uix.screenmanager import Screen
from kivy.config import Config
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout



class board_setup(Screen):
    pass


class window(App):
    def build(self):
        return board_setup()


if __name__ == "__main__":
    width_of_board = 820
    height_of_board = 800

    #Set the Hight and Width of the App
    Config.set('graphics', 'width', str(width_of_board))
    Config.set('graphics', 'height', str(height_of_board))

    #Make the App non-resizable
    Config.set('graphics', 'resizable', '0')
    Config.write()

    #Make the top windows bar go away
    Window.borderless = True

    #Runs the
    window().run()
