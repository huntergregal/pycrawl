import http.client
import urllib.request
#WebCrawler
#Brought to you by Hunter Gregal


host=str(input("Please input the target host url. Ex: aptgetswag.com:\n"))
dir1=str(input("Please input the directory to crawl. Ex: '/pages/' or simple '/':\n"))
myExt=["php","html","js","jpeg","jpg","png","txt"]
myName=["index.","robots.","page.","password.","secret."]
myDict=[]
a=0
b=0
while (a < len(myName)):
    while (b < len(myExt)):
        myDict.append(myName[a] + myExt[b])
        b=b+1
    b=0
    a=a+1
                    
i=0 
while (i < len(myDict)):
    conn = http.client.HTTPConnection(host)
    conn.request("HEAD", dir1 + myDict[i])
    res = conn.getresponse()
    page = str(("http://" + host + dir1 + myDict[i]))
  
    if (res.status == 200):
        print(page + "    " + res.reason)
        usock = urllib.request.urlopen(page)
        print(usock.info())
      
    conn.close()
    i = i+1
