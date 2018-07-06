from Data_Conversion.position_of_pieces import teams_turn
from Data_Conversion.position_of_pieces import position_dic

#Imports each of the pieces' specific files
from Checking_for_valid_move.bishop import Bishop
from Checking_for_valid_move.king import King
from Checking_for_valid_move.knight import knight
from Checking_for_valid_move.pawn import pawn_movement
from Checking_for_valid_move.Queen import Queen
from Checking_for_valid_move.rook import rook

from Checking_for_valid_move.turn_based import move_turn
from Checking_for_valid_move.is_square_occupied import is_square_occupied

class is_valid_move():
    ''''
    This function is kinda complicated, and I am sure I could have modularized or organized the code in a more beautiful and readable way, but
    essentially this code is checking all of the edge (and normal) cases that the pieces could have been moved to. It checks what piece has been moved (pawn, Queen, etc.), and then checks
    against multiple different factors if that move was valid.
    '''

    def valid(self, chess_position_numerical, position_piece, pos_chess, piece_that_moved):
        #The teams_turn variable needed to be global even though I imported it through the file location
        global teams_turn

        pawn = pawn_movement(chess_position_numerical)
        result = ""
        piece_only = ""

        #Gets the name of the piece only, discarding color and left/right
        #Example: "Left Black Rook" would become "Rook"
        index = len(str(piece_that_moved)) - 1
        while str(piece_that_moved)[index] != " ":
            piece_only += str(str(piece_that_moved)[index])
            index -= 1

        #Continues breking up the ID into the piece
        if str(piece_only)[0] == str(1) or str(piece_only)[0] == str(2) or str(piece_only)[0] == str(3) or str(piece_only)[0] == str(4) or str(piece_only)[0] == str(5) or str(piece_only)[0] == str(6) or str(piece_only)[0] == str(7) or str(piece_only)[0] == str(8):
            piece_only = piece_only[1:]
        piece_only = piece_only[::-1]

        #analysis of piece based on what piece it was
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
                #This means the piece MUST be a pawn
                #THe pawn is isolated from the other pieces because it has different moving rules based on if it is capturing a piece or not

                if str(position_dic[str(chess_position_numerical)])[0] == 'W':
                    #Since the piece is white, it checks to see if it has 'landed' onto the top row, Where it can be promoted
                    if str(pos_chess) == "a8" or str(pos_chess) == "b8" or str(pos_chess) == "c8" or str(pos_chess) == "d8" or str(pos_chess) == "e8" or str(pos_chess) == "f8" or str(pos_chess) == "g8" or str(pos_chess) == "h8":
                        #If so, chnage the team that has active play
                        teams_turn = "B"

                        #Return that the move was valid
                        return "New_Piece"
                else:
                    #Since the piece is black it checks the bottom
                    if str(pos_chess) == "a1" or str(pos_chess) == "b1" or str(pos_chess) == "c1" or str(pos_chess) == "d1" or str(pos_chess) == "e1" or str(pos_chess) == "f1" or str(pos_chess) == "g1" or str(pos_chess) == "h1":
                        if move_turn(piece_that_moved, teams_turn) == "True":

                            #Changes the active play to White
                            teams_turn ="W"

                            #Returns that the move was valid
                            return "New_Piece"

                result = pawn.pawn_capture(chess_position_numerical, pos_chess)

            if str(result) == "True":
                if move_turn(piece_that_moved, teams_turn) == "True":
                    #If the move was valid, change the active play and return that the move was valid
                    if teams_turn == "W":
                        teams_turn = "B"
                    else:
                        teams_turn ="W"
                    return "True, Captured"


        elif is_square_occupied(chess_position_numerical, position_piece, pos_chess, piece_that_moved) == "True":
            if result == "":
                #Same as above, the pawn has to go here
                if str(position_dic[str(chess_position_numerical)])[0] == 'W':
                    #Checks to see if the top row is the end location, since the piece was white
                    if str(pos_chess) == "a8" or str(pos_chess) == "b8" or str(pos_chess) == "c8" or str(pos_chess) == "d8" or str(pos_chess) == "e8" or str(pos_chess) == "f8" or str(pos_chess) == "g8" or str(pos_chess) == "h8":
                        if move_turn(piece_that_moved, teams_turn) == "True":

                            #Changes the play
                            teams_turn = "B"

                            #Returns that the move was Valid
                            return "New_Piece"
                else:
                    #Since the piece is black, the algorithm checks the bottom row
                    if str(pos_chess) == "a1" or str(pos_chess) == "b1" or str(pos_chess) == "c1" or str(pos_chess) == "d1" or str(pos_chess) == "e1" or str(pos_chess) == "f1" or str(pos_chess) == "g1" or str(pos_chess) == "h1":
                        if move_turn(piece_that_moved, teams_turn) == "True":

                            #Changes the team that can move
                            teams_turn ="W"

                            #Returns that the move was valid
                            return "New_piece"

                result = pawn.pawn(chess_position_numerical, pos_chess)


            if str(result) == "True":
                if move_turn(piece_that_moved, teams_turn) == "True":
                    #If the move was valid, change the play and return that it was valid
                    if teams_turn == "W":
                        teams_turn = "B"
                    else:
                        teams_turn ="W"

                    return "True"

            elif str(result) == "Castle":
                '''
                An Edge-Case for Castling, Done mostly in it's own file '''

                if move_turn(piece_that_moved, teams_turn) == "True":
                    #Changes the play and returns that the move was valid
                    if teams_turn == "W":
                        teams_turn = "B"
                    else:
                        teams_turn ="W"

                    return "Castle"

    def main(self, chess_position_numerical, position_piece, pos_chess, piece_that_moved):
        checking = is_valid_move()

        #Calls the above function and returns the result to Board.py
        #Board.py takes the data and runs some more analysis, and if the move passes that, then the piece will move
        #on the GUI for the user, and the dictionary will update locations of all the pieces
        status = checking.valid(chess_position_numerical, position_piece, pos_chess, piece_that_moved)
        return status
