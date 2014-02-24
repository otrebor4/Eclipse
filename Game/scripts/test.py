'''
Created on Feb 5, 2014

@author: rfloresx
'''
import game.components.Component as Component
import game.util.Vector2 as Vector2

class test1(Component.Component):
    def OnCollision(self,collision):
        if collision.other.name == "player":
            self.gameObject.world.resetWorld()
            self.gameObject.world.loadWorld( [self.gameObject, collision.other], [("Resources/testmap2_l1.txt",False), ("Resources/testmap2_l2.txt",True)])
            pos = collision.other.shape.position
            collision.other.shape.position = Vector2.Vector2(pos.x,600)
        
        
class testEventOnDamage(Component.Component):
    
    def OnDamage(self,damage):
        print "OnDamge"
        if damage.source.name == "player":
            print "player damage %f"%(damage.amount)


import game.bt.base as bt
class testBehavior(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.behavior = bt.BehaviorTree()
        self.data = {}
        self.behavior.data = self.data
        self.behavior.addAction(self.RandomMove)
        self.behavior.addAction(self.test)
    
    def update(self, delta):
        self.behavior.update(delta)
        
    def RandomMove(self,delta):
        print "random move"
        if not self.data.has_key("some"):
            self.data["some"] = False
        if not self.data["some"]:
            self.data["some"] = True
            return bt.State.Success
        else:
            self.data["some"] = False
        return bt.State.Failed
            
    def test(self,delta):
        print "test"
        if not self.data.has_key("dir"):
            self.data["dir"] = 0
        self.data["dir" ] = self.data["dir"]+delta
        
        if self.data["dir"] > 5:
            self.data["dir"] = 0
            print "ho"
            return bt.State.Success
        return bt.State.Running
        
        
        
        