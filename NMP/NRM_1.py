# first test using Newton-Raphson's Method

# same example as SIM 1 and 2

x = 0


def func(x):

    return 2*x**2 - 5*x + 3


def first_deriv(x):

    return 4*x -5


for iteration in range(100):
    xnew = x - func(x)/first_deriv(x)
    if abs(xnew - x) < .0000001:
        break

    x = xnew

print('the root : %.5f' % xnew)
print('iterations : %d' % int(iteration+1))


# x^2 + cos^2(x) - 4x = 0

from math import cos, sin

a = -10


def func_2(y):

    return y**2 + cos(y)**2 - 4*y


def first_deriv_2(y):

    return 2*y - 2*sin(y)*cos(y) - 4


for it2 in range(100):
    anew = a - func_2(a)/first_deriv_2(a)
    if abs(anew - a) < .0000001:
        break

    a = anew

print('the root : %.5f' % anew)
print('iterations : %d' % int(it2+1))