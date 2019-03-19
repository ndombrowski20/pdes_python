# Simple Iteration Method test doc 1

# Test Equation: 2x^2 - 5x + 3 = 0

# Alg1: x = (2x^2 + 3)/5
# Alg2: x = sqrt((5x-3)/2)

from math import sqrt

x = 0       # initial guess

for it0 in range(1000):
    xnew = (2*x**2 + 3)/5
    if abs(xnew-x) < .000001:       # this is taken to be the Degree of Accuracy
        break
    x = xnew

print('the first root: %.5f' % x)
print('the number of iterations: %d' % int(it0 + 1))

y = 2       # initial guess

for it1 in range(1000):
    ynew = sqrt((5*y-3)/2)
    if abs(ynew-y) < .00000001:       # this is taken to be the Degree of Accuracy
        break
    y = ynew

print('the first root: %.5f' % y)
print('the number of iterations: %d' % int(it1 + 1))

