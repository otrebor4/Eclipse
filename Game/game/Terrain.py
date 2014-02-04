'''
Created on Feb 3, 2014

@author: rfloresx
'''
import pygame
import Resources
import game.phys.Collider as Collider
import base.GameObject as GameObject

class TyleInfo:
    def __init__(self,pos, area=None, img=None):
        self.pos = pos
        self.area =area
        self.image = img
    
    def rect(self):
        (w,h) = (self.area[2], self.area[3]) if self.area != None else (64,64)
        return (self.pos[0],self.pos[1], w, h)
    
class Terrain:
    def __init__(self,resources = Resources.Resources(), screen = None, world =None):
        self.screen = screen
        self.layers = []
        self.resources = resources
        self.world = world
        
    '''
    bitmap is a list of TyleInfo, sourceData is a map of characters to images, haveCollision tell if Tyles should have collision
    '''
    def GenerateLayer(self, tyles):
        width = self.screen.get_width()
        height = self.screen.get_height()
        layer = pygame.Surface( [width,height], pygame.SRCALPHA, 32)
        layer = layer.convert_alpha()#create layer of the size of the screen
        
        #layer.fill( (0,0,0,0))#clear layer
        for tyle in tyles:
            layer.blit(tyle.image, tyle.pos, tyle.area)
        return layer.convert_alpha()
    
    '''
    load layer from file, if haveCollision will return a list of collider objects
    '''
    def AddLayer(self,map_file,haveCollision):
        size = 64
        tyles = []
        images = {}
        with open(map_file) as f:
            y = 0;
            for line in f:
                #get keymap
                if ':' in line:
                    line = line.rstrip('\n')
                    cmap = line.split(':')
                    images[cmap[0]] = self.resources.LoadImage(cmap[1])
                #load tyle
                else:
                    x = 0;
                    line = line.rstrip('\n')
                    for c in line:
                        if images.has_key(c):
                            tyles.append(TyleInfo((x,y),(0,0,size,size), images[c]))
                        x = x + size
                    y = y + size
        self.layers.append(self.GenerateLayer(tyles ))
        if haveCollision:
            for tyle in tyles:
                #domy way
                (x,y,w,h) = tyle.rect()
                block = GameObject.GameObject(self.world)
                block.collider = Collider.RectCollider( block,x,y,w-2,h-2)
                block.components.append(block.collider)
                self.world.AddObject(block)
                block.collider.static = True
                
                
               
                
                
    def drawLayer(self, screen, args):
        for arg in args:
            if arg < len(self.layers):
                screen.blit(self.layers[arg],(0,0))
                
                
                
                
                