# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:17:19 2017

@author: Sam
"""

L = ['x', 'y', 'z']
S = range(1,4)
one = list(zip(S,L))

two = {2*k + 1:(2*k+1)*(2*k+1) for k in range(5,10)}
       
names = ['Bob', 'Bill', '', 'Mary']
idSal = {0:1000, 3:900, 1:1200}
three = {names[i]:idSal[i] for i in idSal.keys()}
         
print('\none: '+ str(one))
print('\ntwo: '+ str(two))
print('\nthree: '+ str(three))
         
