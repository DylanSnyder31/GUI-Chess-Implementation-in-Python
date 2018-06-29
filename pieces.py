from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image



class white_pieces(Button, Image):
    def yes(self):
        print("CLICK")
    def no(self):
        print("NOPE")

class pieces(App):
    def build(self):
        return white_pieces()

pieces().run()
