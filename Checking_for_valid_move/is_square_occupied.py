def is_square_occupied(chess_position_numerical, position_piece, pos_chess, piece_that_moved):

    if position_piece[pos_chess] != 'None':
        piece_occupied = str(position_piece[pos_chess])
        if str(piece_occupied)[0] == 'L':
            color_of_occupied = str(piece_occupied[5])
        elif str(piece_occupied)[0] == 'R':
            color_of_occupied = str(piece_occupied[6])
        else:
            color_of_occupied = str(piece_occupied[0])

        if str(piece_that_moved)[0] == 'L':
            color_of_moved = str(piece_that_moved[5])
        elif str(piece_that_moved)[0] == 'R':
            color_of_moved = str(piece_that_moved[6])
        else:
            color_of_moved = str(piece_that_moved[0])

        if color_of_moved == color_of_occupied:
            return "False"

        else:

            return "True, Captured"


    else:

            return "True"
