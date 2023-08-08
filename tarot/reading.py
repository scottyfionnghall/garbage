import json
from random import  choice
from scraper import scrape
import os
class Card:
    """A model of a Tarot card."""

    def __init__(self,name,upright,reversed):
        """
        Initialize arcana(suite), name, 
        description and interpretation.
        """
        self.name = name
        self.upright = upright
        self.reversed = reversed
    
    def reading(self):
        """
        Function to print out a reading using card info.
        """

        print(f'Card name: {self.name}')
        print(choice([self.upright,self.reversed]))

# scrape cards into tarot.json file
if os.path.isfile('tarot.json') != True:
    print('Creating "trot.json"...')
    scrape()
    print('Completed!\n')

cards = open('tarot.json','r')
cards = json.load(cards)
deck = []

for card in cards:
    name = card
    upright = cards[name][0]
    reversed = cards[name][1]
    deck.append(Card(name,upright,reversed))

current_card = choice(deck)
current_card.reading()


