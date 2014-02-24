'''
Created on Feb 6, 2014

@author: rfloresx
'''
import game.components.Component as Component
import Events
import pygame
class Health(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.maxHealth = 100
        self.health = 100
        self.eh = pygame.mixer.Sound( "Resources/songs/EnemyHit.wav" )
        self.ek = pygame.mixer.Sound( "Resources/songs/Enemy_Kill.wav" )
        
    def update(self, delta):
        if self.health <= 0:
            self.ek.play()
            Events.OnDie({'cause':'health'}).CallOn(self.gameObject)
            #self.gameObject.Destroy()
    def Damage(self,damage):
        self.health -= damage
        
        
    def OnDamage(self,damage):
        self.eh.play()
        self.health-=damage.amount
        if self.health < 0:
            self.health = 0
        if self.health > self.maxHealth:
            self.health = self.maxHealth
class DestroyOnDie(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)

    def OnDie(self,data):
        self.gameObject.Destroy()
