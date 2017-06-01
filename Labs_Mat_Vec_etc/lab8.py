# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:02:22 2017

@author: Sam
"""

from vec import Vec
from mat import Mat
import math
from math import pi

"""
def matId(D): return Mat( (D,D) , { (x,y) : 1 for x in D for y in D if x == y} ) 
print('\nmatId')
print(matId({'x', 'y', 'z'}))
    
def matTransform(a,b,z): 
    M = matId({'a','b','c'})
    M['a','c'] = a/z
    M['b','c'] = b/z
    return M
v = Vec({'a','b','c'},{'a':2,'b':2, 'c':2})
print('\nmatTransform')
print(matTransform(3,5,2))
print(matTransform(3,5,2) * v)
    
def matScale(i,j):
    M = matId({'a','b','c'})
    M['a','a'] = i
    M['b','b'] = j
    return M
v = Vec({'a','b','c'},{'a':2,'b':2, 'c':2})
print('\nmatScale')
print(matScale(2,3))
print(matScale(2,3) * v)
    
def matReflect(k):
    M = matId({'a','b','c'})
    if   k == 'x':
        M['b','b'] = -1
    elif k == 'y':
        M['a','a'] = -1
    else:
        print('Invalid argument (must be "x" or "y")')
    return M
print('\nmatReflect')
print(matReflect('x'))
print(matReflect('y'))
print(matReflect('z'))
 
def matRotate(r):
    M = matId({'a','b','c'})
    M['a','a'] =  math.cos(r)
    M['a','b'] = -math.sin(r)
    M['b','a'] =  math.sin(r)
    M['b','b'] =  math.cos(r)
    return M
print('\nmatRotate')
print(matRotate(0))
"""
    
def matId(D): return Mat( (D,D) , { (x,y) : 1 for x in D for y in D if x == y} ) 
    
def matTransform(a,b): 
    M = matId({'x','y','z'})
    M['x','x'] = a
    M['y','y'] = 1
    M['x','z'] = 1
    M['y','z'] = b
    M['z','y'] = 1
    M['z','x'] = 1
    M['z','z'] = 1
    return M
u = Vec({'x','y','z'},{'x':2,'y':2, 'z':1})
print(matTransform(2,3) * u)


def matShift(a,b):
    M = matId({'x','y','z'})
    M['x','z'] = a
    M['y','z'] = b
    return M
u = Vec({'x','y','z'},{'x':2,'y':2, 'z':1})
print(matShift(2,3) * u)


def matRotate(a,b,r):
    M = matId({'x','y','z'})
    M *= matShift(a,b)
    M['x','x'] =  math.cos(r)
    M['x','y'] = -math.sin(r)
    M['y','x'] =  math.sin(r)
    M['y','y'] =  math.cos(r)
    M *= matShift(-a,-b)
    M *= 1.0
    return M
u = Vec({'x','y','z'},{'x':2,'y':2, 'z':1})
print(matRotate(3,3,pi/2) * u)





    
    
    
    