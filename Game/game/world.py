'''
Created on Jan 27, 2014

@author: otrebor
'''
import game.base.RectObject as RectObject
import game.base.CircleObject as CircleObject
import phys.PhysEng as PhysEng
import phys.Riged as Riged
import util.Vector2 as Vector2


class World:
    
    def __init__(self,gravity=Vector2.Vector2()):
        self.phyEng = PhysEng.PhysEng()
        self.objects = []
        self.gravity = gravity
        
    def createWall(self, x, y, w, h, color=(0, 0, 0)):
        wall = RectObject.RectObject(self,x, y, w, h, color)
        self.phyEng.add(wall.collider)
        wall.collider.static = True
        self.objects.append(wall)
        return wall
    
    def createCircle(self, x, y, r, color=(0, 0, 0), riged = True):
        cir = CircleObject.CircleObject(self,x, y, r, color)
        if riged:
            cir.addComponent(Riged.Riged(cir))
        self.phyEng.add(cir.collider)
        self.objects.append(cir)
        
        return cir
    
    def createRect(self, x, y, w, h, color=(0, 0, 0), riged = True):
        r = RectObject.RectObject(self,x, y, w, h, color)
        if riged:
            r.addComponent(Riged.Riged(r))
        self.phyEng.add(r.collider)
        self.objects.append(r)
        return r
    
    # not working
    def addSprite(self, img, x, y, w, h):
        
        sprite = sprite.Sprite(img, x, y, w, h)    
        # self.phyEng.add( sprite )
        
    def update(self, delta):
        # update game logic
        for obj in self.objects:
            obj.update(delta)
        # update physics
        self.phyEng.update(delta)
    
    def draw(self, screen):
        # call draw
        for obj in self.objects:
            obj.draw(screen)
