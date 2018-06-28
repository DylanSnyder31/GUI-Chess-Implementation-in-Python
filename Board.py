from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.config import Config
from kivy.core.window import Window


class main_window(Screen):
    pass

class filename(App):
    def build(self):
        return main_window()



if __name__ == "__main__":
    width_of_board = 800
    height_of_board = 800
    #Set the Hight and Width of the App
    Config.set('graphics', 'width', str(width_of_board))
    Config.set('graphics', 'height', str(height_of_board))

    #Make the App non-resizable
    Config.set('graphics', 'resizable', '0')
    Config.write()
    #Make the top windows bar go away
    #Window.borderless = True
    filename().run()
