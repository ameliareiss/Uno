# Amelia Reiss
# gui.py

import sys
import pygame
import design as d

class GUI:
    '''GUI class contains all methods for creating and displaying the objects and surfaces on the screen, 
    as well as handling user interaction with the GUI.'''
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.wild_card_rects = [] # list of colored rects on wild card prompt
        self.discard_outline = None
        self.draw_outline = None
        self.hand_outline = None
        # dictionary of all on screen images, where key = name and value = (surf, rect)
        self.images = {} 

        self.create_board() # create all surfaces/rects for game objects

    def create_board(self):
        '''Creates all surfaces and rects that appear on screen and saves to instance.'''
        self.screen.fill(d.screen_color)
        self.draw_outlines() # create outlines for discard pile and user hand
        self.create_wild() # create wild card surface
        
        # create draw, end turn, left scroll, and right scroll images
        self.images["draw"] = (self.make_image((d.card_w, d.card_h), "grey10", 30, "Draw", "grey90", d.draw_pos))
        self.images["end turn"] = (self.make_image((d.end_w, d.end_h), d.outline_color, 30, "End Turn", "grey10", d.end_pos))
        self.images["left scroll"] = (self.make_image((d.scroll_w, d.scroll_h), d.outline_color, 30, "<--", "grey10", d.left_pos))
        self.images["right scroll"] = (self.make_image((d.scroll_w, d.scroll_h), d.outline_color, 30, "-->", "grey10", d.right_pos))

    def draw_outlines(self):
        '''Draws and saves the border/outlines for the discard pile and the player hand.'''
        self.discard_outline = pygame.draw.rect(self.screen, d.outline_color, (d.discard_border), 3, d.border)
        self.hand_outline = pygame.draw.rect(self.screen, d.outline_color, (d.hand_border), 3, d.border)
        self.draw_outline = pygame.draw.rect(self.screen, d.outline_color, (d.draw_border), 3, d.border)

    def create_wild(self):
        '''Creates the color selection pop-up for wild cards'''
        # create big surface to hold colors
        self.wild_surf = pygame.Surface((d.card_w * 1.5, d.card_h * 1.5))
        self.wild_rect = self.wild_surf.get_rect()
        self.wild_rect.center = (self.discard_outline.center) # position rect above discard pile

        # create 4 smaller colored rects
        for i, color in enumerate(d.colors):
            surf = pygame.Surface((self.wild_rect.w/2+1, self.wild_rect.h/2)) # make small surface
            surf.fill(color) # add color to surface

            # assign each color its position, respective to big surface
            if i == 0: # red in top left
                pos = (0,0)
            elif i == 1: # purple in top right
                pos = (self.wild_rect.w / 2, 0)
            elif i == 2: # green in bottom left
                pos = (0, self.wild_rect.h / 2)
            else: # blue in bottom right
                pos = (self.wild_rect.w / 2, self.wild_rect.h / 2)
            
            self.wild_surf.blit(surf, pos) # add small, colored rect to big rect
            rect = surf.get_rect(topleft=(self.wild_rect.x, self.wild_rect.y)) # move rect to big rect
            rect = rect.move(pos) # offset small quadrant by pos to get actual pos
            self.wild_card_rects.append(rect) # add smaller rect to list of color rects

    def make_image(self, dimensions, background_color, text_size, text, text_color, pos):
        '''Creates a button with text and adds its to the dictionary. 
        Takes the button's dimensions, the button's color, the 
        text to be displayed, the color of the text, the size of the text, and
        position of the topleft of the surface as parameters.'''
        # create button surface and add color
        surf = pygame.Surface(dimensions)
        surf.fill(background_color)

        # create text
        font = pygame.font.SysFont(None, text_size) # create font
        text = font.render(text, True, text_color, background_color) # create text
        textrect = text.get_rect(center=(dimensions[0] / 2, dimensions[1] / 2)) # center text to surface
        surf.blit(text, textrect) 

        # attatch text to surface
        surfrect = surf.get_rect().move(pos)

        # return surface and rect created
        return surf, surfrect
    
    def update(self):
        '''Updates all components of graphics on screen'''
        self.screen.fill(d.screen_color)
        self.draw_outlines()

        # display all images
        for image in self.images:
            self.screen.blit(self.images[image][0], self.images[image][1])

        # these change often, so need to recreate every call
        self.show_hand(self.game.players[0])
        self.show_num_cards(self.game.players[1])
        self.show_num_cards(self.game.players[0])
        self.show_discard_pile()

    def show_hand(self, user):
        '''Displays the user's hand'''
        # if player has more than 8 cards, only display 7
        if len(user) > 7:
            start_idx, end_idx = user.leftmost, user.leftmost + 7
        # otherwise, display however many they have
        else: 
            start_idx, end_idx = 0, len(user)
        for i in range(start_idx, end_idx):
            user.hand[i].display(self.screen, (d.hand_pos[0] + d.card_w * (i-start_idx), d.hand_pos[1]))

    def show_num_cards(self, player):
        '''Displays the number of cards that the player has'''
        # change font size and position, based on player
        if player == self.game.players[0]: # user
            name = "You have"
            size = 30
            pos = (d.screen_w/2, d.screen_h-35)
        else: # opponent
            name = "Opponent has"
            size = 50
            pos = (d.screen_w/2, 50)
        # create and display text
        font = pygame.font.SysFont(None, size)
        text = font.render(f"{name} {len(player)} cards", True, "black", d.screen_color)
        textrect = text.get_rect(center=pos)
        self.screen.blit(text, textrect)

    def show_discard_pile(self):
        '''Displays the discard pile'''
        card = self.game.get_top()
        self.screen = card.display(self.screen, (d.discard_pos))

    def pick_color(self):
        '''Allows user to change the wild card color by clicking a respective color quadrant.
        Returns the index of the color chosen (see design.py).'''
        while True:
            self.update()
            self.show_wild()
            for event in pygame.event.get():
                # if user closes window, quit
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()

                # if user clicks a color, return the color that is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for i, rect in enumerate(self.wild_card_rects):
                        if rect.collidepoint(pos):
                            return i

            pygame.display.flip()

    def user_turn(self):
        '''Allows user to interact with GUI'''
        for event in pygame.event.get():
            
            # if user closes window, quit
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

            # if user clicks something
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.execute_click()

    def execute_click(self):
        '''Executes user clicks if valid. Valid moves per turn include
        drawing once, and playing a single card. A card cannot be drawn after
        a card has been played, but a card can be played after a card
        has been drawn.'''
        user = self.game.players[0]
        pos = pygame.mouse.get_pos()
        # if user ends turn
        if self.clicked(pos, "end turn"):
            self.game.change_turn()
            # print(f"ENDED TURN with {len(user)} cards") # testing

        # if user wants to navigate navigate left or right in hand, make sure there are cards to show
        elif self.clicked(pos, "left scroll") and user.leftmost > 0:
            user.leftmost -= 1
        elif self.clicked(pos, "right scroll") and len(user) > 7 and len(user) - (user.leftmost + 7) > 0:
            user.leftmost += 1

        # if user draws card
        elif self.clicked(pos, "draw") and not user.played and not user.drawn:
            user.drawn = self.game.give_cards(user)

        # if user plays card in hand
        elif not user.played:
            moves = self.game.get_valid_cards(user) # list of playable cards for user
            for card in user.hand:
                if card.selected() and card in moves:
                    # If user played rightmost card when scrolled all the way to the right 
                    if user.leftmost >= (len(user) - 7) and user.leftmost > 0:
                        # decrement leftmost to shift cards to right
                        user.leftmost -= 1 

                    # play card
                    self.play_card(user.play(card))
                    user.played = True
                    # print(f"user played {card}") # testing

            # if played card is action card, execute action
            if user.played and self.game.get_top().action:
                color = None
                i = -1
                # if wild is played, prompt for color change
                if self.game.get_top().wild(): 
                    i = self.pick_color()
                    color = d.colors[i]
                    # print(f"user picked {color}") # testing

                self.game.do_action(color) # execute action of card

    def show_wild(self):
        '''Displays the wild card color selection pop-up'''
        self.screen.blit(self.wild_surf, self.wild_rect)

    def play_card(self, card):
        '''Moves a given card from the hand to the discard pile. Changes wild cards back to its
        default state, if it was the last card played'''
        self.game.discard(card) # discard the card
        self.screen.blit(self.screen, card.rect.copy()) # remove old card from hand view
        self.screen = card.display(self.screen, (d.discard_pos[0], d.discard_pos[1])) # move card to discard pile

        # if previous top card was wild, reset surface and color value back to white/none
        last = self.game.discarded[-2]
        if last.wild():
            last.change_color(d.wild_color)

    def clicked(self, pos, name):
        '''Returns True if the user's cursor is inside the box with the given name'''
        return self.images[name][1].collidepoint(pos)
