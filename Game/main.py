'''
Created on Jan 15, 2014

@author: Otrebor45
'''

import random

import game.Game as Game
import game.util.Vector2 as Vector2
import generate_map
from scripts import ClickToMove
from scripts import Shoter


class Test(Game.Game):
    
    
    def __init__(self):
        self.GAMENAME = "Test Game"
        Game.Game.__init__(self)
        self.world.LoadTerrain("Resources/testmap_layer1.txt", False)
        self.world.LoadTerrain("Resources/testmap_layer2.txt", True)
        self.world.LoadTerrain("Resources/testmap_layer3.txt", False)
        for i in range(0, 5):
            # c = self.world.createRect(250, 250, 5, 5, (10,10,50))
            c = self.world.createCircle(random.uniform(50, 450), random.uniform(50, 450), 10, (250, 0, 100))
            c.riged.velocity = Vector2.Vector2(random.uniform(-10, 10), random.uniform(-10, 10)).scale(0)
            
        r = self.world.createRect(250, 250, 25, 25, (10, 10, 50))
        r.addComponent(Shoter.Controller)
        # r.addComponent(ClickToMove.ClickToMove(r) )
        r.addComponent(Shoter.Shotter)
        #r.world.createPolygon( [(0,0),(0,768), (1024,768), (1024,0)])
        # r.addComponent(ClickToMove.TestMessage(r))
        self.world.createWall(0, 768, 1024, 100, (0, 0, 0))  # bottom
        self.world.createWall(0, -100, 1024, 100, (0, 0, 0))  # top
        self.world.createWall(-100, 0, 100, 768, (0, 0, 0))  # left
        self.world.createWall(1024, 0, 100, 768, (0, 0, 0))  # right
        
        # back ground
        
        #self.b1 = generate_map.create_map("Resources/testmap_layer1.txt" , self.screen)
        #self.b2 = generate_map.create_map("Resources/testmap_layer2.txt" , self.screen)
        #def draw(self, debug=True):
        #    return Game.Game.draw(self, debug=debug)
        
    '''    
    def draw(self, delta):
        self.b1.draw_layer(self.screen)
        self.b2.draw_layer(self.screen)
        return Game.Game.draw(self, delta)
    '''
if __name__ == '__main__':
    g = Test()
    g.run()
    
        
