
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getPlaylistInformation(playlistId, userName):
    print("getting playlist information")
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    #limit 100 for the time being
    playlist = sp.user_playlist(userName, playlistId, fields='tracks')

    #filtering the playlist object into just that data we want

    playlist = playlist['tracks']

    if playlist['total'] > 100:
        print("ERROR: Playlist over 100 songs, I haven't done pagination yet so only playlist of 100 songs or less please.")
        exit()


    playlist = playlist['items']


    trackArray = []

    for current in playlist:
        artistName = current["track"]["artists"][0]["name"]
        trackName = current["track"]["name"]
        albumImageUrl = current["track"]["album"]["images"][0]["url"]
        albumImageHeight = current["track"]["album"]["images"][0]["height"]
        albumImageWidth = current["track"]["album"]["images"][0]["width"]
        albumName = current["track"]["album"]["name"]

        trackObject = {
            "artistName": artistName,
            "trackName": trackName,
            "albumImageUrl": albumImageUrl,
            "albumImageHeight": albumImageHeight,
            "albumImageWidth": albumImageWidth,
            "albumName": albumName,
        }

        trackArray.append(trackObject)

    return trackArray


def getStoreAlbumArt(albumArtUrl, storagePath):
    print("Storing Album Art")
