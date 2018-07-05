from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers
from Data_Conversion.position_of_pieces import position_dic


'''
Since the rules of the pawn movement and the movement of capturing is so different, I
decided to make two different functions that get called depending if a capturing is happeing
'''
class pawn_movement():

    def __init__(self, position_piece):

        #Initializes commonly used values
        self.piece = position_dic[str(position_piece)]

    def positive(self, position_piece, pos_chess):
        #Checks to see if the piece position is one more than the start
        if int(str(position_piece)[1]) + 1 == int(str(pos_chess)[1]):
            #Checks to see if the letters are the same
            if int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
                return "True"
            elif int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) -1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]) or int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) + 1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
                return "Capture"
    def negative(self, position_piece, pos_chess):
        #Checks to see if the piece position is one less than the start
        if int(str(position_piece)[1]) -1 == int(str(pos_chess)[1]):
            #Checks to see if the letters are the same

            if int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
                return "True"
            elif int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) -1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]) or int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) + 1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
                return "Capture"

    def pawn(self, position_piece, pos_chess):
        
        '''
        The rules I used to determine the movement of the pawn, when regular are as follows:

        1. Check the color of the pawn
            A. If White, then the number has the go up by one
            B. If black, then the number has to go down by one
                I. this makes it so the pawn can only move one square at a time

        2. Check if the letter stayed the same
            A. This makes it so the pawn cannot move to the side, but only stay in it's lane

        3. Check the starting location of the pawn, to see if the pawn can move up by two
            A. This allows the pawn to move up two on it's first move
        '''
        pawn = pawn_movement(position_piece)
        if str(self.piece)[0] == 'W':
            if pawn.positive( position_piece, pos_chess) == "True":
                return True

            else:
                #Checks to see if the pawn is in it's starting location
                #If it is, then it has the right to go two spaces
                if str(position_piece) == "a2" or str(position_piece) == "b2" or str(position_piece) == "c2" or str(position_piece) == "d2" or str(position_piece) == "e2" or str(position_piece) == "f2" or str(position_piece) == "g2" or str(position_piece) == "h2":
                    if int(str(position_piece)[1]) + 2 == int(str(pos_chess)[1]):
                        if int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
                            return True
        else:

            if pawn.negative( position_piece, pos_chess) == "True":
                return True

            else:
                #Checks to see if the pawn is in it's starting location
                #If it is, then it has the right to go two spaces
                if str(position_piece) == "a7" or str(position_piece) == "b7" or str(position_piece) == "c7" or str(position_piece) == "d7" or str(position_piece) == "e7" or str(position_piece) == "f7" or str(position_piece) == "g7" or str(position_piece) == "h7":
                    if int(str(position_piece)[1]) - 2 == int(str(pos_chess)[1]):
                        if int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
                            return True

    def pawn_capture(self, position_piece, pos_chess):
        '''
        The rules I used to determine the movement of a pawn when in "capturing mode":

        1. Check the Color
        2. See if the number added one
        3. See if the letter added one
        '''
        pawn = pawn_movement(position_piece)
        if str(self.piece)[0] == 'W':

            #Calls the functions
            if pawn.positive( position_piece, pos_chess) == "Capture":
                return True
        else:
            #Calls the functions
            if pawn.negative( position_piece, pos_chess) == "Capture":
                return True
