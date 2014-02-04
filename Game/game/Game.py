'''
Created on Jan 30, 2014

@author: otrebor
'''
import sys

import pygame

import pygame.locals as locals
import util.Vector2 as Vector2
import world
import Resources

class KeyBoard:
    def __init__(self):
        self.keyState = {}
    def update(self):
        pygame.event.pump()
        for evt in pygame.event.get(locals.KEYDOWN):
            self.keyState[evt.key] = True
        for evt in pygame.event.get(locals.KEYUP):
            self.keyState[evt.key] = False
        
    def isKeyDown(self, key):
        if not self.keyState.has_key(key):
            return False
        else:
            return self.keyState[key]
    
    
class Game:
    RESOLUTION = (1024,768)
    GAMENAME = "null"
    INIT = False        
    def __init__ (self):
        self.INIT = True
        pygame.init()
        self.resources = Resources.Resources() 
        self.screen = pygame.display.set_mode(self.RESOLUTION)
        pygame.display.set_caption(self.GAMENAME)
        self.keyboard = KeyBoard()
        
        if not hasattr(self, 'world'):
            self.world = world.World(self, Vector2.Vector2(0, 0))
         
    def draw(self,debug = False):
        self.screen.fill((0, 0, 0,0))
        self.world.draw(self.screen)
        if debug:
            self.world.debDraw(self.screen)
        pygame.display.flip()
        return
    
    def update(self, delta):
        self.keyboard.update()
        pygame.event.pump()
        for evt in pygame.event.get():
            if evt.type == locals.QUIT:
                pygame.quit()
                sys.exit()
        if self.keyboard.isKeyDown(locals.K_ESCAPE):
            pygame.quit()
            sys.exit()
        
        self.world.update(delta)
        
        return
    
    def run(self):
        if not self.INIT:
            self.init()
        oldtime = pygame.time.get_ticks()
        pygame.time.wait(5)
        while True:
            newtime = pygame.time.get_ticks()
            delta = newtime - oldtime
            oldtime = newtime
            deltaf = delta / 1000.0
            self.update(deltaf)
            self.draw()
