import PIL.Image


from manga_ocr import MangaOcr

mocr = MangaOcr()
img = PIL.Image.open(('./ss/2023-10-27_09-32.png'))
text = mocr(img)


print(text)
