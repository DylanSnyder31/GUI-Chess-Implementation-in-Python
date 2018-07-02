from kivy.app import App
from kivy.uix.screenmanager import Screen

from position_of_mouse import find_position
from position_of_pieces import position_dic
from chess_coords_to_real_coords import convert_coordinates
from valid_move import is_valid_move

class Scatter_Text_widget(Screen):

    def __init__(self, **kwargs):
        super(Scatter_Text_widget, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        res = super(Scatter_Text_widget, self).on_touch_down(touch)

        if res:
            position = find_position()
            #Gets the chess coord of where the mouse pressed
            pos_chess = position.chess_position(touch.pos)

            position_piece = position_dic

            tup = [pos_chess,position_piece[str(pos_chess)]]
            #Writes the chess coord and the piece that was pressed in a text file
            with open('test.txt', 'w') as f:
                f.write(str(tup))

    def on_touch_up(self, touch):
        res = super(Scatter_Text_widget, self).on_touch_up(touch)

        if res:
            position = find_position()
            #Gets the position of the mouse, and translates it into a chess corrd
            pos_chess = position.chess_position(touch.pos)

            position_piece = position_dic
            conversion = convert_coordinates

            with open('test.txt', 'r') as f:
                lisr= f.read()
            f.close()
            #This is where the mouse was pressed, in a chess coord
            chess_position_numerical = str(str(lisr[2]) + str(lisr[3]))

            #This gets the piece that was moved, and stores it in string format
            piece_that_moved = ""
            index = 8
            while index != len(lisr) -2:
                piece_that_moved += str(lisr[index])
                index += 1



            #Checks to see if the square is currently occupied
            st = is_valid_move()
            yes = st.main(chess_position_numerical, position_piece, pos_chess, piece_that_moved)

            if yes == "True":
                self.ids[piece_that_moved].pos = (conversion.to_number()[pos_chess][0], conversion.to_number()[pos_chess][1])


                position_dic[str(chess_position_numerical)] = 'None'
                position_dic[str(pos_chess)] = str(piece_that_moved)

            elif yes == "True, Captured":
                piece_occupied = str(position_piece[pos_chess])
                self.ids[piece_occupied].pos = (1000,1000)
                self.ids[piece_that_moved].pos = (conversion.to_number()[pos_chess][0], conversion.to_number()[pos_chess][1])


                position_dic[str(chess_position_numerical)] = 'None'
                position_dic[str(pos_chess)] = str(piece_that_moved)
            else: #if yes == "FALSE"
                self.ids[piece_that_moved].pos = (conversion.to_number()[chess_position_numerical][0], conversion.to_number()[chess_position_numerical][1])



#Builds the App
class window(App):
    def build(self):
        return Scatter_Text_widget()
