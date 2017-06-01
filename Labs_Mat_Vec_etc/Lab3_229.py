# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:48:46 2017

@author: Sam
"""

print('P1')
s = [1,2,3,4]
def cubes(arg): return [x**3 for x in s if x % 2 == 0]
print(cubes(s))


print('\nP2')
dct     = {0:'A', 1:'B', 2:'C'}
keylist = [1,2,0]
def dict2list(dct, keylist): return [dct[i] for i in keylist]
print(dict2list(dct,keylist))


print('\nP3')
L       = ['A','B','C']
keylist = [0,1,2]
def list2dict(L,keylist): return {x:y for (x,y) in zip(keylist,L)}
print(list2dict(L,keylist))