from _typeshed import Self
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://w3champions.com/Rankings/')
html = driver.page_source
soup = BeautifulSoup(html)
soup

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all(class_="custom-table")

job_elements = results.find_all("div", class_="custom-table")



from _typeshed import Self
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")