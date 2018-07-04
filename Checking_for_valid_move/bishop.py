from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers
from Checking_for_valid_move.checking_for_blocked_path import is_path_blocked

def Bishop(position_piece, pos_chess):
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

        bishop_path = is_path_blocked.path_bishop()

        if abs(first_letter - second_letter) == abs(difference_of_number):
            if bishop_path.recurse(position_piece, pos_chess, difference_of_number, first_letter, second_letter) == "True":

                return True
            else:
                return False
        else:

            return False
    else:

        return False
