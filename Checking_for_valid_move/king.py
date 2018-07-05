from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers

def King(position_piece, pos_chess):
    '''
    The rules I used to determine the path of the king:

    1. Check if the number of the corrdinate moved up or down by one if so, Check if the
                    letter stayed the same or the numeric value of the letter stayed the same
        A. This is to check if the King moved up or down only by one, or if it moved Diagonally by one

    2. Check if the numeric value of the letter moved up or down by one
                                        if so, Check if the number stayed the same
        A. This is to check if the King moved left or right only by one
'''

    #Step 1 : Check if the number differs by no more or less than one
    if int(position_piece[1]) + 1 == int(pos_chess[1]) or int(position_piece[1]) -1 == int(pos_chess[1]):

        #Check to see if the letters are the same
        if str(position_piece)[0] == str(pos_chess)[0]:
            return True

        #Check to see if the numeric value of the letter changed by one
        elif int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) + 1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]) or int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) -1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
            return True


    #Checks to see if the numeric value of the letters differs by by no more or less than one
    elif int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) + 1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]) or int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) -1 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):

        #Checks to make sure the numbers are the same
        if str(position_piece)[1] == str(pos_chess)[1]:
            return True
