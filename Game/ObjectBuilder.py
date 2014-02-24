'''
Created on Feb 13, 2014

@author: Otrebor45
'''

import game.base.GameObject as GameObject
import game.Game as Game
import game.world as World
import game.lib.yaml as yaml


def saveObj(obj, fileName):
    with open(fileName, 'w') as outfile:
        yaml.dump(obj,outfile)

def loadObj(fileName):
    with open(fileName,'r') as infile:
        return yaml.load(infile)

import scripts.Player as Shoter
import game.components.LightSource as Light
def Player(world):
    r = world.createRect(490, 700, 25, 25, (10, 10, 50,255))
    r.addComponent(Shoter.Controller)
    r.addComponent(Shoter.Shotter)
    elight = r.addComponent(Light.SpotLight)
    elight.intensity = 150
    elight.radius = 150
    r.name = "player"
    return r

if __name__ == '__main__':
    _game = Game.Game()
    _world = World.World(_game)
    saveObj(Player(_world),"player.yaml")
    obj2 = loadObj("player.yaml")
    print obj2
    