

from SpotifyApi import getPlaylistInformation
from SpotifyApi import getStoreAlbumArt
from BarCodeColorGeneration import generateStoreBarCodeBackground
from LayerImages import layerImage
from LayerImages import layerText
from LayerImages import createBackgroundImage


def main():
    print("starting script")

    playlistId = "73yt8788Kl512Onxir8R6T?si=XWAVtz4ASd6qf7PVsoMpVA"
    userName = "ace50mon"
    backgoundImageName = "backgroundImage.png"
    totalHeight = 1200
    totalWidth = 700

    # keys, artistName, trackName, albumImageUrl, albumImageHeight, albumImageWidth, albumName
    trackArray = getPlaylistInformation(playlistId, userName)
    print(trackArray)

    getStoreAlbumArt(trackArray[0]['albumImageUrl'], "albumArt", trackArray[0]['photoKey'])
    createBackgroundImage(totalHeight, totalWidth, backgoundImageName)

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
