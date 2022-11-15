""" Determine if the enemy can attack the square (r, c) """


def squareUnderAttack(self, r, c):
    self.whiteToMove = not self.whiteToMove  # Switch to opponent's turn
    opp_moves = self.getAllPossibleMoves()
    self.whiteToMove = not self.whiteToMove  # Switch back to player's turn
    for move in opp_moves:
        if move.endRow == r and move.endCol == c:  # Square is under attack
            return True
    return False
