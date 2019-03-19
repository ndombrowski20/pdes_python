# Simple iterations method with a while loop same example as SIM_1.py

x = 10 # unlike last time this is the new arbitrary value because of how the abs is constructed
xnew = 0 # this is our "guess"
i = 0

while abs(xnew - x) >= .0000001:
    i += 1
    x = xnew
    xnew = (2*x**2 + 3)/5

print('the root: %f' % xnew)
print('iterations: %d' % i)