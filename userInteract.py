from addThings import AddPage, AddPost, DelPage, DelPost
from parsers import JSONToDict

def AddPostOrPage(type, fileList):
    if (type == "page"):
        for file in fileList:
            AddPage(file)
    elif (type == "post"):
        for file in fileList:
            AddPost(file)

def DelPostOrPage(type, fileList):
    if (type == "page"):
        for file in fileList:
            DelPage(file)
    elif (type == "post"):
        for file in fileList:
            DelPost(file)

                