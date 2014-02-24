'''
Created on Feb 5, 2014

@author: rfloresx
'''
import game.components.Component as Component
import game.util.Vector2 as Vector2
import game.Game

class Warp(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.destPosX = None
        self.destPosY = None
        self.map_name = "map1"
    
    def OnTrigger(self,collision):
        if collision.other.name == "player":
            pos = collision.other.shape.position
            if self.destPosX != None:
                pos.x = self.destPosX
            if self.destPosY != None:
                pos.y = self.destPosY
            collision.other.shape.position = pos
            sun = self.gameObject.world.FindObject('sun')
            manager = self.gameObject.world.FindObject('manager')
            if self.map_name == 'random':
                r = game.Game.random.randrange(-1,7)
                if r == -1:
                    self.map_name = "Resources/maps/lost.txt"
                else:
                    self.map_name = "Resources/maps/rand/%i.txt"%(r)
                #print self.map_name
            self.gameObject.world.main.LoadMap(self.map_name, [collision.other,sun,manager])
            


def AddWarp(gameObject, defx, defy, dest_map):
    warp = gameObject.addComponent(Warp)
    warp.destPosX = defx
    warp.destPosY = defy
    warp.map_name = dest_map