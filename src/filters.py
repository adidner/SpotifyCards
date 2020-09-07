


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


def removeTrackExcess(trackname):
    if "(feat" in trackname:
        return trackname.partition("(")[0]
    if "- From" in trackname:
        return trackname.partition("-")[0]
    if "- Radio Edit" in trackname:
        return trackname.partition("-")[0]
    if "- Remastered" in trackname:
        return trackname.partition("-")[0]
    if "- 2011 Mix" in trackname:
        return trackname.partition("-")[0]
    if "- Rerecorded" in trackname:
        return trackname.partition("-")[0]

    return trackname
