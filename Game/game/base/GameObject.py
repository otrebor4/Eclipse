'''
Created on Jan 27, 2014

@author: otrebor
'''
import inspect
import sys


class GameObject:
    def __init__(self, world):
        self.world = world
        self.shape = None
        self.collider = None
        self.render = None
        self.components = []
        self.riged = None
        if world:
            self.main = world.main
            
    def addComponent(self, component):
        comp = None
        if component != None:
            if inspect.isclass(component):
                comp = component(self)
                self.components.append(comp)
            else:
                print "component %s is not a ClassType" % (component)
                raise
        return comp
    
    def getComponent(self, name):
        for comp in self.components:
            if comp.__class__.__name__ == name:
                return comp
    
    def getComponents(self, name):
        comps = []
        for comp in self.components:
            if comp.__class__.__name__ == name:
                comps.append(comp)
        return comps
        
    def update(self, delta):
        if self.components == None:
            return
        for comp in self.components:
            if comp.update != None:
                comp.update(delta)
        
    def draw(self, screen):
        if self.render != None:
            self.render.draw(screen)

    # currently support only one argument, must create a wraper to pass multiple variables
    def sendMessage(self, fname, arg):   
        if self.components == None:
            return
        for comp in self.components:
            try:
                getattr(comp, fname)(arg)
            except AttributeError:
                pass
            except:
                print "Unexpected error:", sys.exc_info()[0]
                raise
