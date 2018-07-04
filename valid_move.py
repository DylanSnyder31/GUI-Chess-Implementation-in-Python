from Data_Conversion.difference_for_letter import dictionar_of_letters_to_numbers
from Data_Conversion.position_of_pieces import teams_turn
from Checking_for_valid_move.bishop import Bishop
from Checking_for_valid_move.is_square_occupied import is_square_occupied
from Checking_for_valid_move.king import King
from Checking_for_valid_move.knight import knight
from Checking_for_valid_move.pawn import pawn, pawn_capture
from Checking_for_valid_move.Queen import Queen
from Checking_for_valid_move.rook import rook
from Checking_for_valid_move.turn_based import teams_turn
from Checking_for_valid_move.turn_based import move_turn
class is_valid_move():

    def valid(self, chess_position_numerical, position_piece, pos_chess, piece_that_moved):
        global teams_turn
        if is_square_occupied(chess_position_numerical, position_piece, pos_chess, piece_that_moved) == "True, Captured":

            piece_only = ""
            index = len(str(piece_that_moved)) - 1
            while str(piece_that_moved)[index] != " ":
                piece_only += str(str(piece_that_moved)[index])
                index -= 1

            if str(piece_only)[0] == str(1) or str(piece_only)[0] == str(2) or str(piece_only)[0] == str(3) or str(piece_only)[0] == str(4) or str(piece_only)[0] == str(5) or str(piece_only)[0] == str(6) or str(piece_only)[0] == str(7) or str(piece_only)[0] == str(8):
                piece_only = piece_only[1:]
            piece_only = piece_only[::-1]

            result = "not"
            if piece_only == "Rook":
                result = rook( chess_position_numerical, pos_chess)
            elif piece_only == "Bishop":
                result = Bishop( chess_position_numerical, pos_chess)
            elif piece_only == "Queen":
                result = Queen( chess_position_numerical, pos_chess)
            elif piece_only == "King":
                result = King( chess_position_numerical, pos_chess)
            elif piece_only == 'Knight':
                result = knight(chess_position_numerical, pos_chess)
            elif piece_only == "Pawn":
                result = pawn_capture(chess_position_numerical, pos_chess)

            if str(result) == "True":
                if move_turn(piece_that_moved, teams_turn) == "True":
                    if teams_turn == "W":

                        teams_turn = "B"
                    else:

                        teams_turn ="W"
                    return "True, Captured"
            else:
                return "False"

        elif is_square_occupied(chess_position_numerical, position_piece, pos_chess, piece_that_moved) == "True":

            piece_only = ""
            index = len(str(piece_that_moved)) - 1
            while str(piece_that_moved)[index] != " ":
                piece_only += str(str(piece_that_moved)[index])
                index -= 1

            if str(piece_only)[0] == str(1) or str(piece_only)[0] == str(2) or str(piece_only)[0] == str(3) or str(piece_only)[0] == str(4) or str(piece_only)[0] == str(5) or str(piece_only)[0] == str(6) or str(piece_only)[0] == str(7) or str(piece_only)[0] == str(8):
                piece_only = piece_only[1:]
            piece_only = piece_only[::-1]
            s = is_valid_move()
            result = "not"
            if piece_only == "Rook":
                result = rook( chess_position_numerical, pos_chess)
            elif piece_only == "Bishop":
                result = Bishop( chess_position_numerical, pos_chess)
            elif piece_only == "Queen":
                result = Queen( chess_position_numerical, pos_chess)
            elif piece_only == "King":
                result = King( chess_position_numerical, pos_chess)
            elif piece_only == 'Knight':
                result = knight(chess_position_numerical, pos_chess)
            elif piece_only == "Pawn":
                result = pawn(chess_position_numerical, pos_chess)

            if str(result) == "True":


                if move_turn(piece_that_moved, teams_turn) == "True":
                    if teams_turn == "W":

                        teams_turn = "B"
                    else:

                        teams_turn ="W"
                    return "True"
                else:
                    return "False"
            else:
                return "False"
        else:
            return "False"

    def main(self, chess_position_numerical, position_piece, pos_chess, piece_that_moved):
        checking = is_valid_move()
        status = checking.valid(chess_position_numerical, position_piece, pos_chess, piece_that_moved)
        return status
