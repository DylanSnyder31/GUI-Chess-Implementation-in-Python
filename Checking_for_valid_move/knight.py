from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers
def knight(position_piece, pos_chess):
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
