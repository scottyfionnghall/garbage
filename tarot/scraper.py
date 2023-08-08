import requests
from bs4 import BeautifulSoup
import json

def scrape():
    """
    Scrapes cards from Labyrinthos.co, takes their name and keywords
    and creates a json file with names as a key and their keywords as a value
    """

    URL = "https://labyrinthos.co/blogs/tarot-card-meanings-list"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    cards = soup.find_all("div", class_="card")
    keywords = soup.find_all("div", class_="keywords")
    card_names = []
    card_meanings = []
    tarot = {}

    for card in cards:
        title = card.find("h3")
        card_names.append(title.get_text())

    for card_keywords in keywords:
        keywords = card_keywords.find('p')
        keywords = str(keywords.get_text())
        keywords = keywords.split('\n')
        upright = keywords[2]
        reversed = keywords[-3].strip('      ')
        card_meanings.append([upright,reversed])

    for i in range(0,len(card_names)):
        tarot[card_names[i]] = card_meanings[i]

    
    with open('tarot.json', 'a') as outfile:
        json.dump(tarot, outfile)