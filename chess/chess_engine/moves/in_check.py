""" Determine if the current player is in check """


def inCheck(self):
    if self.whiteToMove:
        return self.squareUnderAttack(self.whiteKingLocation[0], self.whiteKingLocation[1])
    else:
        return self.squareUnderAttack(self.blackKingLocation[0], self.blackKingLocation[1])
