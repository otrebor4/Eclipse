'''
Created on Jan 22, 2014

@author: otrebor
'''
'''
physical object template
'''

import game.base.Component as Component
from shapes import Rectangle
import shapes


# collider depends on shape to determine its position,size,dimensions
#
class Collider(Component.Component):
    def __init__(self, gameObject):
        Component.Component.__init__(self, gameObject)
        self.gameObject.shape = None
        self.static = False
        
    def draw(self,screen):
        if self.gameObject and self.gameObject.shape:
            self.gameObject.shape.draw(screen)
    
class CircleCollider(Collider):
    def __init__(self, gameObject, x=0, y=0, radius=0):
        Collider.__init__(self, gameObject)
        self.gameObject.shape = shapes.Circle.Circle(x, y, radius)
        
class RectCollider(Collider):
    def __init__(self, gameObject, x=0, y=0, w=0, h=0):
        Collider.__init__(self, gameObject)
        self.gameObject.shape = shapes.Rectangle.Rectangle(x, y, w, h)
        
class PolygonCollider(Collider):
    def __init__(self, gameObject, x=0, y=0, points=[]):
        Collider.__init__(self, gameObject)
        self.gameObject.shape = shapes.Polygon.Polygon(x, y, points)
        
