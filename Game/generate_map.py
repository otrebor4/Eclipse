import pygame
import sys
import math
import fileinput
import os
import create_tiles

class create_map:
    def __init__(self, map_file, screen):
        self.tiles = []
        self.generate_tiles(map_file, screen)
        
    def generate_tiles(self, map_file, screen):
        
        y = 0;
        with open(map_file) as f:
            for line in f:
                x = 0;
                line = line.rstrip('\n')
                for c in line:
                    
                    if c != 'g' or c != 'o':
                        self.tiles.append(create_tiles.create_tiles(x, y, 64, 64, c))
                    else:
                        self.tiles.insert(0, create_tiles.create_tiles(x, y, 64, 64, c))
                    x = x + 64               
                y = y + 64

    def draw_layer(self,screen):      
        for t in self.tiles:
            t.draw(screen)

