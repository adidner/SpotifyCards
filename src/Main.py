

from SpotifyApi import getPlaylistInformation
from SpotifyApi import getStoreAlbumArt
from BarCodeColorGeneration import generateStoreBarCodeBackground
from BarCodeColorGeneration import altGenerateStoreBarCodeBackground

from LayerImages import layerImage
from LayerImages import layerText
from LayerImages import createBackgroundImage


def main():
    print("starting script")

    playlistId = "73yt8788Kl512Onxir8R6T?si=XWAVtz4ASd6qf7PVsoMpVA"
    userName = "ace50mon"
    backgoundImageName = "backgroundImage.png"
    totalHeight = 1233
    totalWidth = 822

    # keys, artistName, trackName, albumImageUrl, albumImageHeight, albumImageWidth, albumName
    trackArray = getPlaylistInformation(playlistId, userName)
    print(trackArray)

    for i in range(0, len(trackArray)):
        photoKey = trackArray[i]['photoKey']
        getStoreAlbumArt(trackArray[i]['albumImageUrl'], "albumArt", photoKey)
        createBackgroundImage(totalHeight, totalWidth, backgoundImageName)


        generateStoreBarCodeBackground("./albumArt/" + photoKey, "barcodeArt",  photoKey, 640, 125)
        #altGenerateStoreBarCodeBackground("./albumArt/" + photoKey + ".png", trackArray[i]["photoKey"] + ".png")

        layerImage(backgoundImageName, "./albumArt/" + photoKey, "merging",photoKey, 91,85)
        layerImage("./merging/" + photoKey , "./barcodeArt/" + photoKey ,"merging",photoKey, 91,725)

        



    #Get playlist song list

        #Grab song 1

        #Grab artist, title, album art (/download album art as saved image)

        #generate barcode background

        #layer images

            #layer album

            #layer barcode background

            #layer barcode logo and barcode

            #layer Text and Text

    print("ending script")


main()
