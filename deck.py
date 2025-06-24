# Amelia Reiss
# deck.py

from random import shuffle
from card import Card
import design as d

class Deck:
    '''Deck class contains a list of cards, where the end of the
    list represents the top of the deck'''
    actions = {10:"reverse", 
               11:"skip", 
               12:"+2", 
               13:"wild", 
               14:"+4 wild"}

    def __init__(self):
        self.cards = []
        # create 2 of each card
        for color in d.colors:
            for value in range(0,15):
            
                # if card is action card, no numeric value
                is_action = False
                if value > 9:
                    value = self.actions[value]
                    is_action = True
                    # if card is wild, no color
                    if "wild" in value: 
                        color = None

                self.cards.append(Card(str(value), color, is_action))
                # 0's and wild cards only have 4 cards total, instead of 8
                if value != 0 and not self.cards[-1].wild():
                    self.cards.append(Card(str(value), color, is_action))
        
        # shuffle deck until top card is NOT action, since top card will be first discard
        while self.cards[-1].action:
            shuffle(self.cards)
    
    def draw(self):
        '''Returns the top card of the deck (last in list)'''
        return self.cards.pop(-1)

    def get_cards(self):
        return self.cards

    def __len__(self):
        return len(self.cards)
    