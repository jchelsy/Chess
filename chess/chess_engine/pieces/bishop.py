from ..moves import Move

""" Get all the Bishop moves located at (row, col) and add them to the list """


def getBishopMoves(self, r, c, moves):
    directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))  # 4 diagonals
    enemy_color = "b" if self.whiteToMove else "w"
    for d in directions:
        for i in range(1, 8):  # Bishop can moves max of 7 squares
            end_row = r + d[0] * i
            end_col = c + d[1] * i
            if 0 <= end_row < 8 and 0 <= end_col < 8:  # on board
                end_piece = self.board[end_row][end_col]
                if end_piece == "--":  # empty space valid
                    moves.append(Move((r, c), (end_row, end_col), self.board))
                elif end_piece[0] == enemy_color:  # enemy piece valid
                    moves.append(Move((r, c), (end_row, end_col), self.board))
                    break
                else:  # friendly piece invalid
                    break
            else:  # off board
                break
