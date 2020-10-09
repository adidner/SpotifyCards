# SpotifyCards

### Description:

Project designed to create a set of 4x6 images featuring album art, artist name and song title corresponding to a song. One for each song in a Spotify Playlist using the spotify API and some python libraries (mainly PIL)

### Usage:

In `src/Constants.py` you will find a variable called `PLAYLIST_ID` which controlls which playlist is used for the creation process. You can get the playlist ID of any playlist by going into Spotify and getting a share link.

Run via `python Main.py` _from the src folder in a terminal_

All the output images will be put into the `src/merging` folder

Once you have all of those images output, you can easily go to a variety of sites and get your photos printed as 4x6's and sent to your house for cheap.

I got mine here https://photos3.walmart.com/about/prints# and then delivered to my local walmart for \$ 0.09 per 4x6 photo

### Installation:

Python https://www.python.org/downloads/
PIL python library `pip install PIL`
spotify python spotify API wrapper `pip install spotipy`
