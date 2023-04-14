from addThings import AddPage, AddPost, DelPage, DelPost
from website import Initialize
from userInteract import AddPostOrPage, DelPostOrPage
import sys
import json

def UnknownCommandError():
    print("ERROR: unknown command\n\ntry:\n\tstaticQuo.py page/post add [markdownFile] ...\n\tstaticQuo.py page/post del [filename]\n\tstaticQuo.py [template] add [number]\n\tstaticQuo.py prefabs\n")

Initialize()

#syntax: staticQuo.py page/post add [markdownFile] ... -> add premade markdown(s)
#syntax: staticQuo.py page/post del [filename] ... -> delete page(s)/post(s)
#syntax: staticQuo.py [template] add [number] -> add x amount of sites using a certain template
#syntax: staticQuo.py prefabs -> browse prefabs and choose one to edit

if (len(sys.argv) >= 4):
    #syntax: staticQuo.py page add [markdownFile]
    if (sys.argv[1] in ["page", "post"]):
        if (sys.argv[2] == "add"):
            AddPostOrPage(sys.argv[1], sys.argv[3:])
        elif (sys.argv[2] == "del"):
            DelPostOrPage(sys.argv[1], sys.argv[3:])
        else:
            UnknownCommandError()
    
    #syntax: staticQuo.py [template] add [number]
    elif isinstance(sys.argv[3],(int, float)) and (sys.argv[3] > 0):
        print("template code not added yet")
    else:
        print("hallo")
        UnknownCommandError()
else:
    print("ikd")