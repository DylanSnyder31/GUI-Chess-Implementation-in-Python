'''
This function is to see if the square that the piece decided to 'land' on was occupied or not.
This is different than checking_for_blocked_path because this only checks the final square, not the squares inbetween, making it able to generalize through the pieces.

Works in 3 steps:
    1. Check if the square is empty or not
    2.If so, Check what color the piece is on the occupied square then;
        Check the color of the piece that moved
    3. Compare the two colors
        A. If they are the same, then the move is invalid
        B. If they differ then the piece is captured, and the piece is valid
'''
def is_square_occupied(chess_position_numerical, position_piece, pos_chess, piece_that_moved):

    #Step 1: Check if the square is empty or not
    if position_piece[pos_chess] != 'None':

        #This variable is the name (ID) of the piece that occupies that square
        piece_occupied = str(position_piece[pos_chess])

        #Step 2: See what color the piece that occupies the square is
        if str(piece_occupied)[0] == 'L':
            color_of_occupied = str(piece_occupied[5])
        elif str(piece_occupied)[0] == 'R':
            color_of_occupied = str(piece_occupied[6])
        else:
            color_of_occupied = str(piece_occupied[0])

        #Step 2: See what color the attacking piece is
        if str(piece_that_moved)[0] == 'L':
            color_of_moved = str(piece_that_moved[5])
        elif str(piece_that_moved)[0] == 'R':
            color_of_moved = str(piece_that_moved[6])
        else:
            color_of_moved = str(piece_that_moved[0])

        #Step 3: Check if the colors match or not, and if it is a capture or not
        if color_of_moved != color_of_occupied:
            return "True, Captured"

    else:
        #If the square is not occupied, then the move is valid
        return "True"
