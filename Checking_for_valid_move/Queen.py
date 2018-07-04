
from Checking_for_valid_move.rook import rook
from Checking_for_valid_move.bishop import Bishop
def Queen(position_piece, pos_chess):
        '''
        CHECK Bishop AND Rook
        IF ONE IS TRUE;
        THEN QUEEN IS TRUE
        '''

        rook_result = rook(position_piece, pos_chess)
        Bishop_result = Bishop(position_piece, pos_chess)

        if rook_result == True or Bishop_result == True:
            return True

        else:
            return False
