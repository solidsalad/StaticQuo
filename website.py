from parsers import JSONToDict
from jinja2 import Environment, FileSystemLoader

def UpdateListBrowser(folder, file):
    data = JSONToDict(f"{folder}/{file}.JSON")
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template(f"{file}_template.html")
    with open(f"{folder}/{file}.html", mode="w", encoding="utf-8") as message:
        message.write(template.render(data = data.values()))

def initialize():
    types = {"types": [{"name":"pages", "folder": "pages"}, {"name":"posts", "folder": "posts"}]}
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("browseList.html")
    with open("_site/home.html", mode="w", encoding="utf-8") as home:
        home.write(template.render(
            types,
            title = "home"
            ))
    for type in types["types"]:
        UpdateListBrowser(type["folder"], type["name"])
