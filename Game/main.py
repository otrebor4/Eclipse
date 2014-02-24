'''
Created on Jan 15, 2014

@author: Otrebor45
'''

import game.Game
import game.phys.shapes.Polygon as Polygon
from scripts import Player
from scripts import warps
from scripts import AnimationController
from scripts import EnemyBehaviors
from scripts import MainMenu
from scripts import CreateMap
from scripts import ObjectInfo
from scripts import Outcomes

import game.components.Navigator as Navigator
import game.components.LightSource as Light
import game.lib.yaml as yaml
import pygame
from game.components import Sprite
import pygame
import os

class Test(game.Game.Game):
    def __init__(self):
        self.DEBUG = False
        self.GAMENAME = "Test Game"
        self.currentSong = "nothing"
        #self.RESOLUTION = (1100,980)
        game.Game.Game.__init__(self)
        #self.ToggleFullScreen()
        #game.Game.pygame.display.toggle_fullscreen()
        #light = self.menuLight()
        #light = self.gameObject.world.main.initLight()
        #player = self.initPlayer()
        #enemy = self.initEnemy()
        #self.LoadMap("Resources/maps/map1_-2.txt",[player,light,enemy])
        self.gotoMainMenu()


    def goToGameOver(self):
        gameover = self.world.createObject()
        gameover.addComponent(Outcomes.GameOver)
        self.world.AddObject(gameover)
        self.world.LoadTerrain(None, [gameover])

    def goToGameWon(self):
    
        gamewon = self.world.createObject()
        gamewon.addComponent(Outcomes.GameWon)
        self.world.AddObject(gamewon)
        self.world.LoadTerrain(None, [gamewon])
    
    
    def gotoMainMenu(self):
        menu = self.world.createObject()
        menu.addComponent(MainMenu.Menu)
        self.world.AddObject(menu)
        self.world.LoadTerrain(None, [menu])
    
    def initManager(self):
        manager = self.world.createObject()
        manager.addComponent(CreateMap.WorldManager)
        manager.name = 'manager'
        return manager
    
    def initPlayer(self):
        '''
        =====player
        '''
       
        obj = self.world.createRectGameObject(800, 100, 56, 32)
        obj.name = "player"
        obj.addComponent(Player.Controller)
        obj.addComponent(Player.Shotter)
        
        Sprite.AddAnimator(obj, "Resources/sprites/robot.txt", self.resources, (-4,-32))
        obj.addComponent(AnimationController.AniationController)
        
        elight = obj.addComponent(Light.SpotLight)
        elight.setVals(50,50, (0,-8) )
        
        light = obj.addComponent(Light.FlashLight)
        light.setVals(350,250,180,100,20, (32,-16))
        
        health = obj.addComponent(ObjectInfo.Health)
        health.maxHealth = 1000
        health.health = 1000
        
        pygame.mouse.set_visible(False)
        obj.addComponent(Player.FlashLightController)
        
        return obj
        
    def initLight(self):
        light = self.world.createObject()
        light.name ='sun'
        elight = light.addComponent(Light.EnvironmentLight)
        elight.color = (00,00,00,255)
        return light

    def menuLight(self):
        light = self.world.createObject()
        light.name ='menu'
        elight = light.addComponent(Light.EnvironmentLight)
        elight.color = (00,00,00,00)
        return light
    
    
        
    def LoadMap(self,areaName, obj):
        self.world.LoadTerrain(areaName,obj )
    
    def Load(self,data):
        bot = self.world.createWall(0, 768, 1024, 100, (0, 0, 0))     # bottom
        top = self.world.createWall(0, -100, 1024, 100, (0, 0, 0))    # top
        left = self.world.createWall(-100, 0, 100, 768, (0, 0, 0))    # left
        right = self.world.createWall(1024, 0, 100, 768, (0, 0, 0))   # right
        
        if data.has_key("top"):
            warps.AddWarp(top, None, 730, data["top"])
        if data.has_key("bot"):
            warps.AddWarp(bot, None, 5, data["bot"])
        if data.has_key("left"):
            warps.AddWarp(left, 960, None, data["left"])
        if data.has_key("right"):
            warps.AddWarp(right, 5, None, data["right"])
        if data.has_key("music"):
            manager = self.world.FindObject('manager')
            if manager:
                mng = manager.getComponent('WorldManager')
                if mng:
                    mng.Play(data["music"] )
            
        self.world.saveTerrain("test_terrain.yaml")
                
                
               
                
 
        self.world.broadcast('load',data)
    
if __name__ == '__main__':
    g = Test()
    g.run()
    

