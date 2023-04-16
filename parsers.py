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

def ParseToHTML(markdownFile):
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