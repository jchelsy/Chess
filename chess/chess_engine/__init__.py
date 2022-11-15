# Classes
from .moves import Move
from .castling import CastleRights
# Methods
from .moves import makeMove, undoMove, getValidMoves, getAllPossibleMoves, squareUnderAttack, inCheck
from .castling import updateCastleRights, getCastleMoves, getKingsideCastleMoves, getQueensideCastleMoves
from .pieces import getKingMoves, getQueenMoves, getRookMoves, getKnightMoves, getBishopMoves, getPawnMoves

"""
This class is responsible for storing all information about the current state of the chess game.
It is also responsible for determining valid moves at the current state & keeping a log of moves.
"""


class GameState:
    def __init__(self):
        self.board = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                      ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                      ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        self.moveFunctions = {'p': self.getPawnMoves, 'R': self.getRookMoves, 'N': self.getKnightMoves,
                              'B': self.getBishopMoves, 'Q': self.getQueenMoves, 'K': self.getKingMoves}

        self.whiteToMove = True
        self.moveLog = []
        self.whiteKingLocation = (7, 4)
        self.blackKingLocation = (0, 4)
        self.checkmate = False
        self.stalemate = False

        self.enpassantPossible = ()  # coords where en passant capture is possible
        self.currentCastlingRight = CastleRights(True, True, True, True)
        self.castleRightsLog = [CastleRights(self.currentCastlingRight.wks, self.currentCastlingRight.bks,
                                             self.currentCastlingRight.wqs, self.currentCastlingRight.bqs)]

    """ Takes a Move as a parameter and executes it """
    def makeMove(self, MOVE):
        return makeMove(self, MOVE)

    """ Undo the last move made """
    def undoMove(self):
        return undoMove(self)

    """ Update the castle rights (given the move) """
    def updateCastleRights(self, MOVE):
        return updateCastleRights(self, MOVE)

    """ All moves (considering checks) """
    def getValidMoves(self):
        return getValidMoves(self)

    """ Determine if the current player is in check """
    def inCheck(self):
        return inCheck(self)

    """ Determine if the enemy can attack the square (row, col) """
    def squareUnderAttack(self, ROW, COL):
        return squareUnderAttack(self, ROW, COL)

    """ All moves without considering checks """
    def getAllPossibleMoves(self):
        return getAllPossibleMoves(self)

    """ Get all the pawn moves located at (r, c) and add these moves to the list """
    def getPawnMoves(self, ROW, COL, MOVES):
        return getPawnMoves(self, ROW, COL, MOVES)

    """ Get all Rook moves located at (r, c) and add these moves to the list """
    def getRookMoves(self, ROW, COL, MOVES):
        return getRookMoves(self, ROW, COL, MOVES)

    """ Get all the Knight moves located at (r, c) and add these moves to the list """
    def getKnightMoves(self, ROW, COL, MOVES):
        return getKnightMoves(self, ROW, COL, MOVES)

    """ Get all the Bishop moves located at (r, c) and add these moves to the list """
    def getBishopMoves(self, ROW, COL, MOVES):
        return getBishopMoves(self, ROW, COL, MOVES)

    """ Get all Queen moves located at (r, c) and add these moves to the list """
    def getQueenMoves(self, ROW, COL, MOVES):
        return getQueenMoves(self, ROW, COL, MOVES)

    """ Get all King moves located at (r, c) and add these moves to the list """
    def getKingMoves(self, ROW, COL, MOVES):
        return getKingMoves(self, ROW, COL, MOVES)

    def getCastleMoves(self, ROW, COL, MOVES):
        return getCastleMoves(self, ROW, COL, MOVES)

    def getKingsideCastleMoves(self, ROW, COL, MOVES):
        return getKingsideCastleMoves(self, ROW, COL, MOVES)

    def getQueensideCastleMoves(self, ROW, COL, MOVES):
        return getQueensideCastleMoves(self, ROW, COL, MOVES)
