from Checking_for_valid_move.checking_for_blocked_path import is_path_blocked

def check(piece_only, chess_position_numerical, position_piece, pos_chess):
    if str(piece_only)[0] == str(1) or str(piece_only)[0] == str(2) or str(piece_only)[0] == str(3) or str(piece_only)[0] == str(4) or str(piece_only)[0] == str(5) or str(piece_only)[0] == str(6) or str(piece_only)[0] == str(7) or str(piece_only)[0] == str(8):
        piece_only = piece_only[1:]
    piece_only = piece_only[::-1]

    result = "not"
    if piece_only == "Rook":
        path_blocked = is_path_blocked()
        rook_path = path_blocked.path_rook()
        if str(position_piece)[0] == str(pos_chess)[0]:
            result = rook_path.letter_same( position_piece, pos_chess):

    


        elif str(position_piece)[1] == str(pos_chess)[1]:
            result = rook_path.number_same(position_piece, pos_chess):


    elif piece_only == "Bishop":
        bishop_path = is_path_blocked.path_bishop()
        result = bishop_path.recurse(position_piece, pos_chess, difference_of_number, first_letter, second_letter)

    elif piece_only == "Queen":
        pass

    elif piece_only == 'Knight':
        pass



    if str(result) == "True":
