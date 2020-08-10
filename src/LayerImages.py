from PIL import Image
import os

def createBackgroundImage(height, width, backgoundImageName):
    img = Image.new('RGB', (width,height), (0, 0, 0))
    img.save(backgoundImageName, "PNG")

def layerImage(backgroundPath, foregroundPath, storagePath,photoKey, x, y):
    print("layering Image")

    try:
        os.mkdir(storagePath)
    except OSError:
        print ("")

    background = Image.open(backgroundPath)
    foreground = Image.open(foregroundPath)

    background.paste(foreground, (x, y), foreground.convert('RGBA'))
    background.save(storagePath + "/" + photoKey)


def layerText(currentImageToLayerOn, textToLayer):
    print("layering Text")
