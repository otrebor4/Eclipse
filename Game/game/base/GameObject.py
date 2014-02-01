'''
Created on Jan 27, 2014

@author: otrebor
'''
import sys
import inspect

class GameObject:
    def __init__(self, world):
        self.world = world
        self.shape = None
        self.collider = None
        self.render = None
        self.components = []
        self.riged = None
        
    def setPos(self, pos):
        if self.collider != None:
            self.collider.setPos(pos)
            
    def setVel(self, vel):
        if self.collider != None:
            self.collider.setVel(vel)
    
    def addVel(self, acc):
        if self.collider != None:
            self.collider.addVel(acc)
    
    def addComponent(self, component, arg = None):
        if component != None:
            if inspect.isclass(component):
                component = component(arg)
            self.components.append(component)
    
    
    def update(self, delta):
        if self.components == None:
            return
        for comp in self.components:
            if comp.update != None:
                comp.update(delta)
        
    def draw(self, screen):
        if self.render != None:
            self.render.draw(screen)

    #currently support only one argument, must create a wraper to pass multiple variables
    def sendMessage(self, fname, arg):   
        if self.components == None:
            return
        for comp in self.components:
            try:
                getattr(comp,fname)(arg)
            except AttributeError:
                pass
            except:
                print "Unexpected error:", sys.exc_info()[0]
                raise