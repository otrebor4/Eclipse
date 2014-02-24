'''
Created on Feb 1, 2014

@author: Otrebor45
'''

import game.components.Render as Render
import game.phys.physutil as Util
import Events
import pygame



class GameWon(Render.GUIComponent):
    def __init__(self, gameObject):
        Render.GUIComponent.__init__(self, gameObject)
        pygame.mixer.music.load("Resources/songs/Winning2.wav"  )
        pygame.mixer.music.play()
        
    def update(self,delta):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.gameObject.world.main.gotoMainMenu()
        
    def OnGUI(self, screen):
        background = pygame.image.load("Resources/congratulations.jpg")
        screen.fill( (255, 255, 255) )
        screen.blit(background, (0,0))

        font = pygame.font.SysFont("agency fb", 72)
        font.set_bold(True)
        titletext = font.render("Congratulations!", 1, (255,0,0))
        titletextpos = titletext.get_rect()
        titletextpos.centerx = screen.get_rect().centerx

        font.set_bold(False)
        starttext = font.render("Against all odds you have escaped!", 1, (255,0,0))
        starttextpos = starttext.get_rect()
        starttextpos.centerx = screen.get_rect().centerx
        starttextpos.centery = screen.get_rect().centery
        starttextpos.y = starttextpos.y + 200

        exittext = font.render("I applaud you with these balloons, Yay!!!", 1, (255,0,0))
        exittextpos = exittext.get_rect()
        exittextpos.centerx = screen.get_rect().centerx
        exittextpos.centery = screen.get_rect().centery
        exittextpos.y = exittextpos.y + 275

        screen.blit(titletext, titletextpos)
        screen.blit(starttext, starttextpos)
        screen.blit(exittext, exittextpos)
        
class GameOver(Render.GUIComponent):
    def __init__(self, gameObject):
        Render.GUIComponent.__init__(self, gameObject)
        self.time = 10
        self.message = 0
        pygame.mixer.music.load("Resources/songs/Ending.wav"  )
        pygame.mixer.music.play()
    def update(self, delta):
        self.time -= 1
        self.message += 1
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.time <= 0:
            self.gameObject.world.main.gotoMainMenu()
            
    def OnGUI(self, screen):
        background = pygame.image.load("Resources/gameover.jpg")
        screen.fill( (255, 255, 255) )
        screen.blit(background, (0,0))
        
        font = pygame.font.SysFont("agency fb", 72)
        font.set_bold(True)
        titletext = font.render("Game Over!", 1, (255,0,0))
        titletextpos = titletext.get_rect()
        titletextpos.centerx = screen.get_rect().centerx

        screen.blit(titletext, titletextpos)
        #screen.blit(text, textpos)
     

      
        
        
