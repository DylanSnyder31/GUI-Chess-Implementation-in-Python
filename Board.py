from kivy.app import App
from kivy.uix.screenmanager import Screen

from Data_Conversion.position_of_mouse import find_position
from Data_Conversion.position_of_pieces import teams_turn
from Data_Conversion.position_of_pieces import position_dic

from Data_Conversion.chess_coords_to_real_coords import convert_coordinates
from valid_move import is_valid_move

class Scatter_Text_widget(Screen):

    def __init__(self, **kwargs):
        #Initializes the class with variables
        super(Scatter_Text_widget, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        #This function gets called when the mouse is pressed

        res = super(Scatter_Text_widget, self).on_touch_down(touch)
        #This makes sure the labels keep their Scatter Property and the mouse input can be obtained

        if res:
            position_piece = position_dic
            position = find_position()

            #Gets the chess coord of where the mouse pressed
            pos_chess = position.chess_position(touch.pos)

            #Saves the input to a text file
            #Probably a bad way to do this, especially for security concerns
            clicked_input = [pos_chess,position_piece[str(pos_chess)]]

            #Writes twrites the input into the file
            with open('Data_Conversion\saved_input.txt', 'w') as f:
                f.write(str(clicked_input))

    def on_touch_up(self, touch):
        #This function gets called when the mouse is released

        res = super(Scatter_Text_widget, self).on_touch_up(touch)
        #Makes sure Scatter properties and touch input work alligned
        if res:
            position = find_position()
            position_piece = position_dic
            conversion = convert_coordinates

            #Gets the position of the mouse, and translates it into a chess corrd
            pos_chess = position.chess_position(touch.pos)

            #opens the text file, to get the previous data
            with open('Data_Conversion\saved_input.txt', 'r') as f:
                list_of_previous_data= f.read()
            f.close()

            #OLD DATA; for the chess corrdinate
            chess_position_numerical = str(str(list_of_previous_data[2]) + str(list_of_previous_data[3]))

            #This is the piece that was moved, taken from the text file
            piece_that_moved = ""
            index = 8
            while index != len(list_of_previous_data) -2:
                piece_that_moved += str(list_of_previous_data[index])
                index += 1

            '''
            Checks with another python file to see if the move was valid or not, against all rules of Chess
            '''
            st = is_valid_move()
            valid_or_not = st.main(chess_position_numerical, position_piece, pos_chess, piece_that_moved)

            #IF THE MOVE WAS VALID
            if valid_or_not == "True":
                #Move the piece to the location
                self.ids[piece_that_moved].pos = (conversion.to_number()[pos_chess][0], conversion.to_number()[pos_chess][1])

                #Updates the Dictionary of all the piece locations
                position_dic[str(chess_position_numerical)] = 'None'
                position_dic[str(pos_chess)] = str(piece_that_moved)

            elif valid_or_not == "True, Captured":
                #If the move was valid, and a capture occured
                piece_occupied = str(position_piece[pos_chess])

                #Deletes the piece that was captured
                self.ids[piece_occupied].pos = (1000,1000)
                #Moves the piece in play
                self.ids[piece_that_moved].pos = (conversion.to_number()[pos_chess][0], conversion.to_number()[pos_chess][1])

                #Updates Dictionary
                position_dic[str(chess_position_numerical)] = 'None'
                position_dic[str(pos_chess)] = str(piece_that_moved)

            else:
                #If the move was not valid

                #Places the piece in the beggining location
                self.ids[piece_that_moved].pos = (conversion.to_number()[chess_position_numerical][0], conversion.to_number()[chess_position_numerical][1])

#Builds the App
class window(App):
    def build(self):
        return Scatter_Text_widget()
