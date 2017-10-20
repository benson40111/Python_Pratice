#-*-coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, lxml, os

def Climb(url):
    a = 0
    page = requests.get(url).text
    html = BeautifulSoup(page, "lxml")
    title = html
    title = title.select("h1")[0].text
    print(title)

    path = os.getcwd()
    new_path = os.path.join(title)
    if not os.path.isdir(new_path):
        os.mkdir(new_path)

    for link in html.find_all("img", class_="BDE_Image"):
        a += 1
        #print link.get("src")
        with open(title  + "/" + str(a) + ".jpg",'wb') as code:  
            code.write(requests.get(link["src"]).content)  

if __name__=="__main__":
    url = str(input("Input url: \n"))
    length = url[37: 41]
    for i in range(0, 10):
        print(url[0: 37] + str(int(length) + i) + url[41: len(url)])
   
        #print url[0: 37] + str(length) + url[41: len(url)]
    """i = 0
    count = -1
    while(count < 0):
        alpha = url[count]
        if (alpha == "/"):
            if (i == 2):
                break
            i += 1
        count -= 1
        print alpha"""
    #Climb(url)

