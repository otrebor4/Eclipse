'''
Created on Jan 28, 2014

@author: otrebor
'''
import pygame

import GameObject
import Object
import game.phys.Collider as Collider


class RectObject(GameObject.GameObject):
    def __init__(self, world, x, y, w, h, color):
        GameObject.GameObject.__init__(self, world)
        self.color = color
        self.collider = Collider.RectCollider(self, x, y, w, h)
        self.components.append(self.collider)
        self.render = Object.Object()
        self.render.draw = lambda screen: self.drawRect(screen)
        #self.pos = lambda: self.collider.pos()
        
        
    def rect(self):
        x = self.shape.Left()
        y = self.shape.Top()
        w = self.shape.Width()
        h = self.shape.Height()
        return pygame.rect.Rect(x, y, w, h)
        
    def drawRect(self, screen):
        pygame.draw.rect(screen, self.color, self.rect())
        
