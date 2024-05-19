import numpy as np
from Transformation.point import Point2D
class Translation:
    '''Translation class'''
    def __init__(self, x=0, y=0):
        self._translation = np.array([[1,0,x],[0,1,y],[0,0,1]])
        self.x = self._translation[0,2]
        self.y = self._translation[1,2]
        
    def __str__(self):
        return f"{self._translation}"
    def __add__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, Translation):
            return Translation(self.x + other.x, self.y + other.y)
        else:
            TypeError("TypeError: Use supported class type(s) for +: 'Translation' and 'point2D'")
    
    
    def __sub__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x - other.x, self.y - other.y)
        elif isinstance(other, Translation):
            return Translation(self.x - other.x, self.y - other.y)
        else:
            print(TypeError("TypeError: Use supported class type(s) for -: 'Translation' and 'point2D'"))
    def __mul__(self, other):
        if isinstance(other, (int, float) ):
            return other * self._translation
        elif isinstance(other, Point2D):
            temp = self._translation @ other._point
            return Point2D(temp[0][0],temp[1][0])
        else:
            print(TypeError("TypeError: Use supported class type(s) for *: 'int', 'float'"))

    def __truediv__(self, other):
        if isinstance(other, (int, float) ):
            return self._translation * (1/other)
        else:
            print(TypeError("TypeError: Use supported class type(s) for /: 'int', 'float'"))
