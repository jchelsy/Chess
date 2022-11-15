from ..chess_engine import GameState, Move
from .page_start import StartPage
from .page_chess import ChessPage
import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
import os

from chess import C
from chess import img_dir


class Control(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Chess")
        self.resizable(0, 0)

        # Set default fonts
        self.font_small = tkfont.Font(self, size=12, family="Cambria")
        self.font_medium = tkfont.Font(self, size=14, family="Cambria")
        self.font_title = tkfont.Font(self, size=16, family="Tw Cen MT Condensed", weight="bold")
        self.font_status = tkfont.Font(family="Helvetica", size=18)

        """ ==================
             Board Dimensions
            ================== """
        self.size = 8  # 8x8 board

        self.initial_boardLength = 4096
        self.initial_boardOutline = 800
        self.initial_sidebarWidth = 1224

        self.boardLength = self.initial_boardLength // self.size  # 512
        self.boardOutline = self.initial_boardOutline // self.size  # 100
        self.sidebarWidth = self.initial_sidebarWidth // self.size  # 153

        self.tileLength = self.boardLength // self.size  # 64
        # Status Label Pos | x=530, y=593.25 (594)
        self.status_pos_x = int((self.boardLength + (self.boardOutline // 2)) - (self.tileLength // 2))
        self.status_pos_y = int(self.boardLength + self.boardOutline - (((self.boardOutline // 2) * 0.75) // 2))

        """ Images """
        self.images = {}  # title_bg, w_tile, b_tile, w_sidebar, b_sidebar
        self.load_images()

        """ ======================
             Initialize All Pages
            ====================== """
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.p1 = StartPage(self.container, self)
        self.p2 = ChessPage(self.container, self)

        self.p1.grid(row=0, column=0, sticky="nsew")
        self.p2.grid(row=0, column=0, sticky="nsew")
        self.frames = {"StartPage": self.p1, "ChessPage": self.p2}

        self.show_frame("StartPage")

        """ ============================
             Initialize Chess Variables
            ============================ """
        self.gs = GameState()
        self.valid_moves = self.gs.getValidMoves()

        self.move_made = False  # flag variable for when a move is made
        self.animate = False  # flag variable for when a move should be animated

        self.selected = ()
        self.player_clicks = []
        self.game_over = False

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

        menubar = frame.menubar()
        self.configure(menu=menubar)

    def draw_gamestate(self):
        self.p2.canvas.delete("board")
        self.p2.canvas.delete("highlight")
        self.p2.canvas.delete("pieces")

        self.draw_board()
        self.draw_pieces()
        self.highlight_board(self.selected)

        self.p2.canvas.tag_raise("text")

    def draw_board(self):
        tiles = [self.images['w_tile'], self.images['b_tile']]
        for row in range(self.size):
            for col in range(self.size):
                tile = tiles[((row + col) % 2)]
                x = (col * self.tileLength) + (self.boardOutline // 2)
                y = (row * self.tileLength) + (self.boardOutline // 2)
                self.p2.canvas.create_image(x, y, image=tile, tags="board", anchor="nw")

    def draw_pieces(self):
        for row in range(self.size):
            for col in range(self.size):
                piece = self.gs.board[row][col]
                if piece != "--":  # not an empty space:
                    x = (col * self.tileLength) + (self.boardOutline // 2)
                    y = (row * self.tileLength) + (self.boardOutline // 2)
                    self.p2.canvas.create_image(x, y, image=self.images[piece], anchor="nw", tags=(piece, "pieces"))

    def highlight_board(self, selected):
        if selected != ():
            row, col = selected
            print("\n(" + str(col) + ", " + str(row) + ")")

            # Is the selected piece the color of the current turn?
            if self.gs.board[row][col][0] == ('w' if self.gs.whiteToMove else 'b'):
                x = (col * self.tileLength) + (self.boardOutline // 2)
                y = (row * self.tileLength) + (self.boardOutline // 2)
                self.p2.canvas.create_image(x, y, image=self.images['circle_negative_green'], anchor="nw",
                                            tags="highlight")
                for move in self.valid_moves:
                    if move.startRow == row and move.startCol == col:
                        print(C.BLUE + "(" + str(move.startCol) + ", " + str(move.startRow) + ")" + C.END, end=" --> ")
                        x = (move.endCol * self.tileLength) + (self.boardOutline // 2)
                        y = (move.endRow * self.tileLength) + (self.boardOutline // 2)

                        ally_color = 'w' if self.gs.whiteToMove else 'b'
                        end_piece = self.gs.board[move.endRow][move.endCol]
                        if end_piece != "--" and end_piece[0] != ally_color:
                            print(C.RED + "(" + str(move.endCol) + ", " + str(move.endRow) + ")" + C.END)
                            self.p2.canvas.create_image(x, y, image=self.images['circle_big_yellow'], anchor="nw",
                                                        tags="highlight")
                        else:
                            print(C.GREEN + "(" + str(move.endCol) + ", " + str(move.endRow) + ")" + C.END)
                            self.p2.canvas.create_image(x, y, image=self.images['circle_small_green'], anchor="nw",
                                                        tags="highlight")
        if self.gs.inCheck():
            if self.gs.whiteToMove:
                x = (self.gs.whiteKingLocation[1] * self.tileLength) + (self.boardOutline // 2)
                y = (self.gs.whiteKingLocation[0] * self.tileLength) + (self.boardOutline // 2)
                self.p2.canvas.create_image(x, y, image=self.images['circle_big_red'], anchor="nw", tags="highlight")
            else:
                x = (self.gs.blackKingLocation[1] * self.tileLength) + (self.boardOutline // 2)
                y = (self.gs.blackKingLocation[0] * self.tileLength) + (self.boardOutline // 2)
                self.p2.canvas.create_image(x, y, image=self.images['circle_big_red'], anchor="nw", tags="highlight")

        self.p2.canvas.tag_raise("highlight")
        self.p2.canvas.tag_raise("pieces")

    def square_clicked(self, event):
        col = (event.x - (self.boardOutline // 2)) // self.tileLength
        row = (event.y - (self.boardOutline // 2)) // self.tileLength

        if not self.game_over:  # is there no check/stalemate?
            if 0 <= col <= 7 and 0 <= row <= 7:  # was a tile clicked? (inside the board area)
                if self.selected == (row, col):  # did the user click the same square twice?
                    self.selected = ()  # de-select
                    self.player_clicks = []
                else:
                    self.selected = (row, col)
                    self.player_clicks.append(self.selected)  # append for both 1st and 2nd clicks

                if len(self.player_clicks) == 2:  # after 2nd click
                    move = Move(self.player_clicks[0], self.player_clicks[1], self.gs.board)

                    for i in range(len(self.valid_moves)):
                        if move == self.valid_moves[i]:
                            self.gs.makeMove(self.valid_moves[i])
                            self.move_made = True
                            self.animate = True
                            self.selected = ()
                            self.player_clicks = []
                    if not self.move_made:  # update the 1st click (& remove the 2nd) if a move wasn't made
                        self.player_clicks = [self.selected]
            else:  # was an area outside the board clicked?
                self.selected = ()
                self.player_clicks = []

        self.shift()

    def shift(self):
        if self.move_made:
            if self.animate:
                self.animate_move(self.gs.moveLog[-1])
            self.valid_moves = self.gs.getValidMoves()
            self.move_made = False
            self.animate = False

        self.draw_gamestate()

        x = self.boardOutline // 2
        y = ((self.boardLength + self.boardOutline) // 2) - self.tileLength

        if self.gs.checkmate:  # is either color in checkmate? (game over)
            self.game_over = True
            # self.disable_undo()

            if self.gs.whiteToMove:  # is it white's turn? (black won)
                self.p2.canvas.create_image(x, y, image=self.images['b_checkmate'], anchor="nw", tags="title")
                self.p2.canvas.itemconfig(self.p2.info_label, text="  Black wins!  ", fill="black")

            else:  # or is it black's turn? (white won)
                self.p2.canvas.create_image(x, y, image=self.images['w_checkmate'], anchor="nw", tags="title")
                self.p2.canvas.itemconfig(self.p2.info_label, text="  White wins!  ", fill="white")

        elif self.gs.stalemate:  # or is there a stalemate? (game over)
            self.game_over = True
            self.p2.canvas.create_image(x, y, image=self.images['stalemate'], anchor="nw", tags="title")
            self.p2.canvas.itemconfig(self.p2.info_label, text="  Stalemate  ", fill="yellow")

        else:  # otherwise...
            self.update_status_label()  # update the label displaying the current turn

    def animate_move(self, move):
        pass

    def update_status_label(self):
        text = "  White's turn!  " if self.gs.whiteToMove else "  Black's turn!  "
        color = "white" if self.gs.whiteToMove else "black"
        self.p2.canvas.itemconfig(self.p2.info_label, text=text, fill=color)

    def new_game(self, event=None):
        self.game_over = False

        self.gs = GameState()  # reset the GameState
        self.valid_moves = self.gs.getValidMoves()
        self.selected = ()
        self.player_clicks = []
        self.move_made = False
        self.animate = False

        self.update_status_label()
        self.draw_gamestate()

    def undo_move(self, event=None):
        if not self.game_over and self.gs.moveLog:
            self.gs.undoMove()
            self.move_made = True
            self.animate = False
            self.update_status_label()
            self.draw_gamestate()

    def load_images(self):
        # Title Screen Background
        self.images['title_bg'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'ui', 'start_bg.png'))
                                                     .resize((918, 612), Image.ANTIALIAS))

        """ Board """
        # Border
        self.images['border'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'board', 'border.png'))
                                                   .resize((612, 612), Image.ANTIALIAS))
        # Tiles
        self.images['w_tile'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'board', 'tile_white.png'))
                                                   .resize((64, 64), Image.ANTIALIAS))
        self.images['b_tile'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'board', 'tile_black.png'))
                                                   .resize((64, 64), Image.ANTIALIAS))
        # Sidebars
        self.images['w_sidebar'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'board', 'side_white.png'))
                                                      .resize((153, 612), Image.ANTIALIAS))
        self.images['b_sidebar'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'board', 'side_black.png'))
                                                      .resize((153, 612), Image.ANTIALIAS))
        # Highlighting
        self.images['box_green'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'highlight', 'box_green.png'))
                                                      .resize((64, 64), Image.ANTIALIAS))
        self.images['box_yellow'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'highlight', 'box_yellow.png'))
                                                       .resize((64, 64), Image.ANTIALIAS))
        self.images['circle_big_green'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'highlight',
                                                                                     'circle_green_big.png'))
                                                             .resize((64, 64), Image.ANTIALIAS))
        self.images['circle_big_yellow'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'highlight',
                                                                                      'circle_yellow_big.png'))
                                                              .resize((64, 64), Image.ANTIALIAS))
        self.images['circle_big_red'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'highlight',
                                                                                   'circle_red_big.png'))
                                                           .resize((64, 64), Image.ANTIALIAS))
        self.images['circle_small_green'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'highlight',
                                                                                       'circle_green_small.png'))
                                                               .resize((64, 64), Image.ANTIALIAS))
        self.images['circle_negative_green'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'highlight',
                                                                                          'circle_green_neg.png'))
                                                                  .resize((64, 64), Image.ANTIALIAS))

        """ Pieces """
        pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
        for piece in pieces:
            self.images[piece] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'pieces', piece + ".png"))
                                                    .resize((64, 64), Image.ANTIALIAS))

        """ Text """
        self.images['b_checkmate'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'text', 'checkmate_black.png'))
                                                        .resize((512, 64), Image.ANTIALIAS))
        self.images['w_checkmate'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'text', 'checkmate_white.png'))
                                                        .resize((512, 64), Image.ANTIALIAS))
        self.images['stalemate'] = ImageTk.PhotoImage(Image.open(os.path.join(img_dir, 'text', 'stalemate.png'))
                                                      .resize((512, 64), Image.ANTIALIAS))
