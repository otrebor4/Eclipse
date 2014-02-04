'''
Created on Jan 27, 2014

@author: otrebor
'''
import game.base.Component as Component


# this = self
class ConstForse(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.gameObject = gameObject
        self.forse = Vector2.Vector2()
        
    def update(self, delta):
        if self.gameObject.collider != None:
            self.gameObject.collider.setSpeed(self.forse.scale(delta).add(self.gameObject.collider.speed))

