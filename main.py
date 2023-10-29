import PIL.Image

from manga_ocr import MangaOcr

from mss import mss

import os
import glob
from PIL import Image


def a():
    mocr = MangaOcr()
    img = PIL.Image.open(('./ss/2023-10-27_09-32.png'))
    text = mocr(img)
    print(text)


def ap(file):
    mocr = MangaOcr()
    img = PIL.Image.open((file))
    text = mocr(img)
    print(text)


# list all images in a directory
def list_all_images():
    os.chdir("./ss")
    for file in glob.glob("*.png"):
        print(file)
        ap(file)
        # img = Image.open(file)
        # img.show()


def __main__():
    with mss() as sct:
        sct.shot()


if __name__ == '__main__':
    # __main__()
    list_all_images()
