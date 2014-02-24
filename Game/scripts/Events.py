'''
Created on Feb 6, 2014

@author: rfloresx
'''

#OnDamage(damage)
class OnDamage:
    def __init__(self,source,amount):
        self.source = source
        self.amount = amount
    
    def CallOn(self,gameObject):
        gameObject.sendMessage("OnDamage",self)
        
class OnDie:
    def __init__(self,data={}):
        self.data = data
    def CallOn(self,gameObject):
        gameObject.sendMessage("OnDie",self.data)