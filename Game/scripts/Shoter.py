'''
Created on Feb 1, 2014

@author: Otrebor45
'''
import pygame

import game.components.Component as Component
import game.util.Vector2 as Vector2
import Events
import Attacks


class Bullet(Component.Component):
    
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        if self.gameObject.riged != None:
            self.gameObject.riged.velocity = Vector2.Vector2()
        self.velocity = Vector2.Vector2()
        self.damage = 10
        self.source = None
        self.time = 0
        
    def update(self, delta):
        if self.gameObject.riged == None and self.gameObject.shape != None:
            self.gameObject.shape.position = self.gameObject.shape.position.add(self.velocity.scale(delta))
        if self.gameObject.riged:
            v = self.gameObject.riged.velocity
            v2 = self.velocity
            if v.x != v2.x or v.y != v2.y:
                self.gameObject.riged.velocity = v2
        self.time += delta
        if self.time > 2:
            self.gameObject.Destroy()
            
    def OnCollision(self, collisions):
        self.gameObject.world.Delete(self.gameObject);
        Events.OnDamage(self.source,self.damage).CallOn(collisions.other)
        
        # self.gameObject.world.Delete(collisions.other)
    
class Shotter(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.time = 0
        self.catche = Vector2.Vector2()
    def update(self, delta):
        self.time -= delta
        if self.time > 0:
            return
        riged = self.gameObject.riged
        if riged:
            bdir = riged.velocity.normalize()
            if bdir.magnitude() == 0:
                bdir = self.catche
            self.catche = bdir

            keys = pygame.key.get_pressed()
            if keys[pygame.K_j]:
                spos = self.gameObject.shape.Center().add(bdir.scale(self.gameObject.shape.Radius()))
                bdir = bdir.scale(500)
                Attacks.createBullet(self.gameObject, self.gameObject.world, spos.x, spos.y, bdir.x, bdir.y, 5, damage = 10, time=2,
                                      ignores={'GameObject':[self.gameObject]}, file_name='Resources/sprites/bullet.txt', nockback=10)
                #createBullet(self.gameObject,self.gameObject.world, spos.x, spos.y, bdir.x, bdir.y, 5)
                self.time = .1
'''                
            (left, mid, right) = pygame.mouse.get_pressed()
            if left:
                #pos = pygame.mouse.get_pos()
                #bdir = #Vector2.Vector2(pos[0], pos[1]).sub(self.gameObject.shape.position).normalize()
                spos = self.gameObject.shape.Center().add(bdir.scale(self.gameObject.shape.Radius()))
                bdir = bdir.scale(500)
                createBullet(self.gameObject,self.gameObject.world, spos.x, spos.y, bdir.x, bdir.y, 5)
                self.time = .1
            if right:
                pass
            if mid:
                pass
 '''   
    
class Controller(Component.Component):
    yaml_tag = u'!Controller'
    def __getstate__(self):
        data = Component.Component.__getstate__(self)
        data['walkSpeed'] = self.walkSpeed
        data['runSpeed'] = self.runSpeed
        return data
    
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.coldown = 0
        if self.gameObject.riged:
            self.gameObject.riged.kinematic = True
        self.walkSpeed = 100
        self.runSpeed = self.walkSpeed * 2
        
    def update(self, delta):
        self.coldown -= delta
        speed = self.walkSpeed
        if self.coldown <= 0:
            self.coldown += .01
            vel = Vector2.Vector2()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_k]:
                speed = self.runSpeed
            if keys[pygame.K_w]:
                vel = vel.add(Vector2.Vector2(0, -1))
            if keys[pygame.K_s]:
                vel = vel.add(Vector2.Vector2(0, 1))
            if keys[pygame.K_a]:
                vel = vel.add(Vector2.Vector2(-1, 0))
            if keys[pygame.K_d]:
                vel = vel.add(Vector2.Vector2(1, 0))
            if self.gameObject.riged:
                vel =  lerp(self.gameObject.riged.velocity,vel.normalize().scale(speed),6*delta)
                vel = vel if vel.magnitude() > .01 else Vector2.Vector2()
                self.gameObject.riged.velocity = vel
        
        
class FlashLightController(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        pass
    def update(self,delta):
        riged = self.gameObject.riged
        #anim = Sprite.SpriteAnim()
        light = self.gameObject.getComponent('FlashLight')
        
        if riged:
            speed = riged.velocity.magnitude() *1
            angle = riged.velocity.angle()
            if speed < 1: #no moving
                return
            light.angle = angle
        
def lerp(start,end,lval):
    mid = end.sub(start)
    mid = mid.scale(lval)
    return start.add(mid)
    

    
