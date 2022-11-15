from ..castling import CastleRights

""" Undo the last move made """


def undoMove(self):
    if len(self.moveLog) != 0:  # Ensure a moves is present to undo
        move = self.moveLog.pop()
        self.board[move.startRow][move.startCol] = move.pieceMoved
        self.board[move.endRow][move.endCol] = move.pieceCaptured
        self.whiteToMove = not self.whiteToMove  # swap player turn

        # Update the King's position (if necessary)
        if move.pieceMoved == 'wK':
            self.whiteKingLocation = (move.startRow, move.startCol)
        elif move.pieceMoved == 'bK':
            self.blackKingLocation = (move.startRow, move.startCol)

        # Undo en passant
        if move.isEnpassantMove:
            self.board[move.endRow][move.endCol] = '--'  # leave landing square blank
            self.board[move.startRow][move.endCol] = move.pieceCaptured
            self.enpassantPossible = (move.endRow, move.endCol)

        # Undo a 2-square pawn advance
        if move.pieceMoved[1] == 'p' and abs(move.startRow - move.endRow) == 2:
            self.enpassantPossible = ()

        # Undo castling rights
        self.castleRightsLog.pop()  # Get rid of the new castle rights from the moves being undone
        new_rights = self.castleRightsLog[-1]
        self.currentCastlingRight = CastleRights(new_rights.wks, new_rights.bks, new_rights.wqs, new_rights.bqs)

        # Undo castle moves
        if move.isCastleMove:
            if move.endCol - move.startCol == 2:  # King-side
                self.board[move.endRow][move.endCol + 1] = self.board[move.endRow][move.endCol - 1]
                self.board[move.endRow][move.endCol - 1] = '--'
            else:  # Queen-side
                self.board[move.endRow][move.endCol - 2] = self.board[move.endRow][move.endCol + 1]
                self.board[move.endRow][move.endCol + 1] = '--'
