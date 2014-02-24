'''
Created on Feb 15, 2014

@author: Otrebor45
'''

import game.components.Component as Component

class AniationController(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.animator = gameObject.getComponent("SpriteAnim")
    
    def init(self,vel):
        riged = self.gameObject.riged
        if riged:
            angle = vel.angle()
            anim = self.gameObject.getComponent("SpriteAnim")
            if anim is None:
                return
            speed = 0
            if angle >= 325 or angle < 45:#moving right
                anim.play("right", speed)
            elif angle < 135: #moving down
                anim.play("down",speed)
            elif angle < 225:#moving left
                anim.play("left", speed)
            elif angle < 325:#moving up
                anim.play("up",speed)
    
    def update(self,delta):
        riged = self.gameObject.riged
        #anim = Sprite.SpriteAnim()
        anim = self.animator
        if not anim:
            print "animator don't found"
            return
        if riged:
            speed = riged.velocity.magnitude() *0.15
            angle = riged.velocity.angle()
            (x,y) = riged.velocity.normalize().xy()
            (x,y) = self.calDirection((x,y))
            
            if speed < 1: #no moving
                anim.setSpeed(0)
                return
            if speed < 5:
                speed = 5
            if speed > 10:
                speed = 10
            if angle >= 325 or angle < 45:#moving right
                anim.play("right", speed)
            elif angle < 135: #moving down
                anim.play("down",speed)
            elif angle < 225:#moving left
                anim.play("left", speed)
            elif angle < 325:#moving up
                anim.play("up",speed)
            
 
    
    def calDirection(self, (x,y)):
        if x > 0:
            x = 1
        if x < 0:
            x = -1
        if y > 0:
            y = 1
        if y < 0:
            y = -1
        return (x,y)