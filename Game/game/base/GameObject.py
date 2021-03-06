'''
Created on Jan 27, 2014

@author: otrebor
'''
import inspect
import sys
import game.lib.yaml as yaml

class Object():
    def __init__(self):
        pass

class GameObject(yaml.YAMLObject):
    yaml_tag = u'!GameObject'
    
    def __getstate__(self):
        data = {}
        data['name'] = self.name 
        data['shape'] = self.shape
        data['collider'] = self.collider
        data['renders'] = self.renders
        data['GUIs'] = self.GUIs
        data['components'] = self.components
        data['riged'] = self.riged
        data['type'] = self.type
        return data
    
    def __init__(self, world):
        self.name = "object"
        self.type = 'object'
        self.world = world
        self.shape = None
        self.collider = None
        self.renders = []
        self.GUIs = []
        self.components = []
        self.riged = None
        if world:
            self.main = world.main
        
    def addComponent(self, component):
        comp = None
        if component != None:
            if inspect.isclass(component):
                comp = component(self)
                # self.components.append(comp)
            else:
                print "component %s is not a ClassType" % (component)
                raise
        return comp
    
    def getComponent(self, name):
        for comp in self.components:
            if comp.__class__.__name__ == name:
                return comp
        return None
    
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
        for render in self.renders:
            render.draw(screen)
            
    def OnGUI(self,screen):
        for gui in self.GUIs:
            gui.OnGUI(screen)
            
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
    def Destroy(self):
        if self.world:
            self.world.Delete(self)
        
        
if __name__ == '__main__':
    obj = GameObject(None)
    s = yaml.dump(obj)
    obj2 = yaml.load(s)
    print yaml.dump(obj2)
    