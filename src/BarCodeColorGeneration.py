
from PIL import Image
from collections import defaultdict
import os
from Constants import BARCODE_WIDTH, BARCODE_HEIGHT


def generateStoreBarCodeBackground(albumArtPath,storagePath, photoKey):
    print("Generate store barcode background")

    try:
        os.mkdir(storagePath)
    except OSError:
        print ("")

    im = Image.open(open(albumArtPath, 'rb'))
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

    img = Image.new('RGB', (BARCODE_WIDTH, BARCODE_HEIGHT), (r, g, b))
    img.save(storagePath + "/" + photoKey, "PNG")
    return (r,g,b)
