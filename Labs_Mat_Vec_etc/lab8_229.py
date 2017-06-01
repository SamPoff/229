# -*- coding: utf-8 -*-

from vec import Vec
from mat import Mat
import math

def matId(D): return Mat( (D,D) , { (x,y) : 1 for x in D for y in D if x == y} ) 
print('matId')
print(matId({'a', 'b', 'c', 'd'}))
    
def matTransform(a,b,z): 
    M = matId({'a','b','c'})
    M['a','c'] = a
    M['b','c'] = b
    return M
v = Vec({'a','b','c'},{'a':1,'b':1, 'c':1})
print('matTransform')
print(matTransform(2,3,1) * v)
    
def matScale(i,j):
    M = matId({'a','b','c'})
    M['a','a'] = i
    M['b','b'] = j
    return M
print('matScale')
print(matScale(2,3))
    
def matReflect(k):
    M = matId({'a','b','c'})
    if   k == 'x':
        M['b','b'] = -1
    elif k == 'y':
        M['a','a'] = -1
    else:
        print('Invalid argument (must be "x" or "y")')
    return M
print('matReflect')
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
print('matRotate')
print(matRotate(0))
    
    
    
    
    