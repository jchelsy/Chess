import os
from .window import Control
from chess import cwd


def run():
    root = Control()
    root.geometry("%dx%d" % (918, 612))
    root.iconbitmap(os.path.join(cwd, "icon.ico"))
    root.mainloop()


# if __name__ == "__main__":
#     run()
