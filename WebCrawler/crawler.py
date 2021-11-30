from bs4.element import ResultSet, SoupStrainer
import requests
import os
from bs4 import BeautifulSoup
import csv
import asyncio
from pyppeteer import launch
from requests.api import request
from Job import Job

#pip install typeshed-client
#pip install beautifulsoup4
#pip install requests
#pip install pyppeteer

async def main():
    #URL = "https://realpython.github.io/fake-jobs/"
    #URL = https://crawler-test.com/ Possibly used to unit-test all different webscraping methods and sites
    #URL = 'https://www.w3champions.com/rankings'
    URL = 'https://w12.mangafreak.net/'
    browser = await launch()

    newpage = await browser.newPage()
    await newpage.goto(URL)
    content = await newpage.content()    
    soup = BeautifulSoup(content, "html.parser")
    #Will return a list of element that have html attr and value
    element_list = soup.find_all('a',{'class':{'image'}})

    #Used to just increment the name of pictures that are downloaded
    indexer = 0    
    userprofile = os.environ['USERPROFILE'] 
    os.makedirs(os.path.dirname(userprofile+'/source/repos/Scripts/Python/WebCrawler/pythonCrawlerAzure/WebCrawler/Images/'),exist_ok=True)
    for image in element_list:
        #Loop trough all the element. The content out of each html attr becomes available
        #image.find('img') tells python to find and grab everything inside this html-element.
        #When adding a ['src'], it specifies what type of content that should be grabbed.
        imgurl = image.find('img')['src']
        #Makes a http call for the URL and grabs the content.
        #image_data becomes mostly hexadecimal data that needs to be converted.
        #This is so it can be translated into a .jpg-file or whatever file-format it can become
        image_data = requests.get(imgurl).content
        #Only want to download the first 5 pictures
        if(indexer == 10):                
                break
        else:
            #Creates a directory if it is not already available and puts the files into it.
            with open('C:/Users/Johnn/source/repos/Scripts/Python/WebCrawler/pythonCrawlerAzure/WebCrawler/Images/Testimg'+str(indexer)+'.jpg', 'wb') as handler:
                    handler.write(image_data)        
        indexer += 1
    await browser.close()

if(__name__ == "__main__"):
    asyncio.run(main())

# with open('/app/file1.csv', 'w', newline='',) as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Title','Company','Location'])
#     for object in objects:
#         writer.writerow([object.title, object.company, object.location])


#How I solved it before
# for source in image.contents:
#     print(source)
#     print(source['src'])
#     img_data = requests.get(source['src']).content