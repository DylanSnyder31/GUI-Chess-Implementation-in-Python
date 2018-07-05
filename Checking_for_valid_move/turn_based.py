from Data_Conversion.position_of_pieces import teams_turn

def move_turn(piece_that_moved, teams_turn):
    '''
    This function makes it so each player gets a turn, and checks if the move is valid based on that data
    '''

    #Checks to see if the turn matches the piece that moved
    #Based on different properties of the name, this data can be figured out
    if str(piece_that_moved)[0] == teams_turn:
        return "True"
    else:
        if str(piece_that_moved)[0] == "L":
            if str(piece_that_moved)[5] == teams_turn:
                return "True"
        elif str(piece_that_moved)[0] == "R":
            if str(piece_that_moved)[6] == teams_turn:
                return "True"
