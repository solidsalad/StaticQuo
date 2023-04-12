from parsers import ParseToHTML, GetYamlData, JSONToList
import json

def AddPage(markdownFile, template):
    try:
        ParseToHTML("pages", markdownFile, template)
    except:
        print(f"file {markdownFile} not found, skipping to next file")
    else:
        pageName = markdownFile.replace(".md", "")
        #make list of all pages
        pagelist = JSONToList("pages/pages.JSON")

        #check if there is already a page with that name (if yes, it gets overwritten)
        if pageName not in pagelist:
            pagelist.append(pageName)

        pageData = GetYamlData(markdownFile)
        with open("pages/" + markdownFile.replace("md", "JSON"), "w") as f:
            json.dump(pageData, f, default=str)
        with open("pages/pages.JSON", "w") as k:
            json.dump(pagelist, k, default=str)
    

def AddPost(markdownFile, template):
    try:
        ParseToHTML("posts", markdownFile, template)
        postData = GetYamlData(markdownFile)
    except:
        print(f"file {markdownFile} not found, skipping to next file")
    else:
        postName = markdownFile.replace(".md", "")
        #make list of all posts
        postlist = JSONToList("posts/posts.JSON")

        #check if there is already a post with that name (if yes, it gets overwritten)
        if postName not in postlist:
            postlist.append(postName)
        
        with open("posts/" + markdownFile.replace("md", "JSON"), "w") as f:
            json.dump(postData, f, default=str)
        with open("posts/posts.JSON", "w") as k:
            json.dump(postlist, k, default=str)