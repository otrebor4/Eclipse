'''
Created on Feb 1, 2014

@author: Otrebor45
'''

import game.components.Render as Render
import game.phys.physutil as Util
import Events
import pygame



class Menu(Render.GUIComponent):
    def __init__(self, gameObject):
        Render.GUIComponent.__init__(self, gameObject)
        pygame.mixer.music.load("Resources/songs/TittleScreenMusic.wav"  )
        pygame.mixer.music.play()
        self.time = 10
        
    def update(self,delta):
        self.time -= 1
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.time <= 0:
            intro = self.gameObject.world.createObject()
            intro.addComponent(Intro)
            self.gameObject.world.main.LoadMap(None, [intro])
        
    def OnGUI(self, screen):
        background = pygame.image.load("Resources/background.jpg")
        screen.fill( (255, 255, 255) )
        screen.blit(background, (0,0))

        font = pygame.font.SysFont("agency fb", 72)
        font.set_bold(True)
        titletext = font.render("STRANDED", 1, (255,0,0))
        titletextpos = titletext.get_rect()
        titletextpos.centerx = screen.get_rect().centerx

        font.set_bold(False)
        starttext = font.render("Press Space to start", 1, (255,0,0))
        starttextpos = starttext.get_rect()
        starttextpos.centerx = screen.get_rect().centerx
        starttextpos.centery = screen.get_rect().centery
        starttextpos.y = starttextpos.y + 200

        exittext = font.render("Press Esc to exit", 1, (255,0,0))
        exittextpos = exittext.get_rect()
        exittextpos.centerx = screen.get_rect().centerx
        exittextpos.centery = screen.get_rect().centery
        exittextpos.y = exittextpos.y + 275

        screen.blit(titletext, titletextpos)
        screen.blit(starttext, starttextpos)
        screen.blit(exittext, exittextpos)
        
class Intro(Render.GUIComponent):
    def __init__(self, gameObject):
        Render.GUIComponent.__init__(self, gameObject)
        self.time = 10
        self.message = 0
        self.space = 0
    def update(self, delta):

        if self.time > 0:
            self.time -= 1
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.time == 0:
            self.space += 1
            self.time = 5
            
        if self.space == 6:
            light = self.gameObject.world.main.initLight()
            player = self.gameObject.world.main.initPlayer()
            manager = self.gameObject.world.main.initManager()
            #enemy = self.gameObject.world.main.initEnemy()"Resources/maps/lost.txt"
            #self.gameObject.world.main.LoadMap("Resources/maps/rand/6.txt",[player,light,manager])
            self.gameObject.world.main.LoadMap("Resources/maps/map1_-2.txt",[player,light,manager])
            
    def OnGUI(self, screen):
        background = pygame.image.load("Resources/background.jpg")
        screen.fill( (255, 255, 255) )
        screen.blit(background, (0,0))
        font = pygame.font.SysFont("agency fb", 36)
        font.set_bold(False)

        if self.space == 0:
            text = font.render("Once upon a time there was a robot name Roborto. He was cruising through", 1, (255,255,255))
            text2 = font.render("space when his spaceship suddenly started to malfunction.", 1, (255,255,255))
        elif self.space == 1:
            text = font.render("Roborto had made a costly mistake, he never made sure he had enough fuel for the trip!", 1, (255,255,255))
            text2 = font.render("Without any fuel left, Roborto quickly altered his course to the nearest planet.", 1, (255,255,255))
        elif self.space == 2:
            text = font.render("With his ship about to crash land, Roborto had no choice but to push the eject button.", 1, (255,255,255))
            text2 = font.render("He must now travel through an unknown island in hopes of finding his ship and fuel.", 1, (255,255,255))
        elif self.space == 3:
            text = font.render("There's only one problem, Roborto's own power supply is decaying.", 1, (255,255,255))
            text2 = font.render("He must hurry and complete his objectives before he is shut down from existence.", 1, (255,255,255))
        elif self.space == 4:
            text = font.render("Beware, you are not alone on this island.", 1, (255,255,255))
            text2 = font.render("You're only way to live is to kill.", 1, (255,255,255))
        elif self.space == 5:
            text = font.render("Hint: Roborto can harness fuel from the remains of the dead (animals/beasts/etc).", 1, (255,255,255))
            text2 = font.render("Good Luck!", 1, (255,255,255))

        
        text3 = font.render("Press space to continue.", 1, (255,255,255))
        
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_rect().centery
        textpos.y -= 200
        textpos2 = text2.get_rect()
        textpos2.centerx = screen.get_rect().centerx
        textpos2.y = textpos.y + 50
        textpos3 = text3.get_rect()
        textpos3.centerx = screen.get_rect().centerx
        textpos3.y = textpos2.y + 50
        
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)
        screen.blit(text3, textpos3)
        
        font = pygame.font.SysFont("agency fb", 48)
        font.set_bold(True)
        text = font.render("Controls", 1, (255,255,255))
        textpos = text.get_rect()
        textpos.centery = screen.get_rect().centery
        textpos.centerx = screen.get_rect().centerx
        textpos.y += 200
        screen.blit(text, textpos)
        
        font = pygame.font.SysFont("agency fb", 36)
        font.set_bold(False)
        text = font.render("W- Up, S - Down, A - Left, D - Right", 1, (255,255,255))
        textpos = text.get_rect()
        textpos.centery = screen.get_rect().centery
        textpos.centerx = screen.get_rect().centerx
        textpos.y += 250
        screen.blit(text, textpos)

        text = font.render("Hold Space to Run, and Left Click to shoot", 1, (255,255,255))  
        textpos.centery = screen.get_rect().centery
        textpos.centerx = screen.get_rect().centerx
        textpos.y += 300
        screen.blit(text, textpos)

        text = font.render("Right Click to use Force Field", 1, (255,255,255))  
        textpos.centery = screen.get_rect().centery
        textpos.centerx = screen.get_rect().centerx
        textpos.y += 350
        screen.blit(text, textpos)


      
        
        
