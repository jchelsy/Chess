import tkinter as tk


class ChessPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # White Sidebar
        self.sidebar_white = tk.Canvas(self, width=153, height=612, bg="black",
                                       borderwidth=0, highlightthickness=0)
        self.sidebar_white.grid(row=0, column=0, padx=0, pady=0)
        self.sidebar_white.create_image(0, 0, image=self.controller.images['w_sidebar'], anchor="nw")

        # Black Sidebar
        self.sidebar_black = tk.Canvas(self, width=153, height=612, bg="black",
                                       borderwidth=0, highlightthickness=0)
        self.sidebar_black.grid(row=0, column=2, padx=0, pady=0)
        self.sidebar_black.create_image(0, 0, image=self.controller.images['b_sidebar'], anchor="nw")

        # Board Border
        self.canvas = tk.Canvas(self, width=612, height=612, bg="black",
                                borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=1, padx=0, pady=0)
        self.canvas.create_image(0, 0, image=self.controller.images['border'], anchor="nw")

        self.canvas.bind("<Button-1>", self.controller.square_clicked)  # left-click event

        # Status Label  (530, 593)
        self.info_label = self.canvas.create_text(self.controller.status_pos_x, self.controller.status_pos_y,
                                                  font=self.controller.font_status, fill="white",
                                                  text="  White's turn!  ", tags="text", anchor="center")

    def menubar(self):
        # Create Menubar
        menubar = tk.Menu(self.controller)
        # Create 'File' dropdown
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Game", command=self.controller.new_game)
        filemenu.add_command(label="Undo", command=self.controller.undo_move)
        # Add 'File' dropdown to the menubar
        menubar.add_cascade(label="File", menu=filemenu)

        return menubar
