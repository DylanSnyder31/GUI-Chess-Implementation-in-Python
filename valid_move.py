from Data_Conversion.position_of_pieces import teams_turn
from Data_Conversion.position_of_pieces import position_dic
from Checking_for_valid_move.bishop import Bishop
from Checking_for_valid_move.is_square_occupied import is_square_occupied
from Checking_for_valid_move.king import King
from Checking_for_valid_move.knight import knight
from Checking_for_valid_move.pawn import pawn_movement
from Checking_for_valid_move.Queen import Queen
from Checking_for_valid_move.rook import rook

from Checking_for_valid_move.turn_based import move_turn
from Checking_for_valid_move.king_check import end_game

class is_valid_move():
    #Checks to make sure the move was valid, and not breaking any rules of Chess

    def valid(self, chess_position_numerical, position_piece, pos_chess, piece_that_moved):
        pawn = pawn_movement(chess_position_numerical)
        global teams_turn
        king_check = end_game(teams_turn)


        piece_only = ""
        index = len(str(piece_that_moved)) - 1
        while str(piece_that_moved)[index] != " ":
            piece_only += str(str(piece_that_moved)[index])
            index -= 1

        result = ""

        if str(piece_only)[0] == str(1) or str(piece_only)[0] == str(2) or str(piece_only)[0] == str(3) or str(piece_only)[0] == str(4) or str(piece_only)[0] == str(5) or str(piece_only)[0] == str(6) or str(piece_only)[0] == str(7) or str(piece_only)[0] == str(8):
            piece_only = piece_only[1:]
        piece_only = piece_only[::-1]


        if piece_only == "Rook":
            result = rook( chess_position_numerical, pos_chess)
        elif piece_only == "Bishop":
            result = Bishop( chess_position_numerical, pos_chess, piece_that_moved)
        elif piece_only == "Queen":
            result = Queen( chess_position_numerical, pos_chess, piece_that_moved)
        elif piece_only == "King":
            result = King( chess_position_numerical, pos_chess)
        elif piece_only == 'Knight':
            result = knight(chess_position_numerical, pos_chess)

        if is_square_occupied(chess_position_numerical, position_piece, pos_chess, piece_that_moved) == "True, Captured":
            '''
            This function gets called when the piece that moved is going to capture a piece
            '''

            if result == "":

                if str(position_dic[str(chess_position_numerical)])[0] == 'W':
                    if str(pos_chess) == "a8" or str(pos_chess) == "b8" or str(pos_chess) == "c8" or str(pos_chess) == "d8" or str(pos_chess) == "e8" or str(pos_chess) == "f8" or str(pos_chess) == "g8" or str(pos_chess) == "h8":
                        return "New_Piece"
                else:
                    if str(pos_chess) == "a1" or str(pos_chess) == "b1" or str(pos_chess) == "c1" or str(pos_chess) == "d1" or str(pos_chess) == "e1" or str(pos_chess) == "f1" or str(pos_chess) == "g1" or str(pos_chess) == "h1":
                        if move_turn(piece_that_moved, teams_turn) == "True":
                            #if king_check.in_check() == "True":

                            if teams_turn == "W":
                                teams_turn = "B"
                            else:
                                teams_turn ="W"
                            return "New_Piece"

                result = pawn.pawn_capture(chess_position_numerical, pos_chess)

            if str(result) == "True":
                if move_turn(piece_that_moved, teams_turn) == "True":
                    #if king_check.in_check() == "True":
                    if teams_turn == "W":
                        teams_turn = "B"
                    else:
                        teams_turn ="W"
                    return "True, Captured"


        elif is_square_occupied(chess_position_numerical, position_piece, pos_chess, piece_that_moved) == "True":
            if result == "":

                if str(position_dic[str(chess_position_numerical)])[0] == 'W':

                    print(str(pos_chess))
                    if str(pos_chess) == "a8" or str(pos_chess) == "b8" or str(pos_chess) == "c8" or str(pos_chess) == "d8" or str(pos_chess) == "e8" or str(pos_chess) == "f8" or str(pos_chess) == "g8" or str(pos_chess) == "h8":
                        if move_turn(piece_that_moved, teams_turn) == "True":
                            #if king_check.in_check() == "True":

                            if teams_turn == "W":
                                teams_turn = "B"
                            else:
                                teams_turn ="W"
                                return "New_Piece"
                else:

                    if str(pos_chess) == "a1" or str(pos_chess) == "b1" or str(pos_chess) == "c1" or str(pos_chess) == "d1" or str(pos_chess) == "e1" or str(pos_chess) == "f1" or str(pos_chess) == "g1" or str(pos_chess) == "h1":
                        if move_turn(piece_that_moved, teams_turn) == "True":
                            #if king_check.in_check() == "True":

                            if teams_turn == "W":
                                teams_turn = "B"
                            else:
                                teams_turn ="W"
                            return "New_piece"

                result = pawn.pawn(chess_position_numerical, pos_chess)


            if str(result) == "True":
                if move_turn(piece_that_moved, teams_turn) == "True":
                    #if king_check.in_check() == "True":

                    if teams_turn == "W":
                        teams_turn = "B"
                    else:
                        teams_turn ="W"
                    return "True"

            elif str(result) == "Castle":

                if move_turn(piece_that_moved, teams_turn) == "True":
                    if teams_turn == "W":
                        teams_turn = "B"
                    else:
                        teams_turn ="W"

                    return "Castle"
    def main(self, chess_position_numerical, position_piece, pos_chess, piece_that_moved):
        checking = is_valid_move()
        #Calls the above function and returns the result to Board.py
        status = checking.valid(chess_position_numerical, position_piece, pos_chess, piece_that_moved)
        return status
