import numpy as np
from Transformation.point import Point2D
from Transformation.translation import Translation
class Rotation(Translation):
    '''Class that defines a rotation matrix with a translation colum of values [0,0,1]'''
    def __init__(self, angle=np.pi/2):
        self._rotation = np.array([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])
        self.angle = angle

    def __str__(self):
        return f"{self._rotation}"
    
    def __add__(self, other):
        if isinstance(other, Rotation):
            return Rotation(self.angle + other.angle)
        else:
            print(TypeError("TypeError: Use supported class type(s) for *: 'Rotation'"))


    def __mul__(self, other):
        if isinstance(other, Point2D):
            temp = self._rotation @ other._point
            return Point2D(temp[0][0],temp[1][0])
        
        else:
            print(TypeError("TypeError: Use supported class type(s) for *: 'point2D'"))