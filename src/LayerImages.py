from PIL import Image


def createBackgroundImage(height, width, backgoundImageName):
    img = Image.new('RGB', (width,height), (0, 0, 0))
    img.save(backgoundImageName, "PNG")

def layerImage(currentImageToLayerOn, imagePathToLayer):
    print("layering Image")

def layerText(currentImageToLayerOn, textToLayer):
    print("layering Text")
