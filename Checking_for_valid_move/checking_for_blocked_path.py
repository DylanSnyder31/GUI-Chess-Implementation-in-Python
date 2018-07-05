from Data_Conversion.position_of_pieces import position_dic
from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers

'''
This file is to make sure the path is clear for the pieces to move.
This file only includes the Rook and the Bishop
    A. The knight isn't here because it is allowed to jump over other pieces
    B. The King isn't here because it can only move on sqaure (unless castling)
    C. The pawn isn't here for the same reason as the king, it can only move one square
    D. THe Queen isn't here because it will steal the code for the Bishop and Rook
'''

class is_path_blocked():

    class path_rook():
        '''
        This class is specific to the Rook, and has two functions,
        number_same is used when the rook is played to the left or right
        letter_same is used when the rook is played up or down
        '''
        def __init__(self, position_piece, pos_chess):
            #Initializes commonly used variable in the two functions
            self.number_that_stayed_the_same = str(pos_chess)[1]

            #These are numeric representations of the letters on the chess coordinates
            self.letter_number_of_start = dictionar_of_letters_to_numbers[str(pos_chess)[0]]
            self.letter_number_of_end =  dictionar_of_letters_to_numbers[str(position_piece)[0]]

            self.letter_that_stayed_the_same = str(pos_chess)[0]
            self.number_of_start = int(str(pos_chess)[1])
            self.number_of_end =  int(str(position_piece)[1])

            self.blocked = "No"

        def number_same(self, position_piece, pos_chess):

            if dictionar_of_letters_to_numbers[str(pos_chess)[0]] -  dictionar_of_letters_to_numbers[str(position_piece)[0]] >= 1:
                #This is for when the Rook is moved to the right

                self.letter_number_of_end += 1
                #Loops through every square the rook went past
                while self.letter_number_of_end != self.letter_number_of_start:
                    for key, value in dictionar_of_letters_to_numbers.items():
                        if value == self.letter_number_of_end:
                            new_number = key

                    #New_number is a square the Rook went over to get to it's finishing point
                    new_number = str(str(new_number)[0]) + str(self.number_that_stayed_the_same)

                    #Checks to make sure the square is empty
                    if position_dic[str(new_number)] != "None":
                        #If it is not empty then blocked will equal "Yes" to make sure that the move will get flagged as FALSE
                        self.blocked = "Yes"

                    #Iterates through the loop
                    self.letter_number_of_end += 1

            elif dictionar_of_letters_to_numbers[str(pos_chess)[0]] -  dictionar_of_letters_to_numbers[str(position_piece)[0]] < 0:
                #This is for when the Rook is moved to the left (almost the same code, but has some key differences)

                self.letter_number_of_start += 1
                #Loops through each square
                while self.letter_number_of_start != self.letter_number_of_end:
                    for key, value in dictionar_of_letters_to_numbers.items():
                        if value == self.letter_number_of_start:
                            #Determines the square that the rook went past
                            new_number = key
                    new_number = str(str(new_number)[0]) + str(self.number_that_stayed_the_same)

                    #Checks to see if that square is empty
                    if position_dic[str(new_number)] != "None":
                        #If not, the move is not valid
                        self.blocked = "Yes"

                    #Iterates the loop, checking every square the rook went past
                    self.letter_number_of_start += 1

            #Checks to see if the move was valid
            if self.blocked == "No":
                return "True"


        def letter_same(self, position_piece, pos_chess):

            if int(str(pos_chess)[1]) - int(str(position_piece)[1]) >= 1:
                #This is for when the rook gets moved up

                self.number_of_end += 1
                #Iterates through the squares
                while str(self.number_of_end) != str(self.number_of_start):
                    new_number = self.number_of_end
                    new_number = str(self.letter_that_stayed_the_same) + str(new_number)

                    #Checks the see if the square is occupied
                    if position_dic[str(new_number)] != "None":
                        #If it is occupied, then the move is NOT valid
                        self.blocked = "Yes"

                    #Continues the Loop
                    self.number_of_end += 1

            elif int(str(pos_chess)[1]) - int(str(position_piece)[1]) < 0:
                #This is used when the rook gets moved down

                self.number_of_start += 1
                #Iterates through the squares
                while str(self.number_of_start) != str(self.number_of_end):

                    #Assignes new_number to a square the rook went past
                    new_number = self.number_of_start
                    new_number = str(self.letter_that_stayed_the_same) + str(new_number)

                    #Checks to see if the square is occupied
                    if position_dic[str(new_number)] != "None":
                        #If it is, the move is NOT valid
                        self.blocked = "Yes"

                    #Continues the loop
                    self.number_of_start += 1

            #Checks the final verdict of the move, if it is valid or not
            if self.blocked == "No":
                return "True"

    class path_bishop():
        '''
        This class is specific to the Bishop, to check it's unique way of moving accross the baord
        There is one function, but four main IF statements to determine if the move went
        down to the right/left or up to the right/left
        '''
        def __init__(self, pos_chess, position_piece, piece_that_moved):
            #Initializes variables that will be used frequently
            self.blocked = "No"
            self.piece_that_moved = piece_that_moved
            self.number_pos = int(str(pos_chess)[1])
            self.number_position = int(str(position_piece)[1])
            self.first = True

        def recurse(self, difference_of_number, first_letter, second_letter):

            if difference_of_number >= 1:
                '''
                When the Bishop gets moved down
                '''
                if first_letter - second_letter >= 1:
                    '''
                    When the Bishop Gets moved to the left'''

                    #This loop is to check each square the Bishop passed By
                    while second_letter != first_letter:
                        for key, value in dictionar_of_letters_to_numbers.items():
                            if value == second_letter:
                                new_number = key

                        #This is the corrdinate of a square that the Bishop went passed
                        new_number = str(str(new_number) + str(self.number_pos))

                        #Checks the square to determine
                        if position_dic[str(new_number)] != "None":
                            if self.first != True:
                                self.blocked = "Yes"

                        #Changes values to iterate through loops
                        second_letter += 1
                        self.number_pos += 1
                        self.first = False

                elif first_letter - second_letter < 0:
                    '''
                    When the Bishop Gets moved to the Right'''

                    #Loop to check each square the Bishop passed by
                    while first_letter != second_letter:
                        for key, value in dictionar_of_letters_to_numbers.items():
                            if value == first_letter:
                                new_number = key

                        #Updates variable with the sqaure corrdinate
                        new_number = str(str(new_number) + str(self.number_position ))

                        #Checks to make sure the corrdinate is empty
                        if position_dic[str(new_number)] != "None":
                            if self.first != True:
                                self.blocked = "Yes"

                        #Updates Values
                        first_letter += 1
                        self.number_position -= 1
                        self.first = False

                #Checks to see if the move was valid
                if self.blocked == "No":
                    return "True"


            elif difference_of_number < 0:
                '''
                When the Bishop Gets moved up
                '''
                if first_letter - second_letter >= 1:
                    '''
                    When the Bishop gets moved to the left'''

                    while second_letter != first_letter:

                        #Checks each square
                        for key, value in dictionar_of_letters_to_numbers.items():
                            if value == second_letter:
                                new_number = key

                        #Assigns vararable to the square the Bishop passed by
                        new_number = str(str(new_number) + str(self.number_pos))

                        #Checks to see if the square is empty
                        if position_dic[str(new_number)] != "None":
                            if self.first != True:
                                self.blocked = "Yes"


                        #Iterates through Loops
                        second_letter += 1
                        self.number_pos -= 1
                        self.first = False


                elif first_letter - second_letter < 0:
                    '''
                    When the Bishop gets moved to the right'''

                    while first_letter != second_letter:

                        #Checks each square
                        for key, value in dictionar_of_letters_to_numbers.items():
                            if value == first_letter:
                                new_number = key

                        #Updates variable with an appropriate square
                        new_number = str(str(new_number) + str(self.number_position))

                        #Checks to see if that square was empty
                        if position_dic[str(new_number)] != "None":
                            if self.first != True:
                                self.blocked = "Yes"

                        #Iterates through loops by changing variable values
                        first_letter += 1
                        self.number_position += 1
                        self.first = False

                #Checks to see if the whole move was valid
                if self.blocked == "No":
                    return "True"
