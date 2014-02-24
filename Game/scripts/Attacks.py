'''
Created on Feb 19, 2014

@author: rfloresx
'''

import game.components.Component as Component
import AnimationController
import game.util.Vector2 as Vector2
import Events
import game.components.Sprite as Sprite
import game.Game

def IsIgnored(obj, data={}):
    for key in data.keys():
        if hasattr(obj, key):
            if getattr(obj, key) in data[key]:
                return True
        if key == 'GameObject'and (obj in data[key]):
            return True
    return False
        
class Bullet(Component.Component):
    
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        if self.gameObject.riged != None:
            self.gameObject.riged.velocity = Vector2.Vector2()
        self.velocity = Vector2.Vector2()
        self.damage = 10
        self.source = None
        self.time = 0
        self.ignores = {}
        self.catch = {}
        self.nockback = 1
        
    def update(self, delta):
        if self.gameObject.riged == None and self.gameObject.shape != None:
            self.gameObject.shape.position = self.gameObject.shape.position.add(self.velocity.scale(delta))
        if self.gameObject.riged:
            v = self.gameObject.riged.velocity
            v2 = self.velocity
            if v.x != v2.x or v.y != v2.y:
                self.gameObject.riged.velocity = v2
        self.time -= delta
        if self.time < 0:
            self.gameObject.Destroy()
            
    def OnCollision(self, collisions):
        
        other = collisions.other
        if IsIgnored(other,self.ignores):
            return
        if self.catch.has_key(other) and self.catch[other]>0: 
            self.catch[other] -= 1
            return
        self.catch[other] = 10
        
        if not other.collider.static:
            other.shape.position = other.shape.position.add(self.velocity.normalize().scale(self.nockback))
        self.gameObject.world.Delete(self.gameObject);
        Events.OnDamage(self.source,self.damage).CallOn(collisions.other)

def createBullet(source, world, px, py, vx, vy, r, damage = 10, time = 2,ignores={}, file_name = None, nockback = 1):
    anim = None
    if not file_name:
        bullet = world.createCircle(px, py, r, (0, 0, 0), True)
    else:
        bullet = world.createCircGameObject(px,py,r,riged = True)
        Sprite.AddAnimator(bullet, file_name, game.Game.Game.Instance().resources, (-r,-r))
        anim = bullet.addComponent(AnimationController.AniationController)
    b = bullet.addComponent(Bullet)
    b.velocity = Vector2.Vector2(vx, vy)
    b.source = source
    b.damage = damage
    b.time = time
    b.ignores = ignores
    b.nockback = nockback
    if anim:
        anim.init(b.velocity)
    
class Explosion(Component.Component):
    def __init__(self,gameObject):
        
        Component.Component.__init__(self, gameObject)
        if self.gameObject.riged != None:
            self.gameObject.riged.velocity = Vector2.Vector2()
        self.damage = 10
        self.source = None
        self.time = .1
        self.ignores = {}
        self.catch = {}
        self.nockback = 10
        
    def update(self,delta):
        self.time -= delta
        if self.time < 0:
            self.gameObject.Destroy()
    
    def OnTrigger(self, collisions):
        
        other = collisions.other
        if IsIgnored(other, self.ignores):
            return
        if self.catch.has_key(other) and self.catch[other]>0: 
            self.catch[other] -= 1
            return
        self.catch[other] = 50
        #print "explosion"
        
        offset = self.nockback
        if collisions.distance < 0:
            offset = -offset
        if not other.collider.static:
            other.shape.position = other.shape.position.add(collisions.normal.scale(collisions.distance+offset))
        Events.OnDamage(self.source,self.damage).CallOn(collisions.other)

def createExplosion(source,world,px,py,r,  damage = 10, time = .1,ignores={}, file_name = None, nockback = 0):
    obj = world.createCircGameObject(px,py,r,riged = False,trigger = True)
    expl = obj.addComponent(Explosion)
    if file_name:
        anim = Sprite.AddAnimator(obj, file_name, game.Game.Game.Instance().resources, (0,0))
        anim.play('default', speed=20)
        
    expl.damage = damage
    expl.source = source
    expl.time = time
    expl.ignores = ignores
    expl.nockback = nockback














