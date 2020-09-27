from SpotifyApi import getPlaylistInformation, getStoreAlbumArt
from BarCodeColorGeneration import generateStoreBarCodeBackground
from LayerImages import layerImage, layerTrackAndArtistText, createBackgroundImage, getImgSize, layerBarcodeImage
from time import sleep
from Constants import *

def main():
    print("starting script")

    # keys, artistName, trackName, albumImageUrl, albumImageHeight, albumImageWidth, albumName
    spotify_object_array = getPlaylistInformation()
    print(spotify_object_array)

    for i in range(0, len(spotify_object_array)):
        currentTrack = spotify_object_array[i]
        photoKey = currentTrack['photoKey']

        albumArtName = "./albumArt/" + photoKey
        mergingName = "./merging/" + photoKey

        getStoreAlbumArt(currentTrack['albumImageUrl'], albumArtName)
        createBackgroundImage()

        red, green, blue = generateStoreBarCodeBackground(albumArtName, "barcodeArt",  photoKey)

        album_width,album_height = getImgSize(albumArtName)

        TOP_PADDING_AND_IMAGE = TOP_PADDING + album_height

        layerImage(BACKGROUND_IMAGE_NAME, albumArtName, mergingName, LEFT_PADDING,TOP_PADDING)
        layerImage(mergingName, "./barcodeArt/" + photoKey, mergingName, LEFT_PADDING, TOP_PADDING + album_height)

        layerBarcodeImage(mergingName, LEFT_PADDING, TOP_PADDING_AND_IMAGE, red, green, blue)

        layerTrackAndArtistText(mergingName, currentTrack['trackName'], currentTrack['artistName'],
                                TOTAL_WIDTH, TOTAL_HEIGHT - (TOP_PADDING_AND_IMAGE + BARCODE_HEIGHT),
                                TOP_PADDING_AND_IMAGE + BARCODE_HEIGHT)

    print("ending script")

main()
