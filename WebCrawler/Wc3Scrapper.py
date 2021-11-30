from bs4.element import ResultSet, SoupStrainer
import requests
import os
import csv
from pyppeteer import launch
import enum

class Player:
    def __init__(self, Name, MMR, Race):
        self.Name = Name
        self.MMR = MMR
        self.Race = Race

class Race(enum.Enum):
    Horde = 1
    Human = 2
    Undead = 3
    NightElf = 4
    Random = 0

def race(index):
    switcher={
        2:Race.Horde.name,
        1:Race.Human.name,
        8:Race.Undead.name,
        4:Race.NightElf.name,
        0:Race.Random.name
    }
    return switcher.get(index,"No race with that number")

def main():       
    #Turns out that this website does not load data from DB, instead it uses API call to get the ranks
    #So Python can just get by using the same API call
    #constelation = requests.get('https://website-backend.w3champions.com/api/ladder/league-constellation?season=9')
    tableData = requests.get('https://website-backend.w3champions.com/api/ladder/0?gateWay=20&gameMode=1&season=9')
    data = tableData.json()

    userprofile = os.environ['USERPROFILE'] 
    os.makedirs(os.path.dirname(userprofile+'/source/repos/Scripts/Python/WebCrawler/pythonCrawlerAzure/WebCrawler/ExternalFiles/file1.csv'),exist_ok=True)
    with open(userprofile+'/source/repos/Scripts/Python/WebCrawler/pythonCrawlerAzure/WebCrawler/ExternalFiles//file1.csv', 'w', newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name','MMR','Race'])
        for player in data:
            playerfaction = race(player['player']['race'])
            wc3Player = Player(player['player']['name'],player['player']['mmr'],playerfaction)
            writer.writerow([wc3Player.Name, wc3Player.MMR, wc3Player.Race])     

if(__name__ == "__main__"):
    main()

