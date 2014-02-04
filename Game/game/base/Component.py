'''
Created on Jan 28, 2014

@author: otrebor
'''

class Component:
    def __init__(self, gameObject):
        self.gameObject = gameObject
        self.main = gameObject.main
        
        
    def update(self, delta):
        pass
    
    def Destroy(self):
        if self.gameObject:
            self.gameObject.world.Destroy(self.gameObject)
