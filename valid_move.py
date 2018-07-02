from difference_for_letter import dictionar_of_letters_to_numbers

class is_valid_move():

    def is_square_occupied(self, chess_position_numerical, position_piece, pos_chess, piece_that_moved):
        if position_piece[pos_chess] != 'None':
            piece_occupied = str(position_piece[pos_chess])
            if str(piece_occupied)[0] == 'L':
                color_of_occupied = str(piece_occupied[5])
            elif str(piece_occupied)[0] == 'R':
                color_of_occupied = str(piece_occupied[6])
            else:
                color_of_occupied = str(piece_occupied[0])

            if str(piece_that_moved)[0] == 'L':
                color_of_moved = str(piece_that_moved[5])
            elif str(piece_that_moved)[0] == 'R':
                color_of_moved = str(piece_that_moved[6])
            else:
                color_of_moved = str(piece_that_moved[0])

            if color_of_moved == color_of_occupied:
                return "False"

            else:
                piece_only = ""
                index = len(str(piece_that_moved)) - 1
                while str(piece_that_moved)[index] != " ":
                    piece_only += str(str(piece_that_moved)[index])
                    index -= 1

                if str(piece_only)[0] == str(1) or str(piece_only)[0] == str(2) or str(piece_only)[0] == str(3) or str(piece_only)[0] == str(4) or str(piece_only)[0] == str(5) or str(piece_only)[0] == str(6) or str(piece_only)[0] == str(7) or str(piece_only)[0] == str(8):
                    piece_only = piece_only[1:]
                piece_only = piece_only[::-1]
                s = is_valid_move()
                result = "not"
                if piece_only == "Rook":
                    result = s.rook( chess_position_numerical, pos_chess)
                elif piece_only == "Bishop":
                    result = s.Bishop( chess_position_numerical, pos_chess)
                elif piece_only == "Queen":
                    result = s.Queen( chess_position_numerical, pos_chess)
                elif piece_only == "King":
                    result = s.King( chess_position_numerical, pos_chess)
                elif piece_only == 'Knight':
                    result = s.knight(chess_position_numerical, pos_chess)
                elif piece_only == "Pawn":
                    result = s.pawn_capture(chess_position_numerical, pos_chess)


                if str(result) == "True":

                    return "True, Captured"
                else:
                    return "False"

        else:
            piece_only = ""
            index = len(str(piece_that_moved)) - 1
            while str(piece_that_moved)[index] != " ":
                piece_only += str(str(piece_that_moved)[index])
                index -= 1

            if str(piece_only)[0] == str(1) or str(piece_only)[0] == str(2) or str(piece_only)[0] == str(3) or str(piece_only)[0] == str(4) or str(piece_only)[0] == str(5) or str(piece_only)[0] == str(6) or str(piece_only)[0] == str(7) or str(piece_only)[0] == str(8):
                piece_only = piece_only[1:]
            piece_only = piece_only[::-1]
            s = is_valid_move()
            result = "not"
            if piece_only == "Rook":
                result = s.rook( chess_position_numerical, pos_chess)
            elif piece_only == "Bishop":
                result = s.Bishop( chess_position_numerical, pos_chess)
            elif piece_only == "Queen":
                result = s.Queen( chess_position_numerical, pos_chess)
            elif piece_only == "King":
                result = s.King( chess_position_numerical, pos_chess)
            elif piece_only == 'Knight':
                result = s.knight(chess_position_numerical, pos_chess)
            elif piece_only == "Pawn":
                result = s.pawn(chess_position_numerical, pos_chess)

            if str(result) == "True":

                return "True"
            else:
                return "False"


    def rook(self, position_piece, pos_chess):
        '''
        NUMBER STAY SAME
        OR
        LETTER STAY SAME
        '''

        if str(position_piece)[0] == str(pos_chess)[0]:

            return True
        elif str(position_piece)[1] == str(pos_chess)[1]:

            return True
        else:

            return False

    def knight(self, position_piece, pos_chess):
        '''
        want abs(letter_number - letter_number2) + abs(number - number)
        THen either number or letter has to varry by exactly ONE
        '''
        letter_number1 = int(dictionar_of_letters_to_numbers[str(position_piece)[0]])
        letter_number2 = int(dictionar_of_letters_to_numbers[str(pos_chess)[0]])

        number1 = int(str(position_piece)[1])
        number2 = int(str(pos_chess)[1])

        difference_between = abs(letter_number1 - letter_number2) + abs(number1 - number2)

        if difference_between == 3:
            if abs(letter_number1 - letter_number2) == 1:
                return True
            elif abs(number1 - number2) == 1:
                return True
            else:
                return False

        else:
            return False

    def Bishop(self, position_piece, pos_chess):
        '''
        NUMBER DID NOT STAY THE SAME
        GET DIFFerecne
        CALCULATE DIFFerecne for LETTER
        CHECK TO SEE IF THAT MAKES SENSE
        '''
        if str(position_piece)[1] != str(pos_chess)[1]:

            difference_of_number = int(str(position_piece)[1]) - int(str(pos_chess)[1])
            first_letter = dictionar_of_letters_to_numbers[str(position_piece)[0]]
            second_letter = dictionar_of_letters_to_numbers[str(pos_chess)[0]]
            if abs(first_letter - second_letter) == abs(difference_of_number):
                return True
            else:

                return False
        else:

            return False


    def Queen(self, position_piece, pos_chess):
        '''
        CHECK Bishop AND Rook
        IF ONE IS TRUE;
        THEN QUEEN IS TRUE
        '''
        s = is_valid_move()
        rook_result = s.rook(position_piece, pos_chess)
        Bishop_result = s.Bishop(position_piece, pos_chess)

        if rook_result == True or Bishop_result == True:
            return True

        else:
            return False

    def King(self, position_piece, pos_chess):
        '''
        +-1 for number then letter stays same
        +-1 for letter then number stays same
        '''

        if int(position_piece[1]) + 1 == int(pos_chess[1]) or int(position_piece[1]) -1 == int(pos_chess[1]):
            if str(position_piece)[0] == str(pos_chess)[0]:
                return True
            else:
                return False

        elif int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) + 1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]) or int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) -1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
            if str(position_piece)[1] == str(pos_chess)[1]:
                return True
            else:
                return False

        else:
            return False

    def pawn(self, position_piece, pos_chess):
        '''
        HAS to MOVE UP BY ONE
        UNLESS CAPTURE THEN ADD one to letter and number
        '''
        if int(str(position_piece)[1]) + 1 == int(str(pos_chess)[1]):
            return True
        else:
            return False

    def pawn_capture(self, position_piece, pos_chess):
        '''
        + 1 for number
        +- one for letter
        '''
        if int(str(position_piece)[1]) + 1 == int(str(pos_chess)[1]):
            if int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) + 1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]) or int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) - 1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
                return True
            else:
                return False
        else:
            return False

    def is_path_blocked(self, position_piece, pos_chess):
        pass

    def special_cases(self, position_piece, pos_chess):
        pass

    def main(self, chess_position_numerical, position_piece, pos_chess, piece_that_moved):
        s = is_valid_move()
        status = s.is_square_occupied(chess_position_numerical, position_piece, pos_chess, piece_that_moved)
        return status
