# Amelia Reiss
# game.py

from random import shuffle
from deck import Deck
from player import Player

class Game:
    '''Game class contains all methods for managing the game's state, like
    executing player moves, changing turns, and moving cards between the player
    and the deck'''
    def __init__(self, num_players):
        self.starting_cards = 7
        self.deck = Deck()
        self.discarded = [self.deck.draw()]
        self.players = []
        self.turn = 0

        # create players and deal cards
        for player in range(num_players):
            self.players.append(Player(f"Player {player+1}"))
            self.give_cards(self.players[player], self.starting_cards)

    def give_cards(self, player, num_cards=1):
        '''Draws num_cards cards from deck and adds to player's hand. Returns False
        if no cards were drawn, True otherwise'''
        # if there are not cards in the deck, restock
        if len(self.deck) < num_cards:
            self.restock()
        # otherwise, try to give cards
        try:
            cards = []
            for _ in range(num_cards):
                cards.append(self.deck.draw())
            player.draw(cards)
        except:
            print("ERROR: Not enough cards in deck to draw.")
            return False
        return True

    def do_action(self, color):
        '''Executes the respective action of the action card, updating the color
        of a wild card, if the card is wild.'''
        top = self.get_top()
        player = self.players[self.turn]
        next_player = self.players[abs(self.turn - 1)]

        # +2 makes next_player draw 2 cards
        if top.value == "+2":
            self.give_cards(next_player, 2)
            
        # wild prompts color change
        if top.wild():
            self.change_wild(self.get_top(), color)
            if top.value == "+4 wild":
                self.give_cards(next_player, 4)

        # all action cards give a second turn, except regular wild cards
        if top.value != "wild":
            # implements reverse like skip for 2 player game
            player.drawn = False
            player.played = False

    def change_wild(self, card, color):
        '''Changes the given card's color to given color.'''
        card.change_color(color) # change color value

    def get_valid_cards(self, player):
        '''Returns a list of valid cards that the player can play'''
        cards = []
        for card in player.hand:
            if self.valid(card):
                cards.append(card)
        return cards

    def valid(self, card):
        '''Returns True if given card can be played on top card of discard pile, False otherwise'''
        return card.playable(self.discarded[-1])

    def discard(self, card):
        '''Adds given card to the top of the discard pile (end of list)'''
        self.discarded.append(card)
    
    def restock(self):
        '''Shuffles cards from discard pile and adds them to the bottom of the deck'''
        top = self.discarded.pop() # pop top card to save
        shuffle(self.discarded) 
        self.deck.cards = self.discarded + self.deck.cards # append shuffled cards to bottom of deck (front of list)
        self.discarded = [top]

    def get_top(self):
        '''Returns top card of discard pile.'''
        return self.discarded[-1]
    
    def change_turn(self):
        '''Changes player turn (only for 2 player game)'''
        self.turn = abs(self.turn - 1)
