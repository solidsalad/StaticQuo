from addThings import AddPage, AddPost
from website import initialize
import sys
import json


initialize()

AddPage("fuck.md", "template1.html", "darkMode.css")
AddPost("dingeske.md", "template1.html", "darkMode.css")
AddPage("chatGPTPageExample.md", "template1.html", "darkMode.css")
AddPost("chatGPTPostExample.md", "template1.html", "darkMode.css")
AddPost("post1.md", "template1.html", "darkMode.css")




#if (len(sys.argv) > 3):
#    if (sys.argv[2] == "page"):
#        try:
#            with open("pingTest.JSON", "r") as f:
#            domainlist = json.load(f)
#        except:
#            #leave list empty/unchanged if no JSON is found
#            domainlist = domainlist
#         
#    for arg in sys.argv[2:]:
#        if (arg not in domainlist):
#            domainlist.append(arg)