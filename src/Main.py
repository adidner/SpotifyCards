

from SpotifyApi import getPlaylistInformation
from SpotifyApi import getStoreAlbumArt
from BarCodeColorGeneration import generateStoreBarCodeBackground
from BarCodeColorGeneration import altGenerateStoreBarCodeBackground

from LayerImages import layerImage
from LayerImages import layerTrackAndArtistText
from LayerImages import createBackgroundImage
from LayerImages import getImgSize

from time import sleep


def main():
    print("starting script")

    #playlistId = "73yt8788Kl512Onxir8R6T?si=XWAVtz4ASd6qf7PVsoMpVA"
    playlistId = "6jIUdymXQAPTJDwhtOyvTT?si=UBdjaHAjQQGmSl09_oY4FA"
    userName = "ace50mon"
    backgoundImageName = "backgroundImage.png"
    totalHeight = 1233
    totalWidth = 822
    barcodeHeight = 160
    barcodeWidth = 640
    barcodeColor = ""

    # keys, artistName, trackName, albumImageUrl, albumImageHeight, albumImageWidth, albumName
    trackArray = getPlaylistInformation(playlistId, userName)
    print(trackArray)

    for i in range(0, len(trackArray)):
        currentTrack = trackArray[i]
        photoKey = currentTrack['photoKey']
        getStoreAlbumArt(currentTrack['albumImageUrl'], "albumArt", photoKey)
        createBackgroundImage(totalHeight, totalWidth, backgoundImageName)


        barcodeColor = generateStoreBarCodeBackground("./albumArt/" + photoKey, "barcodeArt",  photoKey, barcodeWidth, barcodeHeight)
        #altGenerateStoreBarCodeBackground("./albumArt/" + photoKey + ".png", currentTrack["photoKey"] + ".png")

        width,height = getImgSize("./albumArt/" + photoKey)

        layerImage(backgoundImageName, "./albumArt/" + photoKey, "merging",photoKey, 91,85)
        layerImage("./merging/" + photoKey , "./barcodeArt/" + photoKey ,"merging",photoKey, 91, 85 + height)
        red = barcodeColor[0]
        green = barcodeColor[1]
        blue = barcodeColor[2]
        if (red*0.299 + green*0.587 + blue*0.114) > 186:
            layerImage("./merging/" + photoKey, "./assets/black_barcode.png","merging",photoKey, 91, 725)
        else:
            layerImage("./merging/" + photoKey, "./assets/white_barcode.png","merging",photoKey, 91, 725)

        layerTrackAndArtistText("./merging/" + photoKey, currentTrack['trackName'], currentTrack['artistName'],
                                "./merging/" + photoKey, 55,
                                totalWidth, totalHeight - (725 + barcodeHeight), 725 + barcodeHeight)





    print("ending script")


main()
