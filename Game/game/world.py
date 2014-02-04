'''
Created on Jan 27, 2014

@author: otrebor
'''
import game.base.CircleObject as CircleObject
import game.base.RectObject as RectObject
import phys.PhysEng as PhysEng
import phys.Riged as Riged
import util.Vector2 as Vector2
import Terrain
import game.base.GameObject as GameObject
import game.phys.Collider as Collider
import game.phys.shapes.Polygon as Polygon


class World:
    def __init__(self, main, gravity=Vector2.Vector2()):
        self.terrain = Terrain.Terrain(main.resources,main.screen,self )
        self.phyEng = PhysEng.PhysEng()
        self.objects = []
        self.toRemove = []
        self.gravity = gravity
        self.main = main
    
        
    '''
    Terrain loading 
    '''
    def LoadTerrain(self,map_file, haveCollision):
        self.terrain.AddLayer(map_file, haveCollision )
    
    
    '''
    GameObject loading
    '''
    def createPolygon(self,points,static=True):
        obj = GameObject.GameObject(self)
        ((x,y),vectors) = Polygon.getPoligonFromPoints(points)
        obj.collider = Collider.PolygonCollider(obj,x,y,vectors )
        self.phyEng.add(obj.collider)
        obj.collider.static = static
        self.objects.append(obj)
        pass
        
    def createWall(self, x, y, w, h, color=(0, 0, 0)):
        wall = RectObject.RectObject(self, x, y, w, h, color)
        self.phyEng.add(wall.collider)
        wall.collider.static = True
        self.objects.append(wall)
        return wall
    
    def createCircle(self, x, y, r, color=(0, 0, 0), riged=True):
        cir = CircleObject.CircleObject(self, x, y, r, color)
        if riged:
            cir.addComponent(Riged.Riged)
        self.phyEng.add(cir.collider)
        self.objects.append(cir)
        
        return cir
    
    def createRect(self, x, y, w, h, color=(0, 0, 0), riged=True):
        r = RectObject.RectObject(self, x, y, w, h, color)
        if riged:
            r.addComponent(Riged.Riged)
        self.phyEng.add(r.collider)
        self.objects.append(r)
        return r
    
    
    
    def AddObject(self,gameObject):
        self.objects.append(gameObject)
        if gameObject.collider:
            self.phyEng.add(gameObject.collider)
    
    def Delete(self, gameObject):
        self.phyEng.remove(gameObject.collider)
        self.toRemove.append(gameObject)
        
    def update(self, delta):
        # update game logic
        for obj in self.objects:
            obj.update(delta)
        # update physics
        self.phyEng.update(delta)
        self.updateRemove()
    
    def updateRemove(self):
        for obj in self.toRemove:
            try:
                self.objects.remove(obj)
            except:
                pass
        self.toRemove = []
    
    def debDraw(self,screen):
        self.phyEng.draw(screen)
        
        
    def draw(self, screen):
        # call draw
        
        #draw first and second layer
        self.terrain.drawLayer(screen,(0,1))
        
        for obj in self.objects:
            obj.draw(screen)
        self.terrain.drawLayer(screen, (2,3))