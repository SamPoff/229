# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:01:30 2017

@author: Sam
"""
print('1')
print((673%3 == 0) & (909%3 == 0))

print('\n2')
s0 = {pow(2, x) for x in {0, 1, 2, 3}}
print(s0)

print('\n3')
s1 = {x*y for x in {1, 2, 3} for y in {5, 6, 7}}
print(s1)

print('\n4')
l0 = ['A', 'B', 'C']
l1 = [1, 2, 3]
l2 = [[x, y] for x in l0 for y in l1]
print(l2)


print('\n5a')
s5 = {-4, -2, 1, 2, 5, 0}
s5_a = {(i, j, k) for i in s5 for j in s5 for k in s5 if (i + j + k == 0)}
print(s5_a)

print('\n5b')
s5_b = {(i, j, k) for i in s5 for j in s5 for k in s5 if (i + j + k == 0) 
        and (i, j, k) != (0, 0, 0)}
print(s5_b)