from ..moves import Move

""" Get all the Knight moves located at (row, col) and add them to the list """


def getKnightMoves(self, r, c, moves):
    knight_moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
    ally_color = "w" if self.whiteToMove else "b"
    for m in knight_moves:
        end_row = r + m[0]
        end_col = c + m[1]
        if 0 <= end_row < 8 and 0 <= end_col < 8:
            end_piece = self.board[end_row][end_col]
            if end_piece[0] != ally_color:  # not an ally piece (empty or enemy piece)
                moves.append(Move((r, c), (end_row, end_col), self.board))
