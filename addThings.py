from parsers import ParseToHTML, GetYamlData, JSONToDict
from website import UpdateListBrowser
from jinja2 import Environment, FileSystemLoader
import json

def AddPage(markdownFile, template):
    try:
        content = ParseToHTML("pages", markdownFile)
    except:
        print(f"file {markdownFile} not found, skipping to next file")
    else:
        pageName = markdownFile.replace(".md", "")
        #make list of all pages
        pageList = JSONToDict("pages/pages.JSON")

        #check if there is already a page with that name (if yes, it gets overwritten)
        if pageName not in list(pageList.keys()):
            pageList[f"{pageName}"] = ""

        #save data in general page list
        pageData = GetYamlData(markdownFile)
        pageData["fileName"] = pageName
        pageData["content"] = content
        if "author" not in list(pageData.keys()):
            pageData["author"] = "anonymous"
        pageList[f"{pageName}"] = pageData

        #fill in template with jinja
        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template("page_template.html")
        with open(f"pages/{pageName}.html", mode="w", encoding="utf-8") as message:
            message.write(template.render(pageData))

        with open("pages/" + markdownFile.replace("md", "JSON"), "w") as f:
            json.dump(pageData, f, default=str)
        with open("pages/pages.JSON", "w") as k:
            json.dump(pageList, k, default=str)
        UpdateListBrowser("pages", "pages")
    

def AddPost(markdownFile, template):
    try:
        content = ParseToHTML("posts", markdownFile)
    except:
        print(f"file {markdownFile} not found, skipping to next file")
    else:
        postName = markdownFile.replace(".md", "")
        #make list of all posts
        postList = JSONToDict("posts/posts.JSON")

        #check if there is already a post with that name (if yes, it gets overwritten)
        if postName not in list(postList.keys()):
            postList[f"{postName}"] = ""

        #save data and refresh page list
        postData = GetYamlData(markdownFile)
        postData["fileName"] = postName
        postData["content"] = content
        if "author" not in list(postData.keys()):
            postData["author"] = "anonymous"
        postList[f"{postName}"] = postData

        #fill in template with jinja
        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template("post_template.html")
        with open(f"posts/{postName}.html", mode="w", encoding="utf-8") as message:
            message.write(template.render(postData))

        #save data and refresh post list
        with open("posts/" + markdownFile.replace("md", "JSON"), "w") as f:
            json.dump(postData, f, default=str)
        with open("posts/posts.JSON", "w") as k:
            json.dump(postList, k, default=str)
        UpdateListBrowser("posts", "posts")