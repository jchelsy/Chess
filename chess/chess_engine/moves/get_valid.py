from ..castling import CastleRights

""" All moves (considering checks) """


def getValidMoves(self):
    temp_enpassantpossible = self.enpassantPossible
    temp_castlerights = CastleRights(self.currentCastlingRight.wks, self.currentCastlingRight.bks,  # copy current
                                     self.currentCastlingRight.wqs, self.currentCastlingRight.bqs)  # castle rights

    # 1.) Generate all possible moves
    moves = self.getAllPossibleMoves()

    # 2.) For each possible moves, simulate the moves
    for i in range(len(moves) - 1, -1, -1):  # When removing from a list, go backwards through the list
        self.makeMove(moves[i])
        # 3.) Generate all opponent's moves
        # 4.) For each of the opponent's moves, see if they attacked the user's King
        self.whiteToMove = not self.whiteToMove
        if self.inCheck():
            moves.remove(moves[i])  # 5.) If they do attack the user's king, it's not a valid moves
        self.whiteToMove = not self.whiteToMove  # Swap player turn
        self.undoMove()
    if len(moves) == 0:  # Checkmate or Stalemate
        if self.inCheck():
            self.checkmate = True
        else:
            self.stalemate = True

    if self.whiteToMove:
        self.getCastleMoves(self.whiteKingLocation[0], self.whiteKingLocation[1], moves)
    else:
        self.getCastleMoves(self.blackKingLocation[0], self.blackKingLocation[1], moves)
    self.enpassantPossible = temp_enpassantpossible
    self.currentCastlingRight = temp_castlerights
    return moves
