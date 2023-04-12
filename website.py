from parsers import OpenTemplate, ListToLiOfLinks, JSONToList

def UpdateListBrowser(folder, list):
    html = open(f"{folder}/{folder}.html", "w")
    interface = OpenTemplate("browseList.html")
    liLinks = ListToLiOfLinks(folder, list)
    interface = interface.replace("<ul></ul>", liLinks)
    interface = interface.replace("name", f"{folder}")
    html.write(f"{interface}")
    html.close()

def initialize():
    html = open("home.html", "w")
    interface = OpenTemplate("template1.html")
    interface = interface.replace("insert-html", "<a href=posts/posts.html>posts</a>\n<a href=pages/pages.html>pages</a>")
    interface = interface.replace("name", "home")
    html.write(f"{interface}")
    html.close()
    pages = JSONToList("pages/pages.JSON")
    posts = JSONToList("posts/posts.JSON")
    UpdateListBrowser("pages", pages)
    UpdateListBrowser("posts", posts)
