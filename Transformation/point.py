import numpy as np
import matplotlib as plt
class Point2D:
    '''Creates a 2D point with (x,y) values as input'''
    def __init__(self, x=0, y=0):
        self._point = np.array([[x],[y],[1]])
        self.x = self._point[0,0]
        self.y = self._point[1,0]

    def __str__(self):
        return f"({self.x}, {self.y})"
        # return f'{self._point}'
    
    def __add__(self, other):
        assert(isinstance(other, Point2D))
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        assert(isinstance(other, Point2D))
        return Point2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self,other):
        assert(isinstance(other,(int,float)))
        temp = other._transformation @ self._point
        print(temp)
        return temp
    
    def __lt__(self, other):
        assert(isinstance(other,Point2D))
        return np.sqrt(self.x**2 + self.y**2) < np.sqrt(other.x**2 + other.y **2)
        
    def plot(self,clr='b'):
        plt.plot(self.x,self.y, clr+'.')