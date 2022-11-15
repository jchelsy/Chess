from ..castling import CastleRights

""" Takes a Move as a parameter and executes it """


def makeMove(self, move):
    self.board[move.startRow][move.startCol] = "--"
    self.board[move.endRow][move.endCol] = move.pieceMoved
    self.moveLog.append(move)  # log the moves (so it can be undone later)
    self.whiteToMove = not self.whiteToMove  # swap player turn

    # update the King's location (if moved)
    if move.pieceMoved == 'wK':
        self.whiteKingLocation = (move.endRow, move.endCol)
    elif move.pieceMoved == 'bK':
        self.blackKingLocation = (move.endRow, move.endCol)

    # Pawn Promotion
    if move.isPawnPromotion:
        self.board[move.endRow][move.endCol] = move.pieceMoved[0] + 'Q'

    # Enpassant moves
    if move.isEnpassantMove:
        self.board[move.startRow][move.endCol] = '--'  # Capturing the pawn

    # update enpassantPossible variable
    if move.pieceMoved[1] == 'p' and abs(move.startRow - move.endRow) == 2:  # only on 2 square pawn advances
        self.enpassantPossible = ((move.startRow + move.endRow) // 2, move.startCol)
    else:
        self.enpassantPossible = ()

    # Castle moves
    if move.isCastleMove:
        if move.endCol - move.startCol == 2:  # King-side castle moves
            self.board[move.endRow][move.endCol - 1] = self.board[move.endRow][move.endCol + 1]  # moves the Rook
            self.board[move.endRow][move.endCol + 1] = '--'  # erase old Rook
        else:  # Queen-side castle moves
            self.board[move.endRow][move.endCol + 1] = self.board[move.endRow][move.endCol - 2]  # moves the Rook
            self.board[move.endRow][move.endCol - 2] = '--'  # erase old Rook

    # update castling rights (whenever it is a rook or a king moves
    self.updateCastleRights(move)
    self.castleRightsLog.append(CastleRights(self.currentCastlingRight.wks, self.currentCastlingRight.bks,
                                             self.currentCastlingRight.wqs, self.currentCastlingRight.bqs))
