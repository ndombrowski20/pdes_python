# Curve fitting

# linear regression

# once again, i have deviated from his guide. he wants me to use a for loop and i just wasnt feeling it
# so i made my own series of functions and used them to come to the code for this.


def mean(xlist):
    total = 0
    for i in range(len(xlist)):
        total += xlist[i]

    return total/len(xlist)


def intercept(xlist, ylist):
    first = 0
    second = 0
    for i in range(len(xlist)):
        first += xlist[i]**2
        second += xlist[i]*ylist[i]
    numerator = mean(ylist)*first - mean(xlist)*second
    denomenator = first - len(xlist)*mean(xlist)**2
    return round(numerator/denomenator, 3)

def slope(xlist, ylist):
    first = 0
    second = 0
    third = 0
    for i in range(len(xlist)):
        first += xlist[i]*ylist[i]
        second += ylist[i]
        third += xlist[i]**2

    numerator = first - mean(xlist)*second
    denomenator = third - len(xlist)*mean(xlist)**2

    return round(numerator/denomenator, 3)


def lin_reg_at_pt(x, xlist, ylist):
    b = intercept(xlist, ylist)
    m = slope(xlist, ylist)
    return round(m*x+b, 3)


def lin_reg(xlist, ylist):
    b = intercept(xlist, ylist)
    m = slope(xlist, ylist)
    print("the straight line equation:")
    print("y = (%.3f) + (%.3f)x" % (b, m))
    return round(m*x+b, 3)


# polynomial regression


def big_matrix(xlist):
    A = []
    for i in range(len(xlist)):
        ai = []
        for j in range(len(xlist)):
            if i == 0 and j == 0:
                ai.append(len(xlist))
            else:
                sum_all = 0
                for num in xlist:
                    sum_all += num**(i+j)
                ai.append(sum_all)
        A.append(ai)
    return A


def vectr(xlist, ylist):
    B = []
    for i in range(len(xlist)):
        sum_all = 0
        for j in range(len(ylist)):
            sum_all += ylist[j]*xlist[j]**i

        B.append(sum_all)

    return B


x = [0, 1, 2, 3, 4, 5]
y = [2, 8, 14, 28, 39, 62]


print(big_matrix(x))
print(vectr(x, y))
