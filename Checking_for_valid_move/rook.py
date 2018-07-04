from Checking_for_valid_move.checking_for_blocked_path import is_path_blocked

def rook(position_piece, pos_chess):
    '''
    NUMBER STAY SAME
    OR
    LETTER STAY SAME
    '''
    path_blocked = is_path_blocked()
    rook_path = path_blocked.path_rook()

    if str(position_piece)[0] == str(pos_chess)[0]:
        if rook_path.letter_same( position_piece, pos_chess) == 'True':
            return True
        else:
            return False



    elif str(position_piece)[1] == str(pos_chess)[1]:
        if rook_path.number_same(position_piece, pos_chess) == "True":

            return True
        else:
            
            return False



    else:

        return False
