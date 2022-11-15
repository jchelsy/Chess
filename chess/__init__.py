import os

cwd = os.path.dirname(os.path.realpath(__file__))
img_dir = os.path.join(cwd, 'resources', 'images')
# print(cwd)
# print(img_dir)


def colorCode(code: str): return '\033[' + code


class C:
    RED = colorCode('91m')

    GREEN = colorCode('92m')
    YELLOW = colorCode('93m')
    BLUE = colorCode('94m')
    PINK = colorCode('95m')

    END = colorCode('0m')  # reset
