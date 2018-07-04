from Data_Conversion.position_of_pieces import teams_turn

def move_turn(piece_that_moved, teams_turn):

    if str(piece_that_moved)[0] == teams_turn:
        return "True"
    else:
        if str(piece_that_moved)[0] == "L":
            if str(piece_that_moved)[5] == teams_turn:
                return "True"
            else:
                return "False"

        elif str(piece_that_moved)[0] == "R":

            if str(piece_that_moved)[6] == teams_turn:
                return "True"
            else:
                return "False"
        else:
            return "False"
