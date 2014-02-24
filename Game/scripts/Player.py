'''
Created on Feb 1, 2014

@author: Otrebor45
'''
import pygame

import game.components.Component as Component
import game.util.Vector2 as Vector2
import Attacks

class Shotter(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.time = 0
        self.catche = Vector2.Vector2()
        self.gs = pygame.mixer.Sound( "Resources/songs/gunshot.wav" )
        self.ss = pygame.mixer.Sound( "Resources/songs/ShieldSound.wav" )
        
        
    def update(self, delta):
        self.time -= delta
        if self.time > 0:
            return
        riged = self.gameObject.riged
        if riged:
            center = self.gameObject.shape.Center()
            world = self.gameObject.world
            radius = self.gameObject.shape.Radius()
            
            bdir = riged.velocity.normalize()
            if bdir.magnitude() == 0:
                bdir = self.catche
            self.catche = bdir
        
            (left, mid, right) = pygame.mouse.get_pressed()
            if left:
                self.gs.play()
                spos = center.add(bdir.scale(radius))
                bdir = bdir.scale(500)
                Attacks.createBullet(self.gameObject,world, spos.x, spos.y-24, bdir.x, bdir.y, 5,damage=10, time = 2, ignores={'GameObject':[self.gameObject]},file_name='Resources/sprites/bullet.txt')
                self.time = .25
            if right:
                self.ss.play()
                spos = center
                Attacks.createExplosion(self.gameObject, world, spos.x, spos.y, 40, damage = 10, time = .25, ignores={'GameObject':[self.gameObject]}, file_name='Resources/sprites/explosion1.txt')
                self.time = .5
                pass
            if mid:
                pass
         
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
        self.health = None
        
    def update(self, delta):
        if not self.health:
            self.health = self.gameObject.getComponent('Health')
        else:
            self.health.Damage(delta*3)
        self.coldown -= delta
        speed = self.walkSpeed
        if self.coldown <= 0:
            self.coldown += .01
            vel = Vector2.Vector2()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
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
        
    def OnDie(self, data):
        self.gameObject.Destroy()
        self.gameObject.world.broadcast("OnPlayerDie",{'player':self})
        
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
    


    
