# Transformation Package

This is a 2D Transformation package that allows the user to create a 2 dimensional point, manipulate the point in the 2D space, and plot the point using the matplotlib. It also contains matrices that are used to manipulate the point in 2D. 

The package contains the following classes:  
    - Point2D  
    - Translation  
    - Rotation  
    - Transformation  


## How to use

### Point2D

Point2D is a 3x1 ndarray from num that contains the coordinates of the created point object. the point object stores the inputs (x,y) in a 3x1 array in the following order: [x,y,1]  

to create a point, simply write the following:  
`p = Point2D({x}, {y})`

you can also use the object to plot a point using the following command:  
`p.plot()`

plot by default will produce a blue point. The user can change the color of the point by inputting a string argument of the color they wish to choose in the following way:  
`p.plot('g')`


### Translation

Translation is a 3x1 ndarray that stores a translation vector. This veco can be used to translate the Point2D object using the multiplication operator, and is used to construct the transformation matrix.  

To create a Translation object, write down the following line:  
`t1 - Tranformation({x},{y})`


### Rotation

Rotation is a 3x3 ndarray that requires an input of an angle in radiance. It contains the rotation information that can be used to rotate a point using the multiplication operator or to construct a transformation matrix as will be seen shortly.  
`
### Transformation
Transformation is a 3x3 matrix that stores the rotational information and the translational information of a given angel and vector. It can be used to transform a Poin2D object, which will result in a new coordinates after the transformation.

to create a Transformation object, see the following line:  
`T1 = Transformation({object=Rotation} , {object=Translation})`
`
## requirements  
The package requires the use of the following libraries:  
    - Numpy
    - Matplotlib

in case that you do not have the libraries, type in the terminal the following code:
`pip install -r requirements.txt`

## Run sample

To run a code sample of the package, please type the following in the terminal:  
`python3 Basic.py`

## test

To test the code, simply enter the following code in the terminal:  
`python3 -m test`

---
*Last Updated in May 2024*