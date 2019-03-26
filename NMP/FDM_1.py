# for when things get crazy and I need the program to check itself and its inputs
paranoid = True

# finite differences method

# f(x) = .1x^5 - .2x^3 + .1x -.2
# at x = .1

# here, x_{i} = x, x_{i+1} = x + h, x_{i+2} = x + 2h, etc.


def f(y):
    return .1*y**5 - .2*y**3 + .1*y - .2


# h = .001
# x = .1


# forward finite difference method
# h must be really small for this to really be effective


def forward_fd_1(function, y, h):
    return (function(y + h) - function(y))/h


def forward_fd_2(function, y, h):
    return (function(y + 2*h) - 2*function(y + h) + function(y))/(h**2)


# central finite difference method


def central_fd_1(function, y, h):
    return (function(y+h) - function(y-h))/(2*h)


def central_fd_2(function, y, h):
    return (function(y+h) - 2*function(y) + function(y-h))/(h**2)


# backwards finite difference method


def backward_fd_1(function, y, h):
    return (function(y) - function(y - h))/h


def backward_fd_2(function, y, h):
    return (function(y) - 2*function(y - h) + function(y - 2*h))/(h**2)


# print(forward_fd_1(f, x, h))
# print(forward_fd_2(f, x, h))
# print(central_fd_1(f, x, h))
# print(central_fd_2(f, x, h))
# print(backward_fd_1(f, x, h))
# print(backward_fd_2(f, x, h))


# Now we apply above methods to a domain and then plot the values I guess
# We're gonna use the central differences method cause its better error rate lower.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 10000)

print(x)

for i in x:
    print(i)
    print(round(central_fd_1(f, i, .01), 6))
    print(round(central_fd_2(f, i, .01), 6))

plt.plot(x, f(x), '-k', x, central_fd_1(f, x, .01), '--b', x, central_fd_2(f, x, .01), '--r')
plt.xlabel('x')
plt.legend(['y', "y'", "y''"])
plt.grid()
plt.show()
