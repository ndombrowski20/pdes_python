# linear interpolation

# basic set up
time = [0, 20, 40, 60, 80, 100]
temp = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]


def lin_interp0(xp, x1, x2, y1, y2):
    return y1 + (y2-y1)/(x2-x1)*(xp-x1)


# a = lin_interp0(50, 40, 60, 61.6, 71.2)
#
# print(a)


# now with a new function

def lin_interp1(xp, x, y):
    for i, xi in enumerate(x):
        if xp < xi:
            return y[i-1] + (y[i]-y[i-1])/(x[i] - x[i-1])*(xp-x[i-1])
    raise Exception("not in data range")

# print(lin_interp1(50, time, temp))

# lagrange method and algorithm

# for the lists, we use the time and temp above


def lagrange_int(x, xlist, ylist):
    yp = 0

    for i in range(len(xlist)):
        product = 1
        for j in range(len(xlist)):
            if j != i:
                product = product * (x - xlist[j])/(xlist[i]-xlist[j])

        yp = yp + ylist[i]*product

    return round(yp, 1)


# print(lagrange_int(50, time, temp))

# newton's interpolation method

list1 = [0, 1.5, 2.8, 4.4, 6.1, 8.0]
list2 = [0, .9, 2.5, 6.6, 7.7, 8.0]


# they used numpy to do this, but i build my own function to calculate the divided difference

def div_differences(xlist, ylist):

    a = []
    nested_lists = []

    for i in range(len(xlist)):
        # print("i is " + str(i))
        yi = []
        # print(nested_lists)
        for j in range(i+1):
            # print("j is " + str(j))
            if j == 0:
                yi.append(ylist[i])
            else:
                num = (yi[j-1] - nested_lists[j-1][j-1])
                # print(num)
                den = (xlist[i]-xlist[j-1])
                # print(den)
                new = round(num/den, 5)
                yi.append(new)

        nested_lists.append(yi)
    # print(nested_lists)

    for i in range(len(nested_lists)):
        a.append(nested_lists[i][i])

    return a


def newt_int(x, a, xlist):
    y = a[0]
    for i in range(len(xlist)-1):
        product = 1
        for j in range(i+1):
            product *= (x-xlist[j])

        y += product*a[i+1]

    return round(y, 1)


lala = div_differences(list1, list2)

# print(newt_int(4.4, lala, list1))

