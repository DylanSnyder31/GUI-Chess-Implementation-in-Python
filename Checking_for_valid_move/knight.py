from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers

def knight(position_piece, pos_chess):
    '''
    The Rules I used to determine the path of the Kinight:

    1. See if |letter_number1 - letter_number2|  + |number1 - number2| is equal to three
        A. Where the letter_numbers are the numeric values of the letters, and numbers are the numbers of the corrdinates
            I. This eqution represents the original way the knight moves

    2. If that is so, check if the difference between the numeric value of the letters
                and the numbers if ONE varies by exactly one, the move is valid
        A. This is so the knight cannot just simple move up/down/left/right by just three;
                So the knights movement can be preserved
    '''

    #Gets the numeric values of the letters
    letter_number1 = int(dictionar_of_letters_to_numbers[str(position_piece)[0]])
    letter_number2 = int(dictionar_of_letters_to_numbers[str(pos_chess)[0]])

    #Get the numbers of the squares
    number1 = int(str(position_piece)[1])
    number2 = int(str(pos_chess)[1])

    #Step 1: See if the equation equals to three
    if abs(letter_number1 - letter_number2) + abs(number1 - number2) == 3:

        #Step 2: Check the difference between the letter_numbers
        if abs(letter_number1 - letter_number2) == 1:
            return True
            
        #Step2: Check the difference between the numbers
        elif abs(number1 - number2) == 1:
            return True
