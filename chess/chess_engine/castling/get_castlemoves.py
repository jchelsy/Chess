""" Generate all valid castle moves for the King/Queen at (row, col) and add them to the list of moves """


def getCastleMoves(self, r, c, moves):
    if self.squareUnderAttack(r, c):
        return  # can't castle while in check
    if (self.whiteToMove and self.currentCastlingRight.wks) or (
            not self.whiteToMove and self.currentCastlingRight.bks):
        self.getKingsideCastleMoves(r, c, moves)
    if (self.whiteToMove and self.currentCastlingRight.wqs) or (
            not self.whiteToMove and self.currentCastlingRight.bqs):
        self.getQueensideCastleMoves(r, c, moves)
