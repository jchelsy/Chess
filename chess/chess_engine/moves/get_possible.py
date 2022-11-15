""" All moves without considering checks """


def getAllPossibleMoves(self):
    moves = []
    for r in range(len(self.board)):  # number of rows
        for c in range(len(self.board[r])):  # number of cols in given row
            turn = self.board[r][c][0]
            if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                piece = self.board[r][c][1]
                self.moveFunctions[piece](r, c, moves)  # Calls the appropriate moves function based on piece type
    return moves
