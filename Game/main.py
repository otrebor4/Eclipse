'''
Created on Jan 15, 2014

@author: Otrebor45
'''

import game.util.Vector2 as Vector2
import random


from scripts import ClickToMove
import game.Game as Game
import generate_map
from scripts import Shoter


class Test(Game.Game):
    def __init__(self):
        self.GAMENAME = "Test Game"
        Game.Game.__init__(self)
        for i in range(0,5):
            #c = self.world.createRect(250, 250, 5, 5, (10,10,50))
            c = self.world.createCircle(random.uniform(50,450), random.uniform(50,450), 10, (250,0,100))
            c.riged.velocity = Vector2.Vector2(random.uniform(-10,10), random.uniform(-10,10)).scale(0)
            
        r = self.world.createRect(250, 250, 25, 25, (10,10,50))
        r.addComponent(Shoter.Controller(r))
        #r.addComponent(ClickToMove.ClickToMove(r) )
        r.addComponent(Shoter.Shotter(r))
        #r.addComponent(ClickToMove.TestMessage(r))
        self.world.createWall(1, 768, 1024, 100, (0,0,0)) #bottom
        self.world.createWall(1, -100, 500, 100, (0,0,0))   #top
        self.world.createWall(-99, 0, 100, 500, (0,0,0))   #left
        self.world.createWall(500, 0, 100, 500, (0,0,0)) #right
        
        #back ground
        self.b1 = generate_map.create_map("testmap_layer1.txt" , self.screen)
        self.b2 = generate_map.create_map("testmap_layer2.txt" , self.screen)
        
    def draw(self, delta):
        self.b1.draw_layer(self.screen)
        self.b2.draw_layer(self.screen)
        return Game.Game.draw(self, delta)
    
if __name__ == '__main__':
    g = Test()
    g.run()
    
        
