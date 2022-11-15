""" Update the castle rights (given a move) """


def updateCastleRights(self, move):
    if move.pieceMoved == 'wK':
        self.currentCastlingRight.wks = False
        self.currentCastlingRight.wqs = False
    elif move.pieceMoved == 'bK':
        self.currentCastlingRight.bks = False
        self.currentCastlingRight.bqs = False
    elif move.pieceMoved == 'wR':
        if move.startRow == 7:
            if move.startCol == 0:  # left Rook
                self.currentCastlingRight.wqs = False
            elif move.startCol == 7:  # right Rook
                self.currentCastlingRight.wks = False
    elif move.pieceMoved == 'bR':
        if move.startRow == 0:
            if move.startCol == 0:  # left Rook
                self.currentCastlingRight.bqs = False
            elif move.startCol == 7:  # right Rook
                self.currentCastlingRight.bks = False
