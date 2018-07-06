#Import from Kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

#Import files from another folder
from Data_Conversion.position_of_mouse import find_position
from Data_Conversion.position_of_pieces import position_dic
from Data_Conversion.chess_coords_to_real_coords import convert_coordinates
from Data_Conversion.difference_for_letter import promotion_piece

#Import a file from the same folder
from valid_move import is_valid_move


class Scatter_Text_widget(Screen):
    '''
    This is the main function that holds the app together, and takes input from many other files
    '''

    def __init__(self, **kwargs):
        #Initializes the class with variables
        super(Scatter_Text_widget, self).__init__(**kwargs)

        #Initializes commonly used variables
        self.position = find_position()
        self.position_piece = position_dic

    def on_touch_down(self, touch):
        #This function gets called when the mouse is pressed, Anywhere on the board
        #Only really generates the data to be used later

        res = super(Scatter_Text_widget, self).on_touch_down(touch)
        #This makes sure the labels keep their Scatter Property and the mouse input can be obtained

        if res:

            #Gets the chess coord of where the mouse pressed
            pos_chess = self.position.chess_position(touch.pos)

            #Saves the input to a text file
            #Probably a bad way to do this, especially for security concerns
            clicked_input = [pos_chess,self.position_piece[str(pos_chess)]]

            #Writes twrites the input into the file
            with open('Data_Conversion\saved_input.txt', 'w') as f:
                f.write(str(clicked_input))

    def on_touch_up(self, touch):
        #This function gets called when the mouse is released

        res = super(Scatter_Text_widget, self).on_touch_up(touch)
        #Makes sure Scatter properties and touch input work alligned
        if res:
            #Define a variable
            conversion = convert_coordinates

            #Gets the position of the mouse, and translates it into a chess corrd
            #Saves the variable with self, so the Pawn Promotion can access this data
            self.pos_chess = self.position.chess_position(touch.pos)

            #opens the text file, to get the previous data
            with open('Data_Conversion\saved_input.txt', 'r') as f:
                list_of_previous_data= f.read()
            f.close()

            #OLD DATA; for the chess corrdinate
            chess_position_numerical = str(str(list_of_previous_data[2]) + str(list_of_previous_data[3]))
            self.chess_position_numerical = chess_position_numerical

            #This is the piece that was moved, taken from the text file
            self.piece_that_moved = ""
            index = 8
            #Loop is to get the piece that moved, looping through each letter
            while index != len(list_of_previous_data) -2:
                self.piece_that_moved += str(list_of_previous_data[index])
                index += 1

            '''
            Checks with another python file to see if the move was valid or not, against all the rules of Chess
            '''
            st = is_valid_move()
            valid_or_not = st.main(chess_position_numerical, self.position_piece, self.pos_chess, self.piece_that_moved)

            #IF THE MOVE WAS VALID
            if valid_or_not == "True":
                #Move the piece to the location
                self.ids[self.piece_that_moved].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])

                #Updates the Dictionary of all the piece locations
                position_dic[str(chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = str(self.piece_that_moved)

            elif valid_or_not == "True, Captured":
                #If the move was valid, and a capture occured
                piece_occupied = str(self.position_piece[self.pos_chess])

                #Deletes the piece that was captured
                self.ids[piece_occupied].pos = (1000,1000)

                #Moves the piece in play
                self.ids[self.piece_that_moved].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])

                #Updates Dictionary
                position_dic[str(chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = str(self.piece_that_moved)

            elif valid_or_not == "Castle":
                #Move the piece to the location
                self.ids[self.piece_that_moved].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])

                #Checks to see what one of four possible events could have happened
                if str(self.pos_chess) == 'g1':
                    #Updates the position of the Rook
                    self.ids['Right White Rook'].pos = (conversion.to_number()['f1'][0], conversion.to_number()['f1'][1])
                    position_dic['h1'] = 'None'
                    position_dic['f1'] = 'Right White Rook'

                if str(self.pos_chess) == 'c1':
                    #Updates the position of the Rook
                    self.ids['Left White Rook'].pos = (conversion.to_number()['d1'][0], conversion.to_number()['d1'][1])
                    position_dic['a1'] = 'None'
                    position_dic['d1'] = 'Left White Rook'

                if str(self.pos_chess) == 'g8':
                    #Updates the position of the Rook
                    self.ids['Right Black Rook'].pos = (conversion.to_number()['f8'][0], conversion.to_number()['f8'][1])
                    position_dic['h8'] = 'None'
                    position_dic['f8'] = 'Right Black Rook'

                if str(self.pos_chess) == 'c8':
                    #Updates the position of the Rook
                    self.ids['Left Black Rook'].pos = (conversion.to_number()['d8'][0], conversion.to_number()['d8'][1])
                    position_dic['a8'] = 'None'
                    position_dic['d8'] = 'Left Black Rook'

                #Updates the Dictionary the king's location
                position_dic[str(chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = str(self.piece_that_moved)

            elif valid_or_not == "New_Piece":
                #Pawn's Promotion
                sc = Scatter_Text_widget()

                if self.piece_that_moved[0] == "W":
                    #If the piece being promoted is White

                    '''
                    Adds four buttons the user can touch, symbolizing what piece the user will want to promote to '''

                    content = Button(id = 'Queen Promotion', background_normal='Pictures\White_Queen.png', size = (60,60), pos = (410,300))
                    content1 = Button(id = 'Rook Promotion', background_normal='Pictures\white_rook.png', size = (60,60), pos = (307.5,400))
                    content2 = Button(id = 'Bishop Promotion', background_normal='Pictures\white_Bishop.png', size = (60,60), pos = (307.5,300))
                    content3 = Button(id = 'Knight Promotion',  background_normal='Pictures\white_horse.png', size = (60,60), pos = (410,400))

                else:
                    #If the piece is Black

                    #Adds four buttons, but this time in Black, Not white
                    content = Button(id = 'Queen Promotion', background_normal='Pictures/black_Queen.png', size = (60,60), pos = (410,300))
                    content1 = Button(id = 'Rook Promotion', background_normal='Pictures/black_rook.png', size = (60,60), pos = (307.5,400))
                    content2 = Button(id = 'Bishop Promotion', background_normal='Pictures/black_Bishop.png', size = (60,60), pos = (307.5,300))
                    content3 = Button(id = 'Knight Promotion',  background_normal='Pictures/black_horse.png', size = (60,60), pos = (410,400))

                #Adds a floatlayout to the popup
                float = FloatLayout()

                #Adds the buttons the the layout that were just defined based on the color of the promoted piece
                float.add_widget(content)
                float.add_widget(content1)
                float.add_widget(content2)
                float.add_widget(content3)

                #Creates the popup, with the FLoatLayout as the content, and moves it to a location the user will not see, so the
                #popup will not be visable, because the popup does not look aesthetically pleasing
                popup = Popup(content=float, size_hint=(None, None), size=(120, 160), auto_dismiss=False, pos_hint={'x': 10.0, 'y':10.0})

                #Binds all of the buttons the the same funtion, and to close the popup
                content.bind(on_press = self.promotion, on_release=popup.dismiss)
                content1.bind(on_press = self.promotion, on_release=popup.dismiss)
                content2.bind(on_press = self.promotion, on_release=popup.dismiss)
                content3.bind(on_press = self.promotion, on_release=popup.dismiss)

                #Opens the popup so the GUI will display it
                popup.open()

                #Deletes an array of corrdinates
                del promotion_piece[:]

            else:
                #If the move was not valid

                #Places the piece in the beggining location, and not updating the Dictionary
                self.ids[self.piece_that_moved].pos = (conversion.to_number()[chess_position_numerical][0], conversion.to_number()[chess_position_numerical][1])




    def promotion(self, obj):
        conversion = convert_coordinates

        #Appends the corrdinates to an array
        promotion_piece.append(obj.pos[0])
        promotion_piece.append(obj.pos[1])

        #'Deletes' the pawn
        self.ids[self.piece_that_moved].pos = (10000,1000)

        #Declare what piece was occupied in the location (If a pawn captures to be promoted)
        piece_occupied = str(self.position_piece[self.pos_chess])

        #If the square was not empty
        if piece_occupied != "None":
            #Delete that piece
            self.ids[piece_occupied].pos = (1000,1000)

        #If the pawn was white
        if self.piece_that_moved[0] == "W":

            if promotion_piece == [410,300]:
                #Turns the pawn into a Queen, Adds the Queen to the dictionary
                self.ids['Whire Queen'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Whire Queen'

            elif promotion_piece == [307.5, 400]:
                #Turns the pawn into a Rook, Adds the Rook to the dictionary
                self.ids['Ledt White Rook'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt White Rook'

            elif promotion_piece == [307.5, 300]:
                #Turns the pawn into a Bishop, Adds the Bishop to the dictionary
                self.ids['Ledt White Bishop'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt White Bishop'

            elif promotion_piece == [410, 400]:
                #Turns the pawn into a Knight, Adds the Knight to the dictionary
                self.ids['Ledt White Knight'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt White Knight'

        else:
            #If the pawn is BLACK
            #Does the same thing, but changes the color of the piece and the ID of the piece

            if promotion_piece == [410,300]:
                #Turns the pawn into a Queen, Adds the Queen to the dictionary
                self.ids['Block Queen'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Block Queen'

            elif promotion_piece == [307.5, 400]:
                #Turns the pawn into a Rook, Adds the Rook to the dictionary
                self.ids['Ledt Black Rook'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt Black Rook'

            elif promotion_piece == [307.5, 300]:
                #Turns the pawn into a Bishop, Adds the Bishop to the dictionary
                self.ids['Ledt Black Bishop'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt Black Bishop'

            elif promotion_piece == [410, 400]:
                #Turns the pawn into a Knight, Adds the Knight to the dictionary
                self.ids['Ledt Black Knight'].pos = (conversion.to_number()[self.pos_chess][0], conversion.to_number()[self.pos_chess][1])
                position_dic[str(self.chess_position_numerical)] = 'None'
                position_dic[str(self.pos_chess)] = 'Ledt Black Knight'

#Builds the App
class window(App):
    def build(self):
        return Scatter_Text_widget()
