'''from math import *
maxSides = eval(input("Enter Max Sides"))
sides = 6* 2**floor(log(maxSides // 6, 2))
iterations = floor(log(maxSides // 6, 2))

sideLength = 1
radius = 1

for k in range(0, iterations):
    apothem = sqrt(1 - (sideLength / 2)**2)
    sideLength = sqrt((1-apothem)**2 + (sideLength / 2)**2)
print((sides * sideLength) / 2)
#'''
from math import *
sides, sideLength = 6* 2**floor(log(eval(input("Enter Max Sides")) // 6, 2)), 1
for k in range(0, floor(log(sides / 6,2))):
    sideLength = sqrt((1-(sqrt(1 - (sideLength / 2)**2)))**2 + (sideLength / 2)**2)
print("Pi Approximation of Program Results\nNumber of Sides:\t",sides,"\nPI Approximation:\t",(sides * sideLength) / 2, "\nPython's Math.Pi:\t", pi)