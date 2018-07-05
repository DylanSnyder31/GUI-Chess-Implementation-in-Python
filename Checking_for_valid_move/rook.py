from Checking_for_valid_move.checking_for_blocked_path import is_path_blocked

def rook(position_piece, pos_chess):
    path_blocked = is_path_blocked()
    rook_path = path_blocked.path_rook(position_piece, pos_chess)
    '''
    The Rules I used to determine the path of the Rook:

    1. Check to see if the number stayed the same
        A. This is to check if the rook went left/right

    2. Check if the letter stayed the same
        A. This is to check if the rook went up/down
    '''
    #Step 1: Check to see if the number stayed the same
    if str(position_piece)[1] == str(pos_chess)[1]:
        if rook_path.number_same(position_piece, pos_chess) == "True":
            return True
            
    #Step 2: Check to see if the letter stayed the same
    elif str(position_piece)[0] == str(pos_chess)[0]:
        if rook_path.letter_same( position_piece, pos_chess) == 'True':
            return True
