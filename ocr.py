

import easyocr
import glob

reader = easyocr.Reader(['ja'])



# list all images in a directory
def list_all_images():
    files = []
    for file in glob.glob("./ss/words/*.png"):
        files.append(file)
    return files

def to_text(file):
    result = reader.readtext(file, detail=0)
    return result

def __main__():
    for file in list_all_images():
        print(file, to_text(file))


if __name__ == '__main__':
    __main__()