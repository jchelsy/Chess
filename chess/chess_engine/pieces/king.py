from ..moves import Move

""" Get all King moves located at (row, col) and add them to the list """


def getKingMoves(self, r, c, moves):
    king_moves = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    ally_color = "w" if self.whiteToMove else "b"
    for i in range(8):
        end_row = r + king_moves[i][0]
        end_col = c + king_moves[i][1]
        if 0 <= end_row < 8 and 0 <= end_col < 8:
            end_piece = self.board[end_row][end_col]
            if end_piece[0] != ally_color:  # not an ally piece (empty or enemy piece)
                moves.append(Move((r, c), (end_row, end_col), self.board))
