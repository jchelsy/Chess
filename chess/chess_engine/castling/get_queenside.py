from ..moves import Move


def getQueensideCastleMoves(self, r, c, moves):
    if self.board[r][c - 1] == '--' and self.board[r][c - 2] == '--' and self.board[r][c - 3]:
        if not self.squareUnderAttack(r, c - 1) and not self.squareUnderAttack(r, c - 2):
            moves.append(Move((r, c), (r, c - 2), self.board, isCastleMove=True))
