import math
x = 0.1722
y = 6.33
z = 3.25*10**-4

s = 5*math.atan(x)-(1/4)*math.acos(x)*((x+3*abs(x-y)+x**2)/(abs(x-y)*z+x**2))
print('s = ', s)