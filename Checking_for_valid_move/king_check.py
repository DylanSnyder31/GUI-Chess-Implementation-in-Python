from Data_Conversion.position_of_pieces import position_dic
from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers

'''
Check to see if the king is currently in check



	if yes, at the end of every move check again
		if still in check, return FALSE and repeat loop

		if not in check, end loop and return TRUE




How to check if in check:

ROOK:

Check to the left/right
Check up/down

BISHOP:

Check up/down/left/right

KNIGHT:

    CHECK THE FOUR SPOTS IT COULD BE

QUEEN:
CHECK FoR A BISHOP AND A rook



the King is the origin POint
    CHECK each squre for each peice:
        if another piece 'pops up' before the direction, end the
            process becausre that means it is blocked


'''

class end_game():

    def __init__(self, turn):
        '''
        Gets the Position of the King
        '''
        #Checks to see what player's turn it is, and decides the king's ID based on that Data
        if turn == "W":
            king_ID = "White King"
            #What way the pawns are deadly to the king
            self.check_for_pawns = "Up"
        else:
            king_ID = "Black King"
	
            #What way the pawns are deadly to the king
            self.check_for_pawns = "Down"

        #Iterates through the board to determine where the king is
        for key, value in position_dic.items():
            if str(value) == king_ID:

                #Assigns this variabel to the square where the king is present
                self.king_position = str(key)

        self.number_positive = int(self.king_position[1]) + 1
        self.number_negative = int(self.king_position[1]) - 1
        self.player_turn = turn
        self.numeric_value_positive = str(int(dictionar_of_letters_to_numbers[self.king_position[0]]) + 1)
        self.numeric_value_negative = str(int(dictionar_of_letters_to_numbers[self.king_position[0]]) - 1)

        self.number = self.king_position[1]
        self.letter = self.king_position[0]

    def rook(self):
        '''
        CHck if to the left/right wall
        check if to the top/bottom wall
        '''
        numberic = int(self.numeric_value_negative)
        if self.numeric_value_negative != '0':
            endpoint = 'a' + str(self.number)
            for key, value in dictionar_of_letters_to_numbers.items():
                if int(value) == numberic:
                    letter = str(key)
            while position_dic[str(letter) + str(self.number) ] == 'None' or str(letter) + str(self.number) == endpoint:
                numberic -= 1
                for key, value in dictionar_of_letters_to_numbers.items():
                    if str(value) == numberic:
                        letter = str(key)
            if self.player_turn == 'W':
                print("HERE")
                if position_dic[str(letter) + str(self.number) ][0] == "L":
                    if position_dic[str(letter) + str(self.number) ][5] == "B":
                        if position_dic[str(letter) + str(self.number) ][11] == 'R':
                            return "False"
                        else:
                            pass
                    else:
                        pass

                elif position_dic[str(letter) + str(self.number) ][0] =="R":
                    if position_dic[str(letter) + str(self.number) ][6] == "B":
                        if position_dic[str(letter) + str(self.number) ][12] == 'R':
                            return "False"

            else:

                if position_dic[str(letter) + str(self.number) ][0] == "L":
                    if position_dic[str(letter) + str(self.number) ][5] == "W":
                        if position_dic[str(letter) + str(self.number) ][11] == 'R':
                            return "False"
                elif position_dic[str(letter) + str(self.number) ][0] =="R":
                    if position_dic[str(letter) + str(self.number) ][6] == "W":
                        if position_dic[str(letter) + str(self.number) ][12] == 'R':

                            return "False"


        if self.numeric_value_positive != '9':
            '''
            CHECK to thE RIGHt
            '''
            pass
        if self.number_positive != 9:
            '''
            CHeck going DOWN
            '''
            pass
        if self.number_negative != 0:
            '''
            Check going up
            '''
            pass

    def pawn(self):

        if self.check_for_pawns == "Up":
            '''
            If White
            '''
            if self.numeric_value_negative != '0':
                for key, value in dictionar_of_letters_to_numbers.items():
                    if str(value) == self.numeric_value_negative:
                        letter = str(key)
                square = str(letter) + str(self.number_positive)

            if self.numeric_value_positive != '9':
                for key, value in dictionar_of_letters_to_numbers.items():
                    if str(value) == self.numeric_value_positive:
                        letter = str(key)
                square = str(letter) + str(self.number_positive)

            if str(position_dic[square][0]) == "B" and str(position_dic[square][6]) == 'P':
                #A Pawn is in that location
                return "False"


        if self.check_for_pawns == "Down":
            '''
            If black
            '''
            if self.numeric_value_negative != '0':
                for key, value in dictionar_of_letters_to_numbers.items():
                    if str(value) == self.numeric_value_negative:
                        letter = str(key)
                square = str(letter) + str(self.number_negative)

            if self.numeric_value_positive != '9':
                for key, value in dictionar_of_letters_to_numbers.items():
                    if str(value) == self.numeric_value_positive:
                        letter = str(key)
                square = str(letter) + str(self.number_negative)

            if str(position_dic[square][0]) == "W" and str(position_dic[square][6]) == 'P':
                #A Pawn is in that location
                return "False"



    def in_check(self):
        check = end_game
        if check.pawn(self) != "False":
            if check.rook(self) !="False":
                return "True"
