import math
x = 14.26
y = -1.22
z = 3.5*math.pow(10, -2)

s = ((2*math.cos(x-2/3))/(0.5+math.pow(math.sin(y), 2)))*(1+(z**2/(3-(z**2/5))))
print('s = ', s)
