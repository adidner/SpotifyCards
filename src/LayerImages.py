from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
import os
import itertools

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

    artist_divisions = 0
    track_divisions = 0
    width_limit = 640
    img = Image.open(fileInPath)
    draw = ImageDraw.Draw(img)
    trackColor = (255, 255, 255)
    artistColor = (168, 168, 168)
    fontTrack = ImageFont.truetype('arial', fontsize)
    fontArtist = ImageFont.truetype('arial', fontsize - 10)

    artistNameArray = [artistName]
    trackNameArray = [trackName]

    artist_size_array = []
    w_artist,h_artist = draw.textsize(artistName, fontArtist)
    artist_size_array.append((w_artist,h_artist))
    track_size_array = []

    w_track,h_track = draw.textsize(trackName, fontTrack)
    track_size_array.append((w_track,h_track))

    smartBreak = False

    while True:

        #try to divide in a place that makes sense, if we're dividing in 2 and we can
        if artist_divisions == 1:
            makeSenseVars = ['(', '-', '/']
            for current in makeSenseVars:
                if current in artistName:
                    artistNameArray = artistName.split(current)
                    artistNameArray[1] = current + artistNameArray[1]
                    if checkStillToWide(artistNameArray, width_limit, fontArtist, draw) == False:
                        smartBreak = True
                        break
        if smartBreak:
            break
        startIndexArray = getStartIndexsBasedOnDivisions(artist_divisions, len(artistName))
        divisionalSpaces = []
        for current in startIndexArray:
            divisionalSpaces.append(getNearestSpace(artistName, current))
        print(divisionalSpaces)
        artistNameArray = getArrayOfWordsBasedOnArrayDivionalIndexs(divisionalSpaces, artistName)
        if checkStillToWide(artistNameArray, width_limit, fontArtist, draw) == False:
            break
        artist_divisions += 1


    smartBreak = False
    #the exact same code for artist but with slightly different variables, should probably be a function at that point
    while True:

        #try to divide in a place that makes sense, if we're dividing in 2 and we can
        if track_divisions == 1:
            makeSenseVars = ['(', '-', '/']
            for current in makeSenseVars:
                if current in trackName:
                    trackNameArray = trackName.split(current)
                    trackNameArray[1] = current + trackNameArray[1]
                    print(trackNameArray)
                    if checkStillToWide(trackNameArray, width_limit, fontTrack, draw) == False:
                        print("in if")
                        smartBreak = True
                        break
        if smartBreak:
            break
        startIndexArray = getStartIndexsBasedOnDivisions(track_divisions, len(trackName))
        divisionalSpaces = []
        for current in startIndexArray:
            divisionalSpaces.append(getNearestSpace(trackName, current))
        trackNameArray = getArrayOfWordsBasedOnArrayDivionalIndexs(divisionalSpaces, trackName)
        if checkStillToWide(trackNameArray, width_limit, fontTrack, draw) == False:
            break
        track_divisions += 1

    #now again but with arrays and division
    #center_height = ((yTotal - (h_track + h_artist)) / 2) + yoffset
    #draw.text(((xTotal-w_track)/2, center_height - h_track), trackName, trackColor, font=fontTrack)
    #draw.text(((xTotal-w_artist)/2, center_height + h_artist), artistName, artistColor, font=fontArtist)



    placementOfWords = getStartIndexsBasedOnDivisions(len(trackNameArray) + len(artistNameArray), yTotal)
    placementOfWordsCounter = 0
    track_size_array = convertTextArrayToSizeArray(trackNameArray, fontTrack, draw)

    for (current,(w_track,h_track)) in zip(trackNameArray,track_size_array):
        draw.text(((xTotal-w_track)/2, placementOfWords[placementOfWordsCounter] + yoffset - h_track), current, trackColor, font=fontTrack)
        placementOfWordsCounter += 1

    artist_size_array = convertTextArrayToSizeArray(artistNameArray, fontArtist, draw)
    for (current,(w_artist,h_artist)) in zip(artistNameArray,artist_size_array):
        draw.text(((xTotal-w_artist)/2, placementOfWords[placementOfWordsCounter] + yoffset - h_artist), current, artistColor, font=fontArtist)
        placementOfWordsCounter += 1

    print(trackNameArray)
    print(track_size_array)
    print(artistNameArray)
    print(artist_size_array)
    print(placementOfWords)

    img.save(fileOutPath)

def getArrayOfWordsBasedOnArrayDivionalIndexs(divisionalIndexs, word):
    if len(divisionalIndexs) == 0 or (len(divisionalIndexs) == 1 and divisionalIndexs[0] == -1):
        return [word]
    prev = 0
    current = divisionalIndexs[0]
    arrayOfBrokenWords = []
    counter = 0
    while counter < len(divisionalIndexs):
        current = divisionalIndexs[counter]
        arrayOfBrokenWords.append(word[prev:current])
        prev = current
        counter += 1
    arrayOfBrokenWords.append(word[current + 1: len(word)])
    return arrayOfBrokenWords

def getNearestSpace(word, startIndex):
    if word[startIndex] == " ":
        return startIndex
    trigger = True
    positiveDirection = startIndex
    negativeDirection = startIndex
    while trigger:
        positiveDirection += 1
        negativeDirection -= 1
        if positiveDirection > len(word) - 1:
            #throw an error?
            print("No divisional place")
            return -1
        if negativeDirection < 0:
            #throw another error?
            print("No divisional place")
            return -1
        if word[positiveDirection] == " ":
            return positiveDirection
        if word[negativeDirection] == " ":
            return negativeDirection


def getStartIndexsBasedOnDivisions(numberDivisions, wordLen):
    startIndexArray = []
    fraction = numberDivisions + 1
    baseAdd = int(wordLen/fraction)
    current = 0
    for i in range(0, numberDivisions):
        current += baseAdd
        startIndexArray.append(current)
    return startIndexArray



def convertTextArrayToSizeArray(text_array,font,draw):
    size_array = []
    for current in text_array:
        w,h = draw.textsize(current, font)
        size_array.append((w,h))
    return size_array

def checkStillToWide(text_array, width_limit, font, draw):
    size_array = convertTextArrayToSizeArray(text_array,font, draw)
    for current in size_array:
        if current[0] > width_limit:
            return True
    return False


def getImgSize(path):
    image = Image.open(path)
    width, height = image.size
    print(width,height)
    return (width,height)
