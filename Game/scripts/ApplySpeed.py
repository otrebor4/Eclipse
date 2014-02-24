'''
Created on Jan 28, 2014

@author: otrebor
'''
import game.components.Component as Component


class ApplySpeed(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.gameObject
        
    def update(self, delta):
        if self.gameObject != None and self.gameObject.collider != None:
            pos = self.gameObject.shape.position
            speed = self.gameObject.collider.speed
            self.gameObject.collider.setPos(pos.add(speed.scale(delta)))
