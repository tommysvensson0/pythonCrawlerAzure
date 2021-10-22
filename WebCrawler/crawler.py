#from _typeshed import Self
import requests
from bs4 import BeautifulSoup
import csv  

#pip install typeshed-client
#pip install beautifulsoup4

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

class Job(object):
    def __init__(self, title="", company="", location=""):
        self.title = title
        self.company = company
        self.location = location
    
    def make_Job(title, company, location):
       return Job(title, company, location)

    def echo(self):
        print(self.title)
        print(self.company)
        print(self.location)

objects = []
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    title_element = title_element.text.strip()
    company_element = company_element.text.strip()
    location_element = location_element.text.strip()

    testobject = Job(title_element,company_element,location_element)
    objects.append(testobject)

#len(objects)
#asd = objects[47]
#asd.title
#asd.company
#asd.location

with open('C:/Users/tomsve/Git/tommysvensson0-azure-private/ProjectW3C/WebCrawler/file1.csv', 'w', newline='',) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title','Company','Location'])
    for object in objects:
        writer.writerow([object.title, object.company, object.location])
