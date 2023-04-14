from parsers import ParseToHTML, GetYamlData, JSONToDict
from website import UpdateListBrowser, GetNav, GetStyle, AddDropDownContent, Initialize
from jinja2 import Environment, FileSystemLoader
import json
import os
import time

def AddPage(markdownFile, styleFile="darkMode.css"):
    try:
        content = ParseToHTML(markdownFile)
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
                style = GetStyle(styleFile)
                ))

        with open("pages/" + markdownFile.replace("md", "JSON"), "w") as f:
            json.dump(pageData, f, default=str)
        with open("pages/pages.JSON", "w") as k:
            json.dump(pageList, k, default=str)
        
        print(f"page {pageName} from {markdownFile} succesfully added")
        
        UpdateListBrowser("pages", "pages", "pages_template.html")
        Initialize()
    

def AddPost(markdownFile, styleFile="darkMode.css"):
    try:
        content = ParseToHTML(markdownFile)
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
                style = GetStyle(styleFile)
                ))
        
        #add site to taglist for each tag
        if ("tags" in postData.keys()):
            for tag in postData["tags"]:
                sitesWithTag = JSONToDict(f"tags/{tag}.JSON")
                sitesWithTag[f"{postName}"] = postData
                with open(f"tags/{tag}.JSON", "w") as g:
                    json.dump(sitesWithTag, g, default=str)
                UpdateListBrowser("tags", f"{tag}", "tagList.html", f"posts about {tag}")
                
        #save data and refresh post list
        with open("posts/" + markdownFile.replace("md", "JSON"), "w") as f:
            json.dump(postData, f, default=str)
        with open("posts/posts.JSON", "w") as k:
            json.dump(postList, k, default=str)

        print(f"page {postName} from {markdownFile} succesfully added")        
    
        UpdateListBrowser("posts", "posts", "posts_template.html")
        Initialize()

def DelPage(fileName):
    try:
        os.remove(f"pages/{fileName}.html")
        os.remove(f"pages/{fileName}.JSON")
    except:
        print(f'file "{fileName}.html not found')
    else:
        pageList = JSONToDict("pages/pages.JSON")
        del pageList[f"{fileName}"]
        
        #save new list to JSON
        with open("pages/pages.JSON", "w") as k:
            json.dump(pageList, k, default=str)
        
        print(f"page {fileName} succesfully deleted")

        #refresh homepage
        Initialize()

        #update list (and the dropdown content of that page)
        UpdateListBrowser("pages", "pages", "pages_template.html")


def DelPost(fileName):
    try:
        #remove from taglist
        postData = JSONToDict(f"posts/{fileName}.JSON")
        for tag in postData["tags"]:
            sitesWithTag = JSONToDict(f"tags/{tag}.JSON")
            del sitesWithTag[f"{fileName}"]
            #remove taglist if empty
            if (len(sitesWithTag) == 0):
                os.remove(f"tags/{tag}.JSON")
                os.remove(f"tags/{tag}.html")
            else:
                with open(f"tags/{tag}.JSON", "w") as g:
                    json.dump(sitesWithTag, g, default=str)
                UpdateListBrowser("tags", f"{tag}", "tagList.html", f"posts about {tag}")

        #remove files
        os.remove(f"posts/{fileName}.html")
        os.remove(f"posts/{fileName}.JSON")
    except:
        print(f'file "{fileName}.html not found')
    else:
        postList = JSONToDict("posts/posts.JSON")
        del postList[f"{fileName}"]
        
        #save new list to JSON
        with open("posts/posts.JSON", "w") as k:
            json.dump(postList, k, default=str)

        print(f"post {fileName} succesfully deleted")
        
        #refresh homepage
        Initialize()

        #update list (and the dropdown content of that page)
        UpdateListBrowser("pages", "pages", "pages_template.html")

def AddWithPrefab(templateMdFile, fillData, fileName, type="post"):
    #fill in the template with the provided data
    environment = Environment(loader=FileSystemLoader("templates/prefabs/"))
    mdTemplate = environment.get_template(templateMdFile)
    
    with open(f"{fileName}.md", mode="w", encoding="utf-8") as message:
        message.write(mdTemplate.render(fillData))

    if (type == "page"):
        AddPage(f"{fileName}.md")
    elif (type == "post"):
        AddPost(f"{fileName}.md")
    else:
        print(f"filetype {type} not found")
    os.remove(f"{fileName}.md")
