from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers
from Data_Conversion.position_of_pieces import position_dic
def King(position_piece, pos_chess):
    '''
    The rules I used to determine the path of the king:

    1. Check if the number of the corrdinate moved up or down by one if so, Check if the
                    letter stayed the same or the numeric value of the letter stayed the same
        A. This is to check if the King moved up or down only by one, or if it moved Diagonally by one

    2. Check if the numeric value of the letter moved up or down by one
                                        if so, Check if the number stayed the same
        A. This is to check if the King moved left or right only by one

    3. Check if the player is trying to Castle, I hard-coded this in because of the little amount of checks needed

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

    #Step 3: Checking for a Castle
    elif int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) + 2 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]) or int(dictionar_of_letters_to_numbers[str(position_piece)[0]]) - 2 == int(dictionar_of_letters_to_numbers[str(pos_chess)[0]]):
            #If the piece is a white king
            if str(position_piece) == 'e1':
                #Checking to see what direction (Right)
                if str(pos_chess) == 'g1':
                    if position_dic['h1'] == "Right White Rook":
                        if position_dic['f1'] == "None":
                            return "Castle"
                else:
                    #Checking the swaures, to make sure they are empty
                    if position_dic['a1'] == "Left White Rook":
                        if position_dic['d1'] == "None":
                            if position_dic['b1'] == "None":
                                return "Castle"

            #If the piece is a black King
            elif str(position_piece) == 'e8':
                if str(pos_chess) == 'g8':
                    if str(pos_chess) == 'g8':
                        if position_dic['h8'] == "Right Black Rook":
                            if position_dic['f8'] == "None":
                                return "Castle"
                    else:
                        if position_dic['a8'] == "Left Black Rook":
                            if position_dic['d8'] == "None":
                                if position_dic['b8'] == "None":
                                    return "Castle"
