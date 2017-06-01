import numpy as np
from math import pi
from math import sin












"""
Problem One Jacobi


# Initialize an array of zeros for X
x = np.zeros([80,1]) 
b = []
for i in range(81):
    b.append(pi)
counter = 0

A = np.zeros((80,80))
for i in range(1,81):
    for j in range(1,81):
        if j == i:
            A[i-1,j-1] = 2*i
        elif j == i + 2 and i in range(1,79) or j == i - 2 and i in range(3,81):
            A[i-1,j-1] = 0.5*i
        elif j == i + 4 and i in range(1,77) or j == i - 4 and i in range(5,81):
            A[i-1,j-1] = 0.25*i
        else:
            A[i-1,j-1] = 0.0

# Fill b
for i in range(1,81):
    b[i] = pi

tol = 1e-5

for k in range(300):
    # Copy old 'x' for x(k-1)
    counter += 1
    x_old = x.copy() 
    for i in range(1, 81):
        s = 0.0
        for j in range(1, 81):
            if j != i:
                s = s + (A[i-1,j-1] * x_old[j-1])
        
        x[i-1] = (b[i-1] - s) / A[i-1,i-1]

    delta = np.linalg.norm((x - x_old),np.inf)/ np.linalg.norm((x),np.inf);

    if(delta < tol):
        break

print('\nJacobi\n')
print(counter, ' Iterations\n')
print('L2 Norm ', np.linalg.norm(x,2), '\n')
for i in range(10):
    print('x[', i, '] = ', x[i])
"""




    
    
    
    
"""
Problem One GS


# Initialize an array of zeros for X
x = np.zeros([80,1]) 
b = []
for i in range(81):
    b.append(pi)
counter = 0

A = np.zeros((80,80))
for i in range(1,81):
    for j in range(1,81):
        if j == i:
            A[i-1,j-1] = 2*i
        elif j == i + 2 and i in range(1,79) or j == i - 2 and i in range(3,81):
            A[i-1,j-1] = 0.5*i
        elif j == i + 4 and i in range(1,77) or j == i - 4 and i in range(5,81):
            A[i-1,j-1] = 0.25*i
        else:
            A[i-1,j-1] = 0.0

# Fill b
for i in range(1,81):
    b[i] = pi

L = 1
LOld = 2
x_old = x+1

for k in range(300): 
    # Copy old 'x' for x(k-1)
    counter += 1
    x_old = x.copy() 
    for i in range(1, 81):
        s = 0.0
        for j in range(1, 81):
            if j != i:
                s = s + (A[i-1,j-1] * x[j-1])
        
        x[i-1] = (b[i-1] - s) / A[i-1,i-1]

    delta = np.linalg.norm((x - x_old),np.inf)/ np.linalg.norm((x),np.inf);

    if(delta < tol):
        break

print('\nGauss Seidel\n')
print(counter, ' Iterations\n')
print('L2 Norm ', np.linalg.norm(x,2), '\n')
for i in range(10):
    print('x[', i, '] = ', x[i])
"""




    















"""
Problem Two Gaussian Elimination
"""

A = np.array([[5,  5,  0,  0,  0, 5.5], 
              [0,  0,  1, -1, -1, 0  ],
              [0,  0,  0,  2, -3, 0  ],
              [1, -1, -1,  0,  0, 0  ],
              [0,  5, -7, -2,  0, 0 ]])

numrows = 5
numcols = 6

for col in range(numcols - 1):
    
    # Pivoting
    maxRow = np.argmax(abs(A[col:numrows, col]))
    temp = A[maxRow + col].copy()
    A[maxRow + col] = A[col]
    A[col] = temp
    
    # Gaussian Elimination
    for row in range(col + 1, numrows):
        # print(A, '\n')
        A[row] = A[row] - (A[row, col]/A[col, col]) * A[col]
 
# Make solution array
x = np.array([0.0,0.0,0.0,0.0,0.0])
        
# Backsub
for i in range(numrows - 1, -1, -1):
    hold = 0.0
    for j in range(i + 1, numrows): 
        hold = hold + A[i,j] * x[j]
    x[i] = (A[i, numcols - 1] - hold) / A[i, i]
    
print('\nProblem Two Part A Solution Vector\n')
for z in range(5):
    print('\nX[',z,'] =', x[z])
    
    
    
    
    

# Jacobi
print('\nJacobi\n')

A = np.array([[5,  5,  0,  0,  0],
              [0,  5, -7, -2,  0],
              [1, -1, -1,  0,  0],
              [0,  0,  1, -1, -1],
              [0,  0,  0,  2, -3],])
    
A = A * 1.0

# Fill b
b = [5.5, 0.0, 0.0, 0.0, 0.0]
counter = 0
x = np.array([0.0,0.0,0.0,0.0,0.0])

tol = 1e-5

for k in range(4):
    # Copy old 'x' for x(k-1)
    counter += 1
    x_old = x.copy() 
    for i in range(5):
        s = 0.0
        for j in range(5):
            if j != i:
                s = s + (A[i,j] * x_old[j])
        
            x[i] = (b[i] - s) / A[i,i]
            print(A[i,i])


    delta = np.linalg.norm((x - x_old),np.inf)/ np.linalg.norm((x),np.inf);

    if(delta < tol):
        break

print('Solution Vector\n')
for i in range(5):
    print(x[i])












"""
Problem Three


def f(x):
    return cos(x) - x
    
def df(x):
    return -sin(x) - 1

def newtonsFavWay(p, max, tol):
    pn = 0
    for i in range(max):
        if df(p) == 0:
            print('Divide by zero')
        else:
            pn = p - ( f(p) / df(p) )
            if abs(pn - p) < tol:
                return pn
            else:
                print(i, abs(pn - p))
                p = pn



"""











    
    
    
    