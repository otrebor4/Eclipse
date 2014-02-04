import fileinput
import math
import sys

import pygame

import generate_map


pygame.init()

# creates screen, displays caption, creates sprite
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Map_Maker")
l1 = generate_map.create_map("testmap_layer1.txt" , screen)
l2 = generate_map.create_map("testmap_layer2.txt", screen)

while True:
    l1.draw_layer(screen)
    l2.draw_layer(screen)
   
    pygame.display.flip()

    # process event handlers

    pygame.event.pump()
    for evt in pygame.event.get():
        
        # exits screen if escape or 'x' box is clicked
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
