# test doc for the bisection method

# FIRST VERSION OF THE CODE

# def function(y):
#     # define the function here
#     return 2*y**2 - 5*y + 3
#
#
# x1 = 1.2
# x2 = 5
#
# for it1 in range(100):
#     y1 = function(x1)
#     y2 = function(x2)
#
#     if y1 * y2 > 0:
#         raise Exception("root not in range")
#
#     xnew = (x1 + x2)/2
#     ynew = function(xnew)
#
#     if abs(y1) < .0000001:
#         break
#     elif y1*ynew < 0:
#         x2 = xnew
#     else:
#         x1 = xnew
#
# print("the root: %.5f" % x1)
# print("bisections: %d" % it1)

# USING FUNCTIONS AND RUN-TIME INPUT


def function(y):
    # define the function here
    return 2*y**2 - 5*y + 3


x1 = float(input('Enter the value of x1: '))
x2 = float(input('Enter the value of x2: '))

for it1 in range(100):
    y1 = function(x1)
    y2 = function(x2)

    if y1 * y2 > 0:
        raise Exception("# roots =/= 1")

    xnew = (x1 + x2)/2
    ynew = function(xnew)

    if abs(y1) < .0000001:
        break
    elif y1*ynew < 0:
        x2 = xnew
    else:
        x1 = xnew

print("the root: %.5f" % x1)
print("bisections: %d" % it1)


