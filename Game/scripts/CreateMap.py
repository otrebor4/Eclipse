'''
Created on Feb 1, 2014

@author: Otrebor45
'''
import game.components.Component as Component
import game.components.Render as Render
import game.components.Sprite as Sprite
import game.phys.physutil as Util
import game.Game
import game.components.Navigator as Navigator
import Events
import EnemyBehaviors
import AnimationController
import pygame

import ObjectInfo
class WorldManager(Render.GUIComponent):    
    def __init__(self, gameObject):
        Render.GUIComponent.__init__(self, gameObject)
        self.dim = self.gameObject.world.main.RESOLUTION
        self.enemys = {'snake':self.snake,
                       'manbull':self.manbull,
                       'thing':self.thing,
                       'thing1':self.thing1}
        self.player = None
        self.currentSong = 'none'
        (fileName,image,sprite_data,anim) = Sprite.loadData('Resources/sprites/icons.txt',game.Game.Game.Instance().resources)
        self.icons = Sprite.Sprite(None)
        self.icons.setData(fileName, image, sprite_data,"")
        
        self.fuel= 0
        self.goalFuel = 50
        self.msg_timer = 0
        self.message = None# u'Hi\nhi\nhi\n'
    def Play(self, song):
        if self.currentSong != song:
            self.currentSong = song
            pygame.mixer.music.load( self.currentSong )
            pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        
    def update(self,delta):
        world = self.gameObject.world
        if world:
            pass
        if self.player is None:
            self.player = self.gameObject.world.FindObject('player')
        
        if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load( self.currentSong )
                pygame.mixer.music.play()
    
    def load(self,data):
        world = self.gameObject.world
        if self.dim is None:
            self.dim = self.gameObject.world.main.RESOLUTION
        amount = game.Game.random.randrange(3,15)
        if data.has_key('enemycount'):
            amount = int(data['enemycount'])
        if amount == 0:
            return
        for i in (0, amount):
            i = game.Game.random.randrange(0,len(self.enemys))
            (x,y) = self.randomPos( (10, self.dim[0]- 10), (10,self.dim[1]-10) )
            if world.terrain.validPosition( (x,y)):
                key = self.enemys.keys()[i]
                enemy = self.enemys[key](x,y)
                world.addGameObject(enemy)
                
                
    def randomPos(self, w_range, h_range ):
        i = 0
        x = game.Game.random.randrange(w_range[0],w_range[1])
        y = game.Game.random.randrange(h_range[0],h_range[1])
        while not self.gameObject.world.terrain.validPosition( (x,y)):
            x = game.Game.random.randrange(w_range[0],w_range[1])
            y = game.Game.random.randrange(h_range[0],h_range[1])
            i+=1
            if i > 10:
                return (x,y)
        
        return (x,y)
        
    def snake(self, x,y):
        resources = self.gameObject.world.main.resources
        
        obj = self.gameObject.world.createCircGameObject(x, y, 16)
        obj.addComponent(Navigator.Navigator)
        obj.addComponent(EnemyBehaviors.Enemy1)
        obj.addComponent(ObjectInfo.DestroyOnDie)
        Sprite.AddAnimator(obj, "Resources/sprites/monsterA.txt", resources, (-16,-32))
        obj.addComponent(AnimationController.AniationController)
        att = obj.addComponent(EnemyBehaviors.Attack)
        att.meleDamage = 15
        att.rangeDamage = 10
        att.shotDamage = 5
        
        health = obj.addComponent(ObjectInfo.Health)
        health.maxHealth = 50
        health.health = 50
        
        obj.name = "snake"
        obj.type = 'enemy'
        return obj
    
    def manbull(self, x,y):
        resources = self.gameObject.world.main.resources
        
        obj = self.gameObject.world.createCircGameObject(x, y, 20)
        obj.addComponent(Navigator.Navigator)
        obj.addComponent(EnemyBehaviors.Enemy2)
        obj.addComponent(ObjectInfo.DestroyOnDie)
        Sprite.AddAnimator(obj, "Resources/sprites/manbull.txt", resources, (-2,-32))
        obj.addComponent(AnimationController.AniationController)
        att = obj.addComponent(EnemyBehaviors.Attack)
        att.meleDamage = 15
        att.rangeDamage = 10
        att.shotDamage = 5
        
        health = obj.addComponent(ObjectInfo.Health)
        health.maxHealth = 50
        health.health = 50
        
        obj.name = "manbull"
        obj.type = 'enemy'
        return obj
    
    def thing(self,x,y):
        resources = self.gameObject.world.main.resources
        
        obj = self.gameObject.world.createCircGameObject(x, y, 20)
        obj.addComponent(Navigator.Navigator)
        obj.addComponent(EnemyBehaviors.Enemy3)
        obj.addComponent(ObjectInfo.DestroyOnDie)
        Sprite.AddAnimator(obj, "Resources/sprites/lizarda.txt", resources, (-2,-32))
        obj.addComponent(AnimationController.AniationController)
        att = obj.addComponent(EnemyBehaviors.Attack)
        att.meleDamage = 15
        att.rangeDamage = 10
        att.shotDamage = 5
        
        health = obj.addComponent(ObjectInfo.Health)
        health.maxHealth = 50
        health.health = 50
        
        obj.name = "lizard?"
        obj.type = 'enemy'
        return obj
    
    
    def thing1(self,x,y):
        resources = self.gameObject.world.main.resources
        
        obj = self.gameObject.world.createCircGameObject(x, y, 20)
        obj.addComponent(Navigator.Navigator)
        obj.addComponent(EnemyBehaviors.Enemy3)
        obj.addComponent(ObjectInfo.DestroyOnDie)
        Sprite.AddAnimator(obj, "Resources/sprites/wolfa.txt", resources, (-2,-32))
        obj.addComponent(AnimationController.AniationController)
        att = obj.addComponent(EnemyBehaviors.Attack)
        att.meleDamage = 15
        att.rangeDamage = 10
        att.shotDamage = 5
        
        health = obj.addComponent(ObjectInfo.Health)
        health.maxHealth = 50
        health.health = 50
        
        obj.name = "wolf?"
        obj.type = 'enemy'
        return obj
    
    def spawnEnergy(self,x,y):
        resources = self.gameObject.world.main.resources
        obj = self.gameObject.world.createRectGameObject(x,y, 40,40,False,True )
        Sprite.AddSprite(obj, "Resources/sprites/icons.txt", resources, (0,0), 'energy_yellow')
        dmg = obj.addComponent( EnergyItem )
        #dmg = EnergyItem()
        dmg.amount = game.Game.getNextRange(-25, 25)
        if dmg.amount < 0:
            sprt = obj.getComponent('Sprite')
            sprt.changeSprite('energy_red')
        dmg.timer = 5
        
    def spawnFuel(self,x,y):
        resources = self.gameObject.world.main.resources
        obj = self.gameObject.world.createRectGameObject(x,y, 40,40,False,True )
        Sprite.AddSprite(obj, "Resources/sprites/icons.txt", resources, (0,0), 'fuel')
        dmg = obj.addComponent( FuelItem )
        dmg.amount = game.Game.getNextRange(-1, 15)
        if dmg.amount <= 0:
            sprt = obj.getComponent('Sprite')
            sprt.changeSprite('water')
        dmg.timer = 5
        dmg.manager = self
        
    def OnGUI(self,screen):
        if self.player:
            x = 10
            y = 5
            health = self.player.getComponent("Health")
            if health:
                mx = float(health.maxHealth)
                cur = float(health.health)
                perc = float(cur/mx)
                h = 15
                w = 250*perc
                if perc < .4:
                    color = (255,0,0)
                    img = self.icons.getSprite('energy_red')
                elif perc < .7:
                    color = (255,255,0)
                    img = self.icons.getSprite('energy_yellow')
                else:
                    color = (0,255,0)
                    img = self.icons.getSprite('energy_green')
                    
                if img:
                    screen.blit( img, (x,y))
                y += 10
                rect = game.Game.pygame.Rect(x+30,y,int(w),h )
                game.Game.pygame.draw.rect( screen, color, rect)
                
            
            x = 10
            y += 50
            perc = (float(self.fuel)/float(self.goalFuel))
            w = 250*perc
            img = self.icons.getSprite('fuel')
            if img:
                screen.blit( img, (x,y))
                
            if perc < .4:
                color = (255,0,0)
                img = self.icons.getSprite('enery_red')
            elif perc < .99:
                color = (255,255,0)
                img = self.icons.getSprite('enery_yellow')
            elif perc == 1:
                color = (0,255,0)
                img = self.icons.getSprite('enery_green')
        
            y += 10
            rect = game.Game.pygame.Rect(x+30,y,int(w),h )
            if w != 0:
                game.Game.pygame.draw.rect( screen, color, rect)
        
               
        if self.message:
            self.msg_timer += game.Game.Game.Instance().Delta()
            
            if self.msg_timer > 5:
                self.message = None
                return
            font = pygame.font.SysFont("agency fb", 28)
            font.set_bold(False)
            text = font.render(self.message, 1, (255,255,255))
            textpos = text.get_rect()
            textpos.y = 650
            textpos.x = 10
            screen.blit(text, textpos)
            
            '''
            count = int( 15*(float(self.fuel)/float(self.goalFuel)))
            for i in range(0,count):
                img = self.icons.getSprite('fuel')
                if img:
                    screen.blit( img, (x,y))
                x += 60
                '''
    
    def OnPlayerDie(self,data):
        self.gameObject.world.main.goToGameOver()
        
    def goalCompleted(self):
        return self.fuel >= self.goalFuel
    
    def gainFuel(self,amount):
        #if self.fuel >= self.goalFuel and self.amount < 0:
        #    self.setMessage('I need more fuel')
        self.fuel += amount
        if self.fuel < 0:
            self.fuel = 0
        if self.fuel >= self.goalFuel:
            self.fuel = self.goalFuel
            self.setMessage('I have enough fuel!')
    def setMessage(self,smg):
        self.message = smg
        self.msg_timer = 0
    
class Sink(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.objs = {}
        self.damage = 0
        
    def update(self,delta):
        for key in self.objs.keys():
            if key.name != "player":
                key.shape.positino = self.objs[key]
            else:
                if Util.pointInsidePolygon(key.shape.Center().xy(), self.gameObject.shape.Points()):
                    key.shape.position = self.objs[key]['position']
                    
                    d = Events.OnDamage(self.gameObject, self.damage)
                    d.CallOn(key)
                
            self.objs.pop(key)
                       
    def OnTrigger(self, coll):
        if not coll.other in self.objs.keys():
            pos = coll.other.shape.position.add( coll.normal.scale( -(coll.distance+4)))
            self.objs[coll.other] = {"position":pos}
            
        
class Damage(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.damage = 0
    
    def OnTrigger(self, coll):
        Events.OnDamage(self.gameObject,self.damage).CallOn(coll.other)
        
        
class Goal(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
    
    def OnCollision(self,coll):
        if coll.other.name != 'player':
            return
        manager = self.gameObject.world.FindObject("manager")
        manager = manager.getComponent('WorldManager')
        if manager and manager.goalCompleted():
            self.gameObject.world.main.goToGameWon()
        elif manager:
            manager.setMessage("I need %i more fuel to leave" % ( manager.goalFuel-manager.fuel))
        
class FuelItem(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.amount = 0
        self.manager = 0
        
    def update(self,delta):
        self.timer -= delta
        if self.timer <= 0:
            self.Destroy()
    
    def OnTrigger(self, coll):
        if coll.other.name == 'player':
            self.gameObject.Destroy()
            if self.manager:
                self.manager.gainFuel( self.amount)
                
class EnergyItem(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.timer = 0
        self.amount = 0
        
        
    def update(self,delta):
        self.timer -= delta
        if self.timer <= 0:
            self.Destroy()
        
    def OnTrigger(self, coll):
        if coll.other.name == 'player':
            self.gameObject.Destroy()
            Events.OnDamage(self.gameObject, -self.amount).CallOn(coll.other)
