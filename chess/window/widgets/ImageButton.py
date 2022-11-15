import os
from PIL import Image, ImageTk

from chess import img_dir
btn_dir = os.path.join(img_dir, 'ui', 'buttons')


class ImageButton:
    def __init__(self, canvas, controller, **kwargs):
        self.canvas = canvas
        self.controller = controller

        x = kwargs.get('x', 0)
        y = kwargs.get('y', 0)
        anchor = kwargs.get('anchor', "center")
        width = kwargs.get('width', 50)
        height = kwargs.get('height', width)
        state = kwargs.get('state', "normal")
        if 'tags' in kwargs:
            tags = kwargs.get('tags')

        # Default Image
        self.default = ImageTk.PhotoImage(
            Image.open(
                os.path.join(btn_dir, kwargs.get('default', "blank_default") + ".png")
            ).resize((width, height), Image.ANTIALIAS)
        )
        # Hovered Image
        self.hover = ImageTk.PhotoImage(
            Image.open(
                os.path.join(btn_dir, kwargs.get('hover', "blank_hover") + ".png")
            ).resize((width, height), Image.ANTIALIAS)
        )
        # Clicked Image
        self.active = ImageTk.PhotoImage(
            Image.open(
                os.path.join(btn_dir, kwargs.get('active', "blank_click") + ".png")
            ).resize((width, height), Image.ANTIALIAS)
        )
        # Disabled Image
        self.disabled = ImageTk.PhotoImage(
            Image.open(
                os.path.join(btn_dir, kwargs.get('disabled', "blank_click") + ".png")
            )
        )

        self.button = canvas.create_image(x, y, anchor=anchor, state=state, image=self.default)

        canvas.tag_bind(self.button, "<Enter>", self.mouse_hover)
        canvas.tag_bind(self.button, "<Leave>", self.mouse_unhover)
        canvas.tag_bind(self.button, "<Button-1>", self.mouse_down)
        canvas.tag_bind(self.button, "<ButtonRelease-1>", self.mouse_up)

        self.command = kwargs.get('command', None)

    def mouse_hover(self, event=None):
        self.canvas.itemconfig(self.button, image=self.hover)

    def mouse_unhover(self, event=None):
        self.canvas.itemconfig(self.button, image=self.default)

    def mouse_down(self, event=None):
        self.canvas.itemconfig(self.button, image=self.active)

    def mouse_up(self, event=None):
        self.canvas.itemconfig(self.button, image=self.hover)  # mouse up and still hovering

        if self.command is not None:
            if self.command == "NewGame":
                self.controller.show_frame("ChessPage")
                self.controller.draw_gamestate()
