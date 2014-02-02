'''
Created on Jan 28, 2014

@author: otrebor
'''
import game.base.Component as Component
import game.util.Vector2 as Vector2

#riged component require the gameObject to have a collider
class Riged(Component.Component):
    def __init__(self,gameObject, mass = 1.0, ivel = Vector2.Vector2() , applyGravity = True):
        Component.Component.__init__(self, gameObject)
        gameObject.riged = self
        self.mass = mass
        self.velocity = ivel
        self.applyGravity = applyGravity
    
    #apply movement to object
    def update(self,delta):
        if self.gameObject.collider.static:
            self.velocity = Vector2.Vector2()  #static object can't be moved by given speed must manually change position
        self.gameObject.shape.position = self.gameObject.shape.position.add( self.velocity.scale(delta))
        
        if self.applyGravity:
            grav = self.gameObject.world.gravity
            self.velocity = self.velocity.add(grav.scale(delta))
        
