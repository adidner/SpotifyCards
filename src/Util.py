
import os

def makeFolderBasedOnPath(targetPath):
    directory = targetPath.split("/")[1]
    try:
        os.mkdir(directory)
    except OSError:
        print ("")
