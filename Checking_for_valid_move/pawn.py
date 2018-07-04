from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers
from Data_Conversion.position_of_pieces import position_dic

def pawn(position_piece, pos_chess):

    piece = position_dic[str(position_piece)]

    if str(piece)[0] == 'W':


        '''
        HAS to MOVE UP BY ONE
        UNLESS CAPTURE THEN ADD one to letter and number
        '''
        if int(str(position_piece)[1]) + 1 == int(str(pos_chess)[1]):
            if int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):

                return True
            else:
                return False

        else:

            if str(position_piece) == "a2" or str(position_piece) == "b2" or str(position_piece) == "c2" or str(position_piece) == "d2" or str(position_piece) == "e2" or str(position_piece) == "f2" or str(position_piece) == "g2" or str(position_piece) == "h2":
                if int(str(position_piece)[1]) + 2 == int(str(pos_chess)[1]):
                    if int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
                        return True
                    else:
                        return False
                else:
                    return False


            else:
                return False


    else:
        if int(str(position_piece)[1]) -1 == int(str(pos_chess)[1]):
            if int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):

                return True
            else:
                return False
        else:
            if str(position_piece) == "a7" or str(position_piece) == "b7" or str(position_piece) == "c7" or str(position_piece) == "d7" or str(position_piece) == "e7" or str(position_piece) == "f7" or str(position_piece) == "g7" or str(position_piece) == "h7":
                if int(str(position_piece)[1]) - 2 == int(str(pos_chess)[1]):
                    if int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
                        return True
                    else:
                        return False
                else:
                    return False


            else:
                return False
def pawn_capture(position_piece, pos_chess):
    piece = position_dic[str(position_piece)]

    if str(piece)[0] == 'W':

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

    else:
        if int(str(position_piece)[1]) - 1 == int(str(pos_chess)[1]):
            if int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) + 1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]) or int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) - 1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
                return True
            else:
                return False

        else:
            return False
