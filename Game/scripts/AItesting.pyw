'''
Created on Feb 1, 2014

@author: Otrebor45
'''
import pygame
import time
import random
import game.components.Component as Component
import game.util.Vector2 as Vector2
import math

class Movement(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.cooldown = 0
        s = random.uniform(-1,2)
        if(s >= 1):
            self.gameObject.riged.velocity = Vector2.Vector2(0,math.pow(-1, random.randint(1, 10))).scale(50)
        elif(s<1) and (s>=0):
            self.gameObject.riged.velocity = Vector2.Vector2(math.pow(-1, random.randint(1, 10)),0).scale(50)
        else:
            self.gameObject.riged.velocity = Vector2.Vector2(0,0)
            
        if self.gameObject.riged:
            self.gameObject.riged.kinematic = True
            
    def update(self, delta):
        self.cooldown -=delta
        if(self.cooldown<=0):
            self.cooldown=random.randint(4, 10)
            s = random.uniform(-1,2)
            if(s >= 1):
                self.gameObject.riged.velocity = Vector2.Vector2(0,math.pow(-1, random.randint(1, 10))).scale(50)
            elif(s<1) and (s>=0):
                self.gameObject.riged.velocity = Vector2.Vector2(math.pow(-1, random.randint(1, 10)),0).scale(50)
            else:
                self.gameObject.riged.velocity = Vector2.Vector2(0,0)
                self.cooldown= 1.5
    def OnCollision(self, collision):
        self.gameObject.riged.velocity = collision.normal.normal().scale(50*math.pow(-1, random.randint(1, 10)))

 
             
    
        '''
        self.coldown -= delta
        if self.coldown <= 0:
            vel = Vector2.Vector2()
            
            if (self.main.keyboard.isKeyDown(pygame.K_w)):
                vel = vel.add(Vector2.Vector2(0, -1))
            if (self.main.keyboard.isKeyDown(pygame.K_s)):
                vel = vel.add(Vector2.Vector2(0, 1))
            if (self.main.keyboard.isKeyDown(pygame.K_a)):
                vel = vel.add(Vector2.Vector2(-1, 0))
            if (self.main.keyboard.isKeyDown(pygame.K_d)):
                vel = vel.add(Vector2.Vector2(1, 0))
            if self.gameObject.riged:
                self.gameObject.riged.velocity = vel.scale(100)
        
        '''
    
