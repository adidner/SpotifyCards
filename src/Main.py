

from SpotifyApi import getPlaylistInformation
from SpotifyApi import getStoreAlbumArt
from BarCodeColorGeneration import generateStoreBarCodeBackground
from BarCodeColorGeneration import altGenerateStoreBarCodeBackground

from LayerImages import layerImage
from LayerImages import layerTrackAndArtistText
from LayerImages import createBackgroundImage


def main():
    print("starting script")

    playlistId = "73yt8788Kl512Onxir8R6T?si=XWAVtz4ASd6qf7PVsoMpVA"
    userName = "ace50mon"
    backgoundImageName = "backgroundImage.png"
    totalHeight = 1233
    totalWidth = 822
    barcodeHeight = 125
    barcodeWidth = 640

    # keys, artistName, trackName, albumImageUrl, albumImageHeight, albumImageWidth, albumName
    trackArray = getPlaylistInformation(playlistId, userName)
    print(trackArray)

    for i in range(0, len(trackArray)):
        currentTrack = trackArray[i]
        photoKey = currentTrack['photoKey']
        getStoreAlbumArt(currentTrack['albumImageUrl'], "albumArt", photoKey)
        createBackgroundImage(totalHeight, totalWidth, backgoundImageName)


        generateStoreBarCodeBackground("./albumArt/" + photoKey, "barcodeArt",  photoKey, barcodeWidth, barcodeHeight)
        #altGenerateStoreBarCodeBackground("./albumArt/" + photoKey + ".png", currentTrack["photoKey"] + ".png")

        layerImage(backgoundImageName, "./albumArt/" + photoKey, "merging",photoKey, 91,85)
        layerImage("./merging/" + photoKey , "./barcodeArt/" + photoKey ,"merging",photoKey, 91,725)

        layerTrackAndArtistText("./merging/" + photoKey, currentTrack['trackName'], currentTrack['artistName'],
                                "./merging/" + photoKey, 55,
                                totalWidth, totalHeight - (725 + barcodeHeight), 725 + barcodeHeight)


    print("ending script")


main()
