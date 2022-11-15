from ..moves import Move

""" Get all the pawn moves located at (row, col) and add them to the list """


def getPawnMoves(self, r, c, moves):
    if self.whiteToMove:  # White pawn moves
        if self.board[r - 1][c] == "--":  # 1-square Pawn advance
            moves.append(Move((r, c), (r - 1, c), self.board))
            if r == 6 and self.board[r - 2][c] == "--":  # 2-square Pawn advance
                moves.append(Move((r, c), (r - 2, c), self.board))
        if c - 1 >= 0:  # captures to the left
            if self.board[r - 1][c - 1][0] == 'b':  # enemy piece to capture
                moves.append(Move((r, c), (r - 1, c - 1), self.board))
            elif (r - 1, c - 1) == self.enpassantPossible:
                moves.append(Move((r, c), (r - 1, c - 1), self.board, isEnpassantMove=True))
        if c + 1 <= 7:  # captures to the right
            if self.board[r - 1][c + 1][0] == 'b':  # enemy piece to capture
                moves.append(Move((r, c), (r - 1, c + 1), self.board))
            elif (r - 1, c + 1) == self.enpassantPossible:
                moves.append(Move((r, c), (r - 1, c + 1), self.board, isEnpassantMove=True))

    else:  # Black pawn moves
        if self.board[r + 1][c] == "--":  # 1-square Pawn advance
            moves.append(Move((r, c), (r + 1, c), self.board))
            if r == 1 and self.board[r + 2][c] == "--":  # 2-square Pawn advance
                moves.append(Move((r, c), (r + 2, c), self.board))
        # Captures
        if c - 1 >= 0:  # Capture to left
            if self.board[r + 1][c - 1][0] == 'w':
                moves.append(Move((r, c), (r + 1, c - 1), self.board))
            elif (r + 1, c - 1) == self.enpassantPossible:
                moves.append(Move((r, c), (r + 1, c - 1), self.board, isEnpassantMove=True))
        if c + 1 <= 7:  # Capture to right
            if self.board[r + 1][c + 1][0] == 'w':
                moves.append(Move((r, c), (r + 1, c + 1), self.board))
            elif (r + 1, c + 1) == self.enpassantPossible:
                moves.append(Move((r, c), (r + 1, c + 1), self.board, isEnpassantMove=True))
