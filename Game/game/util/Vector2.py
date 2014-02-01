'''
Created on Jan 22, 2014

@author: otrebor
'''
import math


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%0.2f, %0.2f)"%(self.x, self.y)
    
    def __repr__(self):
        return self.__str__()
    
    def add(self, v2):
        return Vector2(self.x + v2.x, self.y + v2.y)
    
    def sub(self, v2):
        return Vector2(self.x - v2.x, self.y - v2.y)
    
    def scale(self, s):
        return Vector2(self.x * s, self.y * s)
    
    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def normalize(self):
        m = self.magnitude()
        if m == 0:
            return Vector2()
        return Vector2(self.x / m, self.y / m)
    
    def normal(self):
        return Vector2(self.y, -self.x)
    
    def distance(self, v2):
        return math.sqrt(math.pow((self.x - v2.x), 2) + math.pow((self.y - v2.y), 2))
    
    # distance square used on circle collision
    def distanceSq(self, v2):
        return math.pow((self.x - v2.x), 2) + math.pow((self.y - v2.y), 2)
    
    def dot(self, v2):
        return self.x * v2.x + self.y * v2.y
    
    def cross(self,v2):
        return Vector2(self.x*v2.y,self.y*v2.x)
    
    
    
    
