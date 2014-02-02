'''
Created on Feb 1, 2014

@author: Otrebor45
'''
import GameObject
import Object
import game.util.Vector2 as Vector2

class TileObject(GameObject.GameObject):
    def __init__(self,world, x,y,w,h,image):
        GameObject.GameObject.__init__(self, world)
        self.min = (x,y)
        self.dim = (w,h)
        self.render = Object.Object()
        self.render.draw = lambda screen : self.drawTile(screen)
        self.pos = lambda: self.getPos()
        
    def getPos(self):
        return Vector2.Vector2(self.min[0],self.min[1])
    
    def drawTile(self,screen):
        pass