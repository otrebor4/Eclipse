'''
Created on Feb 1, 2014

@author: Otrebor45
'''
import pygame

import game.base.Component as Component
import game.util.Vector2 as Vector2


class Bullet(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        if self.gameObject.riged != None:
            self.gameObject.riged.velocity = Vector2.Vector2()
        self.velocity = Vector2.Vector2()
        
    def update(self, delta):
        if self.gameObject.riged == None and self.gameObject.shape != None:
            self.gameObject.shape.position = self.gameObject.shape.position.add(self.velocity.scale(delta))
        if self.gameObject.riged:
            v = self.gameObject.riged.velocity
            v2 = self.velocity
            if v.x != v2.x or v.y != v2.y:
                self.gameObject.riged.velocity = v2
            
        
    def OnCollision(self, collisions):
        self.gameObject.world.Delete(self.gameObject);
        # self.gameObject.world.Delete(collisions.other)
      
class Shotter(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.time = 0
        
    def update(self, delta):
        self.time -= delta
        if self.time > 0:
            return
        (left, mid, right) = pygame.mouse.get_pressed()
        if left or mid or right:
            pos = pygame.mouse.get_pos()
            bdir = Vector2.Vector2(pos[0], pos[1]).sub(self.gameObject.shape.position).normalize()
            spos = self.gameObject.shape.Center().add(bdir.scale(self.gameObject.shape.Radius()))
            bdir = bdir.scale(500)
            createBullet(self.gameObject.world, spos.x, spos.y, bdir.x, bdir.y, 5)
            self.time = .1
            
class Controller(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.coldown = 0
        if self.gameObject.riged:
            self.gameObject.riged.kinematic = True
    def update(self, delta):
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
        
        
    
def createBullet(world, px, py, vx, vy, r):
    bullet = world.createCircle(px, py, r, (0, 0, 0), True)
    b = bullet.addComponent(Bullet)
    b.velocity = Vector2.Vector2(vx, vy)
    
    
