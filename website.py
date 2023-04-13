from parsers import JSONToDict
from jinja2 import Environment, FileSystemLoader

def UpdateListBrowser(folder, file):
    data = JSONToDict(f"{folder}/{file}.JSON")
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template(f"{file}_template.html")
    types = {"links": [{"name":"pages", "folder": "pages"}, {"name":"posts", "folder": "posts"}]}
    with open(f"{folder}/{file}.html", mode="w", encoding="utf-8") as message:
        message.write(template.render(
            data = data.values(),
            nav = GetNav("nav", types),
            navStyle = GetStyle("navStyle.css"),
            style = GetStyle("darkMode.css")
            ))

def initialize():
    types = {"links": [{"name":"pages", "folder": "pages"}, {"name":"posts", "folder": "posts"}]}
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("browseList.html")
    with open("_site/home.html", mode="w", encoding="utf-8") as home:
        home.write(template.render(
            title = "home",
            nav = GetNav("nav", types),
            navStyle = GetStyle("navStyle.css"),
            style = GetStyle("darkMode.css")
            ))
    for type in types["links"]:
        UpdateListBrowser(type["folder"], type["name"])

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
