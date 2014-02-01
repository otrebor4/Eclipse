'''
Created on Jan 28, 2014

@author: otrebor
'''
import Shape
import game.util.Vector2 as Vector2

'''
points are not world points is a set of vectors using x,y as reference point, to simplify movement
'''
class Polygon(Shape.Shape):
    
    def __init__(self, x,y, points):
        #points are vectors from the reference point (x,y)
        Shape.Shape.__init__(self,x,y)
        self.corners = [ Vector2.Vector2( pt.x, pt.y) for pt in points ]
        self.aabb = (min([pt.x for pt in self.corners]),
                     min([pt.y for pt in self.corners]),
                     max([pt.x for pt in self.corners]),
                     max([pt.y for pt in self.corners]))
    
    def getEdges(self):
        #get all edges on polygon
        #edges are correct world position
        edges = []
        for i in range(0, len(self.corners)):
            edges.append( (self.corners[i-1].add(self.position),self.corners[i].add(self.position) ) )
        return edges
    
    def getPoints(self):
        points = []
        for i in range(0, len(self.corners)):
            points.append( self.corners[i].add(self.position))
        
        return points
    