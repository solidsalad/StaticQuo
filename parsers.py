import markdown
import yaml
from yaml.loader import SafeLoader
import json

#with open(markdownFile.replace("md", "html"), 'w') as f:


def MarkdownToHTML(markdownText):
    # Convert markdown to HTML
    tempHtml = markdown.markdown(markdownText)
    # return HTML
    return tempHtml

def StrYamlToDict(yamlText):
    data = yaml.safe_load(yamlText.replace("---", ""))
    return data

def ParseToHTML(destination, markdownFile):
    with open(markdownFile, 'r') as f:
        tempMd= f.read()
    
    #determine where yaml ends and markdown starts
    split = tempMd.rfind("---") + 3
    #split markdown part from the rest
    partMarkdown = tempMd[split+1:]
    return MarkdownToHTML(partMarkdown)


def GetYamlData(markdownFile):
    with open(markdownFile, 'r') as f:
        tempMd= f.read()
    #determine where yaml ends and merkdown starts
    split = tempMd.rfind("---") + 3
    #split yaml part from markdown part
    partYaml = tempMd[:split]
    return StrYamlToDict(partYaml)

#still need to edit this one
def ListToLiOfLinks(folder, list):
    #converting info to html layout
    liList = []
    for i in range(len(list)):
        fileName = JSONToDict(f"{folder}/{list[i]}.JSON")["title"]
        liList.append(f"\n\t\t\t<a href=\"{list[i]}.html\">{fileName}</a>")
        #amount of tabs based on length of address
        tab =  int(3 - float(len(list[i])/15)) * "\t"
    liString = "\n\t\t</li>\n\t\t<li>".join(liList)
    liString = f"<ul>\n\t\t<li>{liString}\n\t\t</li>\n\t</ul>"
    return liString

def JSONToList(source):
    list = []
    #try to open JSON file with already entered pages (if the file exists)
    try:
        with open(source) as f:
            list = json.load(f)
    except:
        #leave list empty/unchanged if no JSON is found
        list = list
    return list

def JSONToDict(source):
    dict = {}
    #try to open JSON file with already entered pages (if the file exists)
    try:
        with open(source) as f:
            dict = json.load(f)
    except:
        #leave dictionary empty/unchanged if no JSON is found
        dict = dict
    return dict