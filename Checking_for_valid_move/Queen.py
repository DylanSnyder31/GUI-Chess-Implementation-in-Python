from Checking_for_valid_move.rook import rook
from Checking_for_valid_move.bishop import Bishop

def Queen(position_piece, pos_chess, piece_that_moved):
    '''
    The rules I used to determine the path of the Queen:
    1. See if the Rook or the Bishop returns a valid move
    '''
    if rook(position_piece, pos_chess) == True or Bishop(position_piece, pos_chess, piece_that_moved) == True:
        return True
