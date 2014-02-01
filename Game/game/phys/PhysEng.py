'''
Created on Jan 29, 2014

@author: otrebor
'''
import physutil

class PhysEng:
    
    def __init__(self):
        self.objects = []
        
    def objCount(self):
        return len(self.objects)
    
    #object is a collider
    def add(self, obj):
        self.objects.append(obj)
    
    def remove(self, obj):
        self.objects.remove(obj)
        
    def update(self, delta):
        size = self.objCount()
        for i in range(0, size):
            for j in range(i, size):
                if i != j:  # is not the same
                    self.handleCollision(self.objects[i], self.objects[j])
                    
    def handleCollision(self, obj1, obj2):
        dis = 2
        info = physutil.testCollision(obj1, obj2)
        if info != None: 
            if not obj1.static or not obj2.static:
                if obj1.static:
                    move = info.direction.scale(info.distance+dis)
                    info.shape2.position = info.shape2.position.add(move)
                elif obj2.static:
                    move = info.direction.scale(info.distance+dis)
                    info.shape1.position = info.shape1.position.add(move)
                else:  
                    move = info.direction.scale((info.distance+dis)/2)
                    info.shape1.position = info.shape1.position.add(move)
                    info.shape2.position = info.shape2.position.add(move.scale(-1))
            physutil.HandleCollision(obj1, obj2, info)
            self.callOnCollision(obj1, obj2, info)
    
    '''
    Send message to obj1 and obj2 to call OnCollision
    arg is an object with other (GameObject), normal(Vector2)
    '''
    def callOnCollision(self, obj1, obj2,info):
        arg = Collision()
        arg.other = obj2.gameObject
        arg.normal = info.direction
        obj1.gameObject.sendMessage("OnCollision", arg)
        arg = Collision()
        arg.other = obj1.gameObject
        arg.normal = info.direction.scale(-1)
        obj2.gameObject.sendMessage("OnCollision", arg)
        
class Collision:
    def __init__(self):
        self.other = None
        self.normal = None
        