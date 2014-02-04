import fileinput
import math
import os
import sys

import pygame

'''
<ch> file/direct
<ch> file/direct

xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
'''

class create_tiles:
    def __init__(self, x, y, width, height, c):
        self.x = x
        self.y = y
        self.width = width
        self.heigh = height
        self.img = self.get_img(c)
        self.map = {}
        
    def get_img(self, tile_type):
        #image = pygame.image.load(self.map[tile_type]).convert()
        
        if tile_type == "g" or tile_type == "o":
            image = pygame.image.load("Resources/grass.png").convert()
            
        elif tile_type == 's':
            image = pygame.image.load("Resources/stone1.png").convert()
           
        elif tile_type == 't':
            image = pygame.image.load("Resources/tree1.png").convert()
           
        elif tile_type == 'd':
            image = pygame.image.load("Resources/dirt1.png").convert()
        
        elif tile_type == 'f':
            image = pygame.image.load("Resources/fence1.png").convert()

        return image
           
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
                                            
                                                    
