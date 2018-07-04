from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers

def King( position_piece, pos_chess):
        '''
        +-1 for number then letter stays same
        +-1 for letter then number stays same
        +- for number then letter +-1
        '''

        if int(position_piece[1]) + 1 == int(pos_chess[1]) or int(position_piece[1]) -1 == int(pos_chess[1]):

            if str(position_piece)[0] == str(pos_chess)[0]:
                return True
            elif int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) + 1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]) or int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) -1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
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
