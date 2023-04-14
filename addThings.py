from parsers import ParseToHTML, GetYamlData, JSONToDict, JSONToList
from website import UpdateListBrowser, GetNav, GetStyle, AddDropDownContent
from jinja2 import Environment, FileSystemLoader
import json

def AddPage(markdownFile, template, style=" "):
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

        #a ditcionary with all the links the nav needs to contain
        navLinks = {"links": [{"name":"pages", "folder": "pages"}, {"name":"posts", "folder": "posts"}]}
        navLinks = AddDropDownContent(navLinks)


        #fill in template with jinja
        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template("page_template.html")
        with open(f"pages/{pageName}.html", mode="w", encoding="utf-8") as message:
            message.write(template.render(
                pageData,
                nav = GetNav("nav", navLinks),
                navStyle = GetStyle("navStyle.css"),
                style = GetStyle(style)
                ))

        with open("pages/" + markdownFile.replace("md", "JSON"), "w") as f:
            json.dump(pageData, f, default=str)
        with open("pages/pages.JSON", "w") as k:
            json.dump(pageList, k, default=str)
        UpdateListBrowser("pages", "pages", "pages_template.html")
    

def AddPost(markdownFile, template, style=" "):
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

        #a ditcionary with all the links the nav needs to contain
        navLinks = {"links": [{"name":"pages", "folder": "pages"}, {"name":"posts", "folder": "posts"}]}
        navLinks = AddDropDownContent(navLinks)

        #fill in template with jinja
        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template("post_template.html")
        with open(f"posts/{postName}.html", mode="w", encoding="utf-8") as message:
            message.write(template.render(
                postData,
                nav = GetNav("nav", navLinks),
                navStyle = GetStyle("navStyle.css"),
                style = GetStyle(style)
                ))
        
        #add site to taglist for each tag
        if ("tags" in postData.keys()):
            for tag in postData["tags"]:
                SitesWithTag = JSONToDict(f"tags/{tag}.JSON")
                SitesWithTag[f"{postName}"] = postData
                with open(f"tags/{tag}.JSON", "w") as g:
                    json.dump(SitesWithTag, g, default=str)
                UpdateListBrowser("tags", f"{tag}", "tagList.html", f"posts about {tag}")
                


        #save data and refresh post list
        with open("posts/" + markdownFile.replace("md", "JSON"), "w") as f:
            json.dump(postData, f, default=str)
        with open("posts/posts.JSON", "w") as k:
            json.dump(postList, k, default=str)
        UpdateListBrowser("posts", "posts", "posts_template.html")