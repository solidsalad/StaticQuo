from parsers import JSONToDict
from jinja2 import Environment, FileSystemLoader

def UpdateListBrowser(folder, content, template, contentHeader=""):
    data = JSONToDict(f"{folder}/{content}.JSON")
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template(template)
    types = {"links": [{"name":"pages", "folder": "pages"}, {"name":"posts", "folder": "posts"}]}
    types = AddDropDownContent(types)
    #if no content header has been provided, the content header becomes the name of the file
    if (contentHeader == ""):
        contentHeader = content
    with open(f"{folder}/{content}.html", mode="w", encoding="utf-8") as message:
        message.write(template.render(
            data = data.values(),
            nav = GetNav("nav", types),
            navStyle = GetStyle("navStyle.css"),
            style = GetStyle("darkMode.css"),
            header = contentHeader,
            title = contentHeader
            ))

def Initialize():
    types = {"links": [{"name":"pages", "folder": "pages"}, {"name":"posts", "folder": "posts"}]}
    types = AddDropDownContent(types)
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("home.html")
    with open("_site/home.html", mode="w", encoding="utf-8") as home:
        home.write(template.render(
            title = "home",
            nav = GetNav("nav", types),
            navStyle = GetStyle("navStyle.css"),
            style = GetStyle("darkMode.css")
            ))
    for type in types["links"]:
        UpdateListBrowser(type["folder"], type["name"], f'{type["name"]}_template.html')

def GetNav(navName, links):
    environment = Environment(loader=FileSystemLoader("templates/"))
    nav = environment.get_template(f"{navName}.html")
    interface = nav.render(
        links
    )
    return interface

def GetStyle(styleName):
    style = open(f"templates/styles/{styleName}","r")
    interface = style.read()
    style.close()
    return interface    

def AddDropDownContent(types):
    #add dropdown content
    for type in types["links"]:
        type["content"] = JSONToDict(f'{type["folder"]}/{type["name"]}.JSON')
    return types
