# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:53:31 2017

@author: Sam
"""
import math

# Exam has tf, mc, and calculations.

def twice(x): 
    return [x*2]
    # return {x*2}
    # return x*2
    
print(twice(5))

L = [1,2,3]

def nextInt(L):
    return [x+1 for x in L]

print(nextInt(L))

def quadratic(a,b,c):
    disc = math.sqrt(b*b-4*a*c)
    return set(((-b+disc)/2*a, (-b-disc)/2*a))
    
print(quadratic(1,-4,4))