""" Get all Queen moves located at (row, col) and add them to the list """


def getQueenMoves(self, r, c, moves):
    self.getRookMoves(r, c, moves)
    self.getBishopMoves(r, c, moves)
