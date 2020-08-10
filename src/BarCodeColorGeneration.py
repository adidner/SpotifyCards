
from PIL import Image
from collections import defaultdict
import os


def generateStoreBarCodeBackground(albumArtPath,storagePath, photoKey, x, y):
    print("Generate store barcode background")

    try:
        os.mkdir(storagePath)
    except OSError:
        print ("")

    im = Image.open(albumArtPath)
    by_color = defaultdict(int)
    for pixel in im.getdata():
        by_color[pixel] += 1

    r = 0
    g = 0
    b = 0
    size = len(by_color.keys())
    for color in by_color.keys():
        r += color[0]
        g += color[1]
        b += color[2]

    r = int(r/size)
    g = int(g/size)
    b = int(b/size)

    img = Image.new('RGB', (x,y), (r, g, b))
    img.save(storagePath + "/" + photoKey, "PNG")



def altGenerateStoreBarCodeBackground(albumArtPath,storagePath):
    im = Image.open(albumArtPath)
    by_color = defaultdict(int)
    r = 0
    g = 0
    b = 0
    for pixel in im.getdata():
         r += pixel[0]
         g += pixel[1]
         b += pixel[2]

    size = len(im.getdata())
    r = int(r/size)
    g = int(g/size)
    b = int(b/size)
    img = Image.new('RGB', (100,100), (r, g, b))
    img.save(storagePath, "PNG")
