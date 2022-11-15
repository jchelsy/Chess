from ..moves import Move


def getKingsideCastleMoves(self, r, c, moves):
    if self.board[r][c + 1] == '--' and self.board[r][c + 2] == '--':
        if not self.squareUnderAttack(r, c + 1) and not self.squareUnderAttack(r, c + 2):
            moves.append(Move((r, c), (r, c + 2), self.board, isCastleMove=True))
