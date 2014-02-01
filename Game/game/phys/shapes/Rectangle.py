'''
Created on Jan 28, 2014

@author: otrebor
'''
import Polygon
import game.util.Vector2 as Vector2


'''
Rectangle position is the left top corner
'''
class Rectangle(Polygon.Polygon):
    def __init__(self, x=0, y=0, w=0, h=0):
        points = [Vector2.Vector2(0,0),
                  Vector2.Vector2(w,0),
                  Vector2.Vector2(w,h),
                  Vector2.Vector2(0,h)]
        Polygon.Polygon.__init__(self, x, y, points)