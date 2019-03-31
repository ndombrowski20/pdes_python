# numerical integration

from math import sin, pi
paranoid = True
fancy = False

# trapezoid rule


def f(y):
    return y*sin(y)


def trapezoidal_int0(f, upper, lower, n):
    h = abs(upper - lower) / n
    S = .5*(f(upper) + f(lower))
    for i in range(1, n):
        S += f(lower + i*h)
    return S*h


def trapezoidal_int1(f, xset):
    sum_num = 0
    for i in range(len(xset)):
        if i == 0:
            sum_num += .5*f(xset[i])
        elif i == len(xset):
            sum_num += .5 * f(xset[i])
        else:
            sum_num += f(xset[i])

    return len(xset)*sum_num


# print(trapezoidal_int0(f, pi/2, 0, 100))

# now we're starting with simpson's one third rule

def simpson_333_v0(f, upper, lower, n):
    if paranoid:
        if n % 2 != 0:
            raise Exception("i only work with an even number of partitions")

    h = abs(upper - lower) / n
    S = f(upper) + f(lower)

    for i in range(1, n):
        if i % 2 ==0:
            S += 2*f(lower + i*h)
        else:
            S += 4*f(lower + i*h)

    if fancy:
        return round(h/3*S, 6)
    return h/3*S


# simpson's 3/8 rule
# not as good as the 1/3 rule

def simpson_375_v0(f, upper, lower, n):
    if paranoid:
        if n % 3 != 0:
            raise Exception("needs to be divisible by three, homes")

    h = abs(upper - lower) / n

    S = f(upper) + f(lower)
    for i in range(1, n, 3):
        S += 3*(f(lower + i*h) + f(lower + (i+1)*h))
    for i in range(3, n, 3):
        S += 2*(f(lower + i*h))

    return S*h*3/8


# print(simpson_375_v0(f, pi/2, 0, 30))


# double integration

def double_f(a, b):
    return a**2*b + b**2*a


def double_int_333_v0(f, ax, bx, ay, by, nx, ny):
    if paranoid:
        if nx % 2 != 0:
            raise Exception("i only work with an even number of partitions")
        if ny % 2 != 0:
            raise Exception("i only work with an even number of partitions")

    hx = (bx - ax) / nx
    hy = (by - ay) / ny

    S = 0
    for i in range(ny+1):
        if i == 0 or i == ny:
            p = 1
        elif i % 2 != 0:
            p = 4
        else:
            p = 2

        for j in range(nx + 1):
            if j == 0 or j == ny:
                q = 1
            elif j % 2 != 0:
                q = 4
            else:
                q = 2

            S += p*q * f(ax + j*hx, ay + i*hy)

    if fancy:
        return round(S*hx*hy/9, 6)
    return S*hx*hy/9


print(double_int_333_v0(double_f, 1, 2, -1, 1, 10, 10))
