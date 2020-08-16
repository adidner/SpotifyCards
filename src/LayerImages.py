from PIL import ImageFont
from PIL import ImageDraw
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


def layerTrackAndArtistText(fileInPath, trackName, artistName, fileOutPath, fontsize, xTotal, yTotal, yoffset):
    print("layering Text")

    img = Image.open(fileInPath)
    draw = ImageDraw.Draw(img)
    fontTrack = ImageFont.truetype('arial', fontsize)
    fontArtist = ImageFont.truetype('arial', fontsize - 10)
    w_artist,h_artist = draw.textsize(artistName, fontArtist)
    w_track,h_track = draw.textsize(trackName, fontTrack)
    center_height = ((yTotal - (h_track + h_artist)) / 2) + yoffset
    draw.text(((xTotal-w_track)/2, center_height - h_track), trackName, (255, 255, 255), font=fontTrack)
    draw.text(((xTotal-w_artist)/2, center_height + h_artist), artistName, (168, 168, 168), font=fontArtist)
    img.save(fileOutPath)
