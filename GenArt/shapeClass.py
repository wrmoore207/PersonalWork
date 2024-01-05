# Ryan Moore
# Shape Class w. Constructors

# Develop methods to draw using turtle or other graphic option. 
# Build as a tool to build other things, bigger, more complex images

from turtle import *
from random import *

class Shape():

    def __init__(self):
        self.shape = 'shape'

class Polygon(Shape):

    def __init__(self):
        self.shape = 'polygon'
        self.numSides = None
        self.sideLength = None

    def computePerimeter(self):
        return sum(self.sideLength)

    def edgeNumber(self):
        return len(self.sideLength)

class Square(Polygon):
        
        def __init__(self):
            self.shape = 'square'
            self.numSides = 4
            self.sideLength = 3
        
        
    
    

# create a shape Class
# 
# create subClass circle
# 
# create subClass square
# 
# create subClass triangle  
