# Amelia Reiss
# design.py

'''This file contains the size, positions, and colors of most elements in the game,
relative to the screen size, allowing for scalability with window size.'''

# card colors
colors = ["indianred4", "mediumpurple3", "palegreen4", "steelblue4"]
wild_color = "grey90"

# colors used in GUI
screen_color = "gray75"
outline_color = "gray50"
highlighted_color = "palegoldenrod" # never got to implement :(

# screen dimensions
screen_w = 1000
screen_h = 700

border = screen_h // 140 # thickness of card border & outlines

# card dimensions, scaled to the screen size
card_w = screen_w // 11.11
card_h = screen_h // 6.1

# border_format = (startx, starty), (width, height)
# player hand position and outline centered to screen, a little above the bottom
hand_pos = (screen_w/2 - card_w*3.5, screen_h - card_h*1.6)
hand_border = (hand_pos[0] - border, hand_pos[1] - border), (card_w*7 + border*2, card_h + border*2)

# discard pile is centered to the middle of the screen, a little to the left
discard_pos = (screen_w/2 - card_w*1.5, screen_h/2 - card_h)
discard_border = (discard_pos[0] - border, discard_pos[1] - border), (card_w + border*2, card_h + border*2)

# draw pile is in line with the discard pile
draw_pos = (screen_w/2 + card_w*.5, screen_h/2 - card_h)
draw_border = (draw_pos[0] - border, draw_pos[1] - border), (card_w + border*2, card_h + border*2)

# buttons to navigate left and right through player hand are centered to the middle of the hand
scroll_w = card_h / 2
scroll_h = card_h // 2.5
left_pos = (hand_border[0][0] - scroll_w*1.25, hand_border[0][1] + hand_border[1][1] / 3)
right_pos = (hand_border[0][0] + hand_border[1][0] + scroll_w*.25, hand_border[0][1] + hand_border[1][1] / 3)

# end turn button centered a little above hand
end_w = card_h
end_h = card_h / 2
end_pos = (screen_w/2 - end_w/2, hand_border[0][1] - end_h - card_h/3)