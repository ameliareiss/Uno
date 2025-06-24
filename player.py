# Amelia Reiss
# player.py

class Player:
    '''Player class contains information about a player's cards in their
    hand, as well as the actions they've executed on their turn'''
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.drawn = False # can only draw once per turn
        self.played = False # can only play 1 card per turn
        self.leftmost = 0 # index of leftmost card being displayed

    def draw(self, cards):
        '''Receives a list of drawn cards from the deck and adds it to the hand'''
        self.hand = self.hand + cards
    
    def play(self, card):
        '''Removes a given card from the hand and returns it'''
        for i, c in enumerate(self.hand):
            if c == card:
                return self.hand.pop(i)
            
    def __len__(self):
        return len(self.hand)
    
    def __eq__(self, other):
        return self.name == other
    
    def __str__(self):
        return f"{self.name} has {self.hand}"
    