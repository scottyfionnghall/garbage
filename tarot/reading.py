import json
from random import  choice

class Card:
    """A model of a Tarot card."""

    def __init__(self,arcana,name,description,interpretation):
        """
        Initialize arcana(suite), name, 
        description and interpretation.
        """

        self.arcana = arcana
        self.name = name
        self.description = description
        self.interpretation = interpretation
    
    def reading(self):
        """
        Function to print out a reading using card info.
        """

        print(f'Card name: {self.name}\n')
        print(f'Description: {self.description}\n')
        print(f'Interpretation: {self.interpretation}')

cards = open('tarot.json','r')
cards = json.load(cards)
deck = []

for card in cards['tarot']:
    arcana = card['suite']
    name = card['name']
    description = card['description']
    interpretation = card['interpretation']
    deck.append(Card(arcana,name,description,interpretation))

current_card = choice(deck)
current_card.reading()


