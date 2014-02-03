import pygame
import sys
import math
import fileinput
import os

class create_tiles:
    def __init__(self, x, y, width, height, c):
        self.x = x
        self.y = y
        self.width = width
        self.heigh = height
        self.img = self.get_img(c)
        
    def get_img(self, tile_type):
        
        if tile_type == "g" or tile_type == "o":
            image = pygame.image.load("grass.png").convert()
            
        elif tile_type == 's':
            image = pygame.image.load("stone1.png").convert()
           
        elif tile_type == 't':
            image = pygame.image.load("tree1.png").convert()
           
        elif tile_type == 'd':
            image = pygame.image.load("dirt1.png").convert()
        
        elif tile_type == 'f':
            image = pygame.image.load("fence1.png").convert()

        return image
           
    def draw(self, screen):
        screen.blit( self.img, (self.x, self.y) )
                                            
                                                    
