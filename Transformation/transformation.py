import numpy as np
from Transformation.point import Point2D
from Transformation.translation import Translation
from Transformation.rotation import Rotation

class Transformation(Rotation, Translation):
    def __init__(self, Rotation=Rotation, Translation=Translation):
        self._R = Rotation
        self._T = Translation
        self._transformation = Rotation._rotation @ Translation._translation
        self.create()
    def create(self):
        temp = self._R._rotation @ self._T._translation
        self._translation = temp
    def __str__(self):
        return f"{self._transformation}"
    def __mul__(self, other):
        assert(isinstance(other,Point2D))
        temp = self._transformation @ other._point
        return Point2D(temp[0][0],temp[1][0])