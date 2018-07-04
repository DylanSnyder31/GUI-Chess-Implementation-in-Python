from Data_Conversion.position_of_pieces import position_dic
from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers

class is_path_blocked():

    class path_rook():
        '''
        SIDEWAYS
        '''
        def number_same(self, position_piece, pos_chess):
            if dictionar_of_letters_to_numbers[str(pos_chess)[0]] -  dictionar_of_letters_to_numbers[str(position_piece)[0]] >= 1:
                '''
                To the Right
                '''
                number_that_stayed_the_same = str(pos_chess)[1]

                number_of_start = dictionar_of_letters_to_numbers[str(pos_chess)[0]]
                number_of_end =  dictionar_of_letters_to_numbers[str(position_piece)[0]] + 1


                blocked = "No"
                while number_of_end != number_of_start:
                    for key, value in dictionar_of_letters_to_numbers.items():
                        if value == number_of_end:
                            new_number = key

                    new_number = str(str(new_number)[0]) + str(number_that_stayed_the_same)
                    print(position_dic[str(new_number)])
                    if position_dic[str(new_number)] == "None":
                        pass

                    else:
                        blocked = "Yes"


                    number_of_end += 1

                if blocked == "Yes":
                    return "False"

                else:
                    return "True"


            elif dictionar_of_letters_to_numbers[str(pos_chess)[0]] -  dictionar_of_letters_to_numbers[str(position_piece)[0]] < 0:
                '''
                Going to the Left
                '''

                number_that_stayed_the_same = str(pos_chess)[1]

                number_of_start = dictionar_of_letters_to_numbers[str(pos_chess)[0]] + 1
                number_of_end =  dictionar_of_letters_to_numbers[str(position_piece)[0]]


                blocked = "No"
                while number_of_start != number_of_end:
                    for key, value in dictionar_of_letters_to_numbers.items():
                        if value == number_of_start:
                            new_number = key

                    new_number = str(str(new_number)[0]) + str(number_that_stayed_the_same)

                    if position_dic[str(new_number)] == "None":
                        pass
                    else:
                        blocked = "Yes"


                    number_of_start += 1

                if blocked == "Yes":
                    return "False"

                else:
                    return "True"






        def letter_same(self, position_piece, pos_chess):

            if int(str(pos_chess)[1]) - int(str(position_piece)[1]) >= 1:
                '''
                GO UP
                '''
                letter_that_stayed_the_same = str(pos_chess)[0]

                number_of_start = str(pos_chess)[1]
                number_of_end =  int(str(position_piece)[1]) + 1


                blocked = "No"

                while str(number_of_end) != str(number_of_start):

                    new_number = number_of_end
                    new_number = str(letter_that_stayed_the_same) + str(new_number)

                    if position_dic[str(new_number)] == "None":
                        pass
                    else:
                        blocked = "Yes"


                    number_of_end += 1

                if blocked == "Yes":
                    return "False"

                else:
                    return "True"

            elif int(str(pos_chess)[1]) - int(str(position_piece)[1]) < 0:
                '''
                GO UP
                '''
                letter_that_stayed_the_same = str(pos_chess)[0]

                number_of_start = int(str(pos_chess)[1]) + 1
                number_of_end =  str(position_piece)[1]


                blocked = "No"

                while str(number_of_start) != str(number_of_end):

                    new_number = number_of_start
                    new_number = str(letter_that_stayed_the_same) + str(new_number)

                    if position_dic[str(new_number)] == "None":
                        pass
                    else:
                        blocked = "Yes"


                    number_of_start += 1

                if blocked == "Yes":
                    return "False"

                else:
                    return "True"

            return "True"


    class path_bishop():
        def recurse(self, position_piece, pos_chess, difference_of_number, first_letter, second_letter):
            if difference_of_number >= 1:
                '''
                Going Down
                '''
                if first_letter - second_letter >= 1:

                    '''
                    To the Left
                    '''
                    #second_letter += 1
                    blocked = "No"
                    number = int(str(pos_chess)[1])
                    first = True
                    while second_letter != first_letter:

                        for key, value in dictionar_of_letters_to_numbers.items():
                            if value == second_letter:
                                new_number = key


                        new_number = str(str(new_number) + str(number))

                        if position_dic[str(new_number)] == "None" or first == True:
                            pass
                        else:
                            blocked = "Yes"


                        second_letter += 1
                        number += 1

                        first = False
                    if blocked == "Yes":
                        return "False"

                    else:
                        return "True"

                elif first_letter - second_letter < 0:
                    '''
                    To the Right
                    '''

                    blocked = "No"
                    number = int(str(position_piece)[1])

                    first = True
                    while first_letter != second_letter:

                        for key, value in dictionar_of_letters_to_numbers.items():
                            if value == first_letter:
                                new_number = key


                        new_number = str(str(new_number) + str(number))

                        if position_dic[str(new_number)] == "None" or first == True:
                            pass
                        else:
                            blocked = "Yes"


                        first_letter += 1
                        number -= 1
                        first = False
                    if blocked == "Yes":
                        return "False"

                    else:
                        return "True"
            #################################################################################################################################
            ###```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````###
            #################################################################################################################################
            elif difference_of_number < 0:
                '''
                Going Up
                '''
                if first_letter - second_letter >= 1:

                    '''
                    To the Left
                    '''

                    #second_letter += 1
                    blocked = "No"
                    number = int(str(pos_chess)[1])
                    first = True
                    while second_letter != first_letter:

                        for key, value in dictionar_of_letters_to_numbers.items():
                            if value == second_letter:
                                new_number = key


                        new_number = str(str(new_number) + str(number))
                        if position_dic[str(new_number)] == "None" or first == True:
                            pass
                        else:
                            blocked = "Yes"


                        second_letter += 1
                        number -= 1

                        first = False
                    if blocked == "Yes":
                        return "False"

                    else:
                        return "True"

                elif first_letter - second_letter < 0:
                    '''
                    To the Right
                    '''

                    blocked = "No"
                    number = int(str(position_piece)[1])

                    first = True
                    while first_letter != second_letter:

                        for key, value in dictionar_of_letters_to_numbers.items():
                            if value == first_letter:
                                new_number = key


                        new_number = str(str(new_number) + str(number))

                        if position_dic[str(new_number)] == "None" or first == True:
                            pass
                        else:
                            blocked = "Yes"


                        first_letter += 1
                        number += 1
                        first = False
                    if blocked == "Yes":
                        return "False"

                    else:
                        return "True"
