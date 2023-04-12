from parsers import ParseToHTML, GetYamlData, JSONToList
import json

def AddPage(markdownFile, template):
    pageName = markdownFile.replace(".md", "")
    #make list of all pages
    pagelist = JSONToList("pages/pages.JSON")

    #check if there is already a page with that name (if yes, it gets overwritten)
    if pageName not in pagelist:
        pagelist.append(pageName)
    ParseToHTML("pages", markdownFile, template)
    pageData = GetYamlData(markdownFile)
    with open("pages/" + markdownFile.replace("md", "JSON"), "w") as f:
        json.dump(pageData, f, default=str)
    with open("pages/pages.JSON", "w") as k:
        json.dump(pagelist, k, default=str)
    

def AddPost(markdownFile, template):
    postName = markdownFile.replace(".md", "")
    #make list of all posts
    postlist = JSONToList("posts/posts.JSON")

    #check if there is already a post with that name (if yes, it gets overwritten)
    if postName not in postlist:
        postlist.append(postName)
    ParseToHTML("posts", markdownFile, template)
    postData = GetYamlData(markdownFile)
    with open("posts/" + markdownFile.replace("md", "JSON"), "w") as f:
        json.dump(postData, f, default=str)
    with open("posts/posts.JSON", "w") as k:
        json.dump(postlist, k, default=str)