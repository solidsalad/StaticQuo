from addThings import AddPage, AddPost, DelPage, DelPost, AddWithPrefab
from parsers import JSONToDict
import os
from datetime import date

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

def FillPrefab(templateName, number=1, type="post"):
    #templateMdFile, fillData, fileName, type="post"
    if (os.path.isfile(f"templates/prefabs/{templateName}.md")):
        for i in range(number):
            print(f"file {i+1}:\n\n")
            data = FillDataDict(JSONToDict(f"templates/prefabs/{templateName}.JSON"))
            nameError = True
            while (nameError == True):
                fileName = input("what do you want this file to be called? ")
                if (" " in fileName) or ("/" in fileName):
                    print("your filename contains spaces and/or slashes, please pick a valid name")
                elif (fileName in JSONToDict(f"{type}s/{type}s.JSON")):
                    print("filename already in use")
                else:
                    nameError = False
            AddWithPrefab(f"{templateName}.md", data, fileName, type)
            #os.remove(f"{fileName}.md")
    else:
        print(f"template {templateName} not found")



def FillDataDict(emptyDict):
        filledDict = emptyDict
        for item in emptyDict:
            if (item == "date"):
                filledDict[item] = str(date.today())
            elif (isinstance(emptyDict[item], list)):
                if (len(emptyDict[item]) == 0):
                    print(f"time to add a list of {item} [answer 'stop' to stop]")
                    count = 1
                    listing = ""
                    while not (listing == "stop"):
                        listing = input(f"nr.{count}: ")
                        if not (listing == "stop"):
                            filledDict[item].append(listing)
                        count += 1
                else:
                    print(f"next, i want you to add {len(emptyDict[item])} {item}:")
                    filledDict[item] = FillDataList(emptyDict[item])
            elif not (isinstance(emptyDict[item], str)):
                try:
                    answer = input(f"give me a {item}: ")
                    filledDict[item] = type(emptyDict[item])(answer)
                except ValueError:
                    print(f"cannot parse string to {type(emptyDict[item])}")
            else:
                filledDict[item] = input(f"give me a {item}: ")
        return filledDict

def FillDataList(emptyList):
    filledList = emptyList
    for i in range(len(emptyList)):
        if (isinstance(emptyList[i], dict)):
            filledList[i] = FillDataDict(emptyList[i])
        elif not (isinstance(emptyList[i], str)):
            try:
                answer = input(f"{i+1}: ")
                filledList[i] = type(emptyList[i])(answer)
            except:
                print(f"cannot parse string to {type(emptyList[i])}")
        else:
            filledList[i] = input(f"{i+1}: ")
    return filledList

                