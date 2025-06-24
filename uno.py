# Amelia Reiss
# uno.py

import pygame
from random import randint
from game import Game
from gui import GUI
import design as d

def main():
    # setup screen
    pygame.init()
    screen = pygame.display.set_mode((d.screen_w, d.screen_h))
    pygame.display.set_caption("Uno")

    # create game objects
    game = Game(2)
    gui = GUI(screen, game)
    user = game.players[0]
    op = game.players[1]

    # main game loop
    while len(user) != 0 and len(op) > 0:
        # set to false to allow multiple turns from action cards
        player = game.players[game.turn]
        player.drawn = False
        player.played = False

        # Player takes turn
        while game.turn == 0 and len(user) > 0: 
            gui.user_turn()
            gui.update() 
            pygame.display.flip()

        # dummy AI takes turn and plays whatever is the first valid move
        while game.turn != 0 and len(op) > 0:
            game, gui, easy_player(game, gui)
            gui.update() 
            pygame.display.flip()

    # print respective end game screen
    print("*" * 10)
    if len(user) == 0:
        print("USER WON")
    else:
        print("OP WON")
    print("*" * 10)

    pygame.quit()

def easy_player(game, gui):
    '''Easy opponent plays the first valid card possible, or draws. This
    player does not ever play a second card after drawing.'''
    op = game.players[1]
    # if there is a valid move, play first card
    valid_moves = game.get_valid_cards(op)
    if len(valid_moves) != 0:
        game.discard(op.play(valid_moves[0]))
        # print(f"{op.name} played {valid_moves[0]}") # testing
        op.played = True

        # if card is wild, pick random color to change to
        color = None
        if game.get_top().wild():
            color = d.colors[randint(0, 3)]

        # execute action card
        if game.get_top().action:
            game.do_action(color)
            # create delay between sequential card plays
            if game.get_top().value != "wild":
                gui.update()
                pygame.display.flip()
                pygame.time.wait(1200)

    else: # otherwise, draw
        op.drawn = game.give_cards(op) 
        pygame.time.wait(1200)
    
    # end turn after making move
    if op.drawn or op.played:
        game.change_turn()

    return game, gui


if __name__ == "__main__":
    main()