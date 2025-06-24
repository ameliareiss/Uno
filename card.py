# Amelia Reiss
# card.py

import pygame
import design as d
pygame.font.init()

class Card:
    '''Card class contains the value and color of a card, allowing for easier comparisons and
    display of cards'''
    def __init__(self, value, color, action):
        self.value = value
        self.color = color
        self.action = action

        card_color = d.wild_color if self.wild() else self.color # default wild cards to white
        self.surface = self.create_card(card_color)
        self.rect = self.surface.get_rect()

    def create_card(self, color):
        '''Creates a card's surface that will be displayed when it is on screen.'''
        # define card size and color
        surf = pygame.Surface((d.card_w, d.card_h)) # create surface
        surf.fill(color) # give color
        pygame.draw.rect(surf, "black", [0, 0, surf.get_width(), surf.get_height()], 3, 5) # give card border

        # add text to card
        size = 30 if self.action else 70 # font size
        font = pygame.font.SysFont(None, size) # create default font
        text = font.render(self.value, True, "black", color) # create text
        textrect = text.get_rect(center=(d.card_w/2, d.card_h/2)) # center text with card size
        surf.blit(text, textrect) # add text to surface

        return surf
    
    def selected(self):
        '''Returns True if the mouse is on this card, False otherwise'''
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def change_color(self, color):
        '''Changes the color value of the card, as well as the display color, by creating
        a new card surface and rect. Mostly used for updating wild cards.'''
        self.color = color
        self.surface = self.create_card(color)
        self.rect = self.surface.get_rect()

    def display(self, screen, position):
        # CHANGE TO GUI FUNCTION AND CREATE IN GUI **********
        '''Displays card at position and updates screen'''
        self.rect = self.surface.get_rect(topleft=(position))
        screen.blit(self.surface, self.rect)
        return screen

    def wild(self):
        '''Returns True if card is wild or +4 wild, False otherwise'''
        return "wild" in str(self.value)
    
    def playable(self, other):
        '''Returns True if card can be played on top of other card (top of discard pile).
        Does not check for other.wild() because wild card has already changed color after
        being played.'''
        return self.value == other.value or self.color == other.color or self.wild()

    def __str__(self):
        if self.wild():
            return self.value
        return f"{self.color} {self.value}"
    
    def __repr__(self):
        if self.wild():
            return self.value
        return f"{self.color} {self.value}"
    
    def __eq__(self, other):
        return str(self) == str(other)


