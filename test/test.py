#!/usr/bin/env python3
import numpy as np
from Transformation.point import Point2D
from Transformation.translation import Translation
from Transformation.rotation import Rotation
from Transformation.transformation import Transformation

np.set_printoptions(precision=4, suppress=True)

def run_tests():
    test1()
    test2()
    test3()


def test1():
    # Set up the points
    points = [Point2D(2, 4), Point2D(3, 6), Point2D(), Point2D(1, 2)]
    for p in points:
        assert(isinstance(p, Point2D))
    p3 =  points[1] + points[2]
    assert(isinstance(p3, Point2D))
        
def test2():
    # Set up the transformations
    t1 = Translation(1, 0)
    r1 = Rotation(np.pi/8)
    T1 = Transformation(r1, t1)
    assert(isinstance(t1,Translation))
    assert(isinstance(r1,Rotation))
    assert(isinstance(T1,Transformation))

def test3():
    # Do operations with points
    points = [Point2D(2, 4), Point2D(3, 6), Point2D(), Point2D(1, 2)]
    points.sort()
    for i in range(len(points)-1):
        assert(np.sqrt(points[i].x**2 + points[i].y**2) <= np.sqrt(points[i+1].x**2 + points[i+1].y**2))

