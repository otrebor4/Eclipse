'''
Created on Jan 28, 2014

@author: otrebor
'''
import pygame

import GameObject
import Object
import game.phys.Collider as Collider


class CircleObject(GameObject.GameObject):
    def __init__(self, world, x, y, r, collor):
        GameObject.GameObject.__init__(self, world)
        
        self.collor = collor
        self.collider = Collider.CircleCollider(self, x, y, r)
        self.components.append(self.collider)
        self.render = Object.Object()
        self.render.draw = lambda screen: self.drawCircle(screen)
        self.pos = lambda: self.collider.pos()
        
        
    def drawCircle(self, screen):
        pos = self.shape.position
        pygame.draw.circle(screen, self.collor, (int(pos.x), int(pos.y)), int(self.shape.radius))
        
        
        
        
        
        
