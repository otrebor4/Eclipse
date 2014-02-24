'''
Created on Feb 6, 2014

@author: rfloresx
'''

import game.components.Component as Component
import game.bt.base as BT
import game.Game
import game.util.Vector2 as Vector2
import Events
import game.Debug as Debug
import Attacks


class BehaviorTree(Component.Component):
    def __init__(self,gameObject):
        Component.Component.__init__(self, gameObject)
        self.behavior = BT.BehaviorTree()
        self.data = {}
        self.behavior.data = self.data
        self.makeTree()
    
    def addAction(self,action):
        self.behavior.addAction(action)
        return self
        
    def makeTree(self):
        print "makeTree not implemented"
        raise
    
    def update(self, delta):
        self.behavior.update(delta)
    '''
    def OnCollision(self, collision):
        if collision.other.name == 'player':
            Events.OnDamage(self,10).CallOn(collision.other)
        if self.data.has_key('dest'):
            self.data.pop('dest')
        if self.data.has_key('target'):
            self.data.pop('target')
        
    def OnTrigger(self, collision):
        if self.data.has_key('dest'):
            self.data.pop('dest')
        if self.data.has_key('target'):
            self.data.pop('target')
        
        self.shape.position = self.shape.position.add( collision.normal.scale(collision.distance))
    '''

class Enemy1(BehaviorTree):
    def __init__(self, gameObject):
        BehaviorTree.__init__(self, gameObject)
        self.speed = 100
        self.agent = self.gameObject.getComponent("Navigator")
        self.timer = 0
        
    def update(self, delta):
        BehaviorTree.update(self, delta)
        self.timer -= delta
        
    def makeTree(self):
        self.addAction(BT.PrioritySelector()
                       .addAction(BT.Sequence()
                                  .addAction(self.findTarget)
                                  .addAction(self.findTargPosition)
                                  .addAction(BT.SwitchSelector(self.targetOnRange,self.attackTarget,self.followPath) ))
                       .addAction(BT.Sequence()
                                  .addAction(self.wonder)
                                  .addAction(self.followPath)))
    
    def targetOnRange(self):
        if self.data.has_key('targ'):
            dis = self.data['targ'].distance(self.gameObject.shape.Center())
            return dis < 150
            
        return False
    
    def wonder(self,delta):
        if not self.data.has_key('targ'):
            pos = self.gameObject.shape.Center()
            _pos = pos.add(Vector2.Vector2(game.Game.getNextRange(-200, 200)  , game.Game.getNextRange(-200,200) ))
            if not _pos:
                return BT.State.Failed
            if self.gameObject.world.terrain.validPosition(_pos.xy()):
                self.data['targ'] = _pos
            return BT.State.Failed
        
        return BT.State.Success
    
    def findTarget(self,delta):
        if self.data.has_key("target"):
            return BT.State.Success
        else:
            pos = self.gameObject.shape
            pos = pos.position.xy() if pos else None
            obj = None
            if pos:
                objs = self.gameObject.world.GetOnRange( pos, 250 )
                for ob in objs:
                    if ob.name == 'player':
                        obj = ob
            if obj:
                self.data['target'] = obj
                return BT.State.Success
                
            return BT.State.Failed
        
    def findTargPosition(self,delta):
        if self.data.has_key('target'):
            obj = self.data['target']
            self.data['targ'] = obj.shape.Center()
        if self.data.has_key('targ'):
            targ = self.data['targ']
            if not self.gameObject.world.terrain.validPosition(targ.xy()):
                self.data.pop('targ')
                return BT.State.Failed
            
            if self.data.has_key('path'):
                path = self.data['path']
                #check if current path is accurate
                if path.end.distance(targ) > 50:
                    self.data.pop('path')
                
            return BT.State.Success
        else:
            return BT.State.Failed
    
    def followPath(self,delta):
        if not self.agent:
            self.agent = self.gameObject.getComponent("Navigator")
            return BT.State.Failed
        pos = self.gameObject.shape.Center()
        path = None
        if not self.data.has_key('path'):
            _pos = self.gameObject.shape.Center().xy()
            if self.data.has_key('targ'):
                _pos = self.data['targ'].xy()
            self.agent.SetPath(_pos)
            path = self.agent.path
            if not path:
                if self.data.has_key('targ'):
                    self.data.pop('targ')
                return BT.State.Failed
            self.data['path'] = path
        else:
            path  = self.data['path']
        if path:
            waypoint = path.getWayPoint()
            if waypoint is None:
                self.data.pop('path')
                return BT.State.Failed
            
            Debug.drawLine(pos.xy(), waypoint.xy(), (0,255,0))
            #pygame = Game.pygame
            #Game.pygame.draw.line( pygame.display.get_surface(), (0,255,0), waypoint.xy(), pos.xy() )
            #print "waypoint"
            #pathstep = waypoint.sub(pos)
            #speed = self.speed*delta
            dist = pos.distance(waypoint)
            
            #print self.speed*delta*10
            radius = self.gameObject.shape.Radius()
            if dist <= radius:
                #self.data.pop('path')
                if not path.getNextWaypoint( radius ):
                    self.data.pop('path')
                    return BT.State.Success
            self.moveToPosition(waypoint, delta)
        else:
            if self.data.has_key('path'):
                self.data.pop('path')
            return BT.State.Failed 
        return BT.State.Running
        
    def checkDistance(self,delta):
        obj = self.data['target']
        self.data.pop('target')
        
        if obj:
            targ = obj.shape.Center()
            dist = targ.distance(self.gameObject.shape.Center())
            if dist < 75:
                return BT.State.Success
        return BT.State.Failed
    
    def attackTarget(self,delta):
        if self.data.has_key('target'):
            target = self.data['target'].shape.Center()
        if self.timer <= 0:
            self.gameObject.sendMessage('doAttackShot',{'target':target})
            self.timer = .5
        
    def moveToPosition(self, target, delta):
        tdir = target.sub( self.gameObject.shape.Center()  )
        #dist = tdir.magnitude()
        vel = tdir.normalize().scale(self.speed)
        #if dist < vel.magnitude():
        #    vel = tdir
        self.gameObject.riged.velocity = vel
    
    def OnDie(self,data):
        manager = self.gameObject.world.FindObject('manager')
        manager = manager.getComponent('WorldManager')
        dice = game.Game.getNextRange(0, 25)
        pos = self.gameObject.shape.Center().xy()
        if dice > 20:
            manager.spawnEnergy(*pos)
        if dice < 15:
            manager.spawnFuel(*pos)
        #manager.gainEnery( game.Game.random.randrange(0,5) )
        
    
class Enemy2(Enemy1):
    def __init__(self, gameObject):
        Enemy1.__init__(self, gameObject)
    
    def makeTree(self):
        self.addAction(BT.PrioritySelector()
                       .addAction(BT.Sequence()
                                  .addAction(self.findTarget)
                                  .addAction(self.findTargPosition)
                                  .addAction(BT.SwitchSelector(self.targetOnRange,self.attackTarget,self.followPath) ))
                       .addAction(BT.Sequence()
                                  .addAction(self.wonder)
                                  .addAction(self.followPath)))
    
    def targetOnRange(self):
        if self.data.has_key('targ'):
            dis = self.data['targ'].distance(self.gameObject.shape.Center())
            #print dis
            return dis < 50
            
        return False    
        
        
    def attackTarget(self,delta):
        target = self.gameObject.shape.Center()
        if self.data.has_key('target'):
            target = self.data['target'].shape.Center()
        if self.timer <= 0:
            self.gameObject.sendMessage('doAttackRange',{'target':target})
            self.timer = 1
     
      
class Enemy3(Enemy1):
    def __init__(self, gameObject):
        Enemy1.__init__(self, gameObject)
    
    def makeTree(self):
        self.addAction(BT.PrioritySelector()
                       .addAction(BT.Sequence()
                                  .addAction(self.findTarget)
                                  .addAction(self.findTargPosition)
                                  .addAction(BT.SwitchSelector(self.targetOnRange,self.attackTarget,
                                                               BT.SwitchSelector(self.targetLongRange,
                                                                                 self.attackTarget2,
                                                                                 self.followPath))))
                       .addAction(BT.Sequence()
                                  .addAction(self.wonder)
                                  .addAction(self.followPath)))
    def targetLongRange(self):
        if self.data.has_key('targ'):
            dis = self.data['targ'].distance(self.gameObject.shape.Center())
            return dis < 150
            
        return False 
    
    def targetOnRange(self):
        if self.data.has_key('targ'):
            dis = self.data['targ'].distance(self.gameObject.shape.Center())
            return dis < 50
            
        return False    
        
        
    def attackTarget(self,delta):
        target = self.gameObject.shape.Center()
        if self.data.has_key('target'):
            target = self.data['target'].shape.Center()
        if self.timer <= 0:
            self.gameObject.sendMessage('doAttackRange',{'target':target})
            self.timer = 1
        
    def attackTarget2(self,delta):
        if self.data.has_key('target'):
            target = self.data['target'].shape.Center()
        if self.timer <= 0:
            self.gameObject.sendMessage('doAttackShot',{'target':target})
            self.timer = .5  
            
    
class Attack(Component.Component):
    
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.meleDamage = 10
        self.rangeDamage = 10
        self.shotDamage = 10
        
    
    
    def doAttackMele(self,arg):
        pass
    
    def doAttackRange(self,arg):
        world = self.gameObject.world
        pos = self.gameObject.shape.Center()
        if arg.has_key('target'):
            target = arg['target']
            bdir = target.sub( pos).scale(.25)
            pos = pos.add(bdir)
        
        Attacks.createExplosion(self.gameObject, world, pos.x, pos.y, 40, damage = self.rangeDamage,  time= .25,
                                 ignores={'type':[self.gameObject.type]}, nockback = 0, file_name='Resources/sprites/explosion1.txt')
        
    
    def doAttackShot(self,arg):
        bdir = Vector2.Vector2(0,0)
        cpos = self.gameObject.shape.Center()
        cpos.y -=24
        if arg.has_key('target'):
            target = arg['target']
            bdir = target.sub( cpos ).normalize()
        elif self.gameObject.riged:
            bdir = self.gameObject.riged.velocity
        
        spos = cpos.add(bdir.scale(self.gameObject.shape.Radius()*4))
        bdir = bdir.scale(500)
        Attacks.createBullet(self.gameObject,self.gameObject.world, spos.x, spos.y, bdir.x, bdir.y, 5, damage = self.shotDamage, time = 2, ignores = {'type':[self.gameObject.type]},nockback=0, file_name='Resources/sprites/bullet.txt'   )
        
        
        