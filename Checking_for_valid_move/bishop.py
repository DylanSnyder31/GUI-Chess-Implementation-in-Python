from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers
from Checking_for_valid_move.checking_for_blocked_path import is_path_blocked

def Bishop(position_piece, pos_chess, piece_that_moved):
    '''
    The Rules I used to determine the path of a Bishop:

    1. The number in the chess corrdinates did not stay the same
        A. This is to make sure the Bishop did not go straight up/ down or to the left/right

    2. Get the difference of the numbers (EXAMPLE: a1 and d4 would have a difference of 3)
        A. This is to make sure the move was a correct diagonal, not a random move that wasn't
            straight up or down.

    3. Calculate the difference of the letters (if a = 1, b = 2 and so on), the example above applies here
        A. This is still to make sure the move was a diagonal

    4. Check the differences, if they are the same then the move was a correct Diagonal
        A. Just like the example had the same difference, it was a correct diagonal
    '''

    #Step 1: Check if number changed
    if str(position_piece)[1] != str(pos_chess)[1]:

        #Step two: Get the difference of the numbers
        difference_of_number = int(str(position_piece)[1]) - int(str(pos_chess)[1])

        #Step 3: Get numeric representation of the letters (Calculate difference in the if statement)
        first_letter = dictionar_of_letters_to_numbers[str(position_piece)[0]]
        second_letter = dictionar_of_letters_to_numbers[str(pos_chess)[0]]

        #Loads in another file, used in the second if statement
        bishop_path = is_path_blocked.path_bishop(pos_chess, position_piece, piece_that_moved)

        #Step 4: Check the differences
        if abs(first_letter - second_letter) == abs(difference_of_number):

            #If they equal, check to make sure the Bishop's path is clear so it doesn't jump over anything
            if bishop_path.recurse(difference_of_number, first_letter, second_letter) == "True":

                #If the path was clear, return a legal Move
                return True
