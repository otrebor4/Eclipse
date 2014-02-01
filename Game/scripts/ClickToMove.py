'''
Created on Jan 28, 2014

@author: otrebor
'''
import game.base.Component as Component
import pygame
import game.util.Vector2 as Vector2
class ClickToMove(Component.Component):
    def __init__(self,gameObject):
        Component.Component.__init__(self, gameObject)
        self.targe = None
        self.shape = gameObject.shape
        self.speed = 100
        
    def update(self,delta):
        if self.shape == None:
            return
        pos = pygame.mouse.get_pos()
        (left, mid, right) = pygame.mouse.get_pressed()
        if left or mid or right:
            self.targe = Vector2.Vector2(pos[0],pos[1])
        if self.targe != None:
            if self.gameObject.riged != None:
                self.gameObject.riged.velocity = Vector2.Vector2()
            tdir = self.targe.sub(self.shape.position)
            dist = tdir.magnitude()
            vel = tdir.normalize().scale(self.speed*delta)
            if dist < vel.magnitude():
                self.shape.position = self.targe.scale(1)
                self.targe = None
            else:
                self.shape.position = self.shape.position.add(vel)
    
        
class TestMessage(Component.Component):
    def __init__(self,gameObject):
        Component.Component.__init__(self, gameObject)
        
    def OnCollision(self,collision):
        #collision.other
        #collision.normal
        print "OnCollision"
        