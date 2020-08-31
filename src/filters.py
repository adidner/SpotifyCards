


def removeInvalidFilenameCharacters(filename):
    filename = filename.replace("#","")
    filename = filename.replace("%","")
    filename = filename.replace("&","")
    filename = filename.replace("{","")
    filename = filename.replace("}","")
    filename = filename.replace("\\","")
    filename = filename.replace("<","")
    filename = filename.replace(">","")
    filename = filename.replace("*","")
    filename = filename.replace("?","")
    filename = filename.replace("/","")
    filename = filename.replace("'","")
    filename = filename.replace("\"","")
    filename = filename.replace(":","")
    filename = filename.replace("@","")
    filename = filename.replace("+","")
    filename = filename.replace("`","")
    filename = filename.replace("|","")
    filename = filename.replace("=","")

    return filename
