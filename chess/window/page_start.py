from .widgets import ImageButton
import tkinter as tk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.background = tk.Canvas(self, width=918, height=612, bg="black",
                                    borderwidth=0, highlightthickness=0)
        self.background.grid(row=0, column=0, padx=0, pady=0)
        self.background.create_image(0, 0, image=self.controller.images['title_bg'], anchor="nw")

        self.btn_newgame = ImageButton(self.background, self.controller, x=10, y=360, width=250, height=75, anchor="nw",
                                       default="newgame_default", hover="newgame_hover", active="newgame_click",
                                       command="NewGame")

    def menubar(self):
        # Create Menubar
        menubar = tk.Menu(self.controller)
        # Create 'File' dropdown
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Quit", command=self.controller.destroy)
        # Add 'File' dropdown to the menubar
        menubar.add_cascade(label="File", menu=filemenu)

        return menubar
