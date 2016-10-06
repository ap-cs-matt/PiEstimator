sides, sideLength, logB2 = 6* 2**int(len(bin((int(input("Enter Max Sides")) // 6)))-3), 1, lambda n:len(bin(n)) -3
for k in range(logB2(sides//6)):sideLength = ((1-((1 - (sideLength / 2)**2)**.5))**2 + (sideLength / 2)**2)**.5
print("Pi Approximation of Program Results\nNumber of Sides:\t",sides,"\nPI Approximation:\t",(sides * sideLength) / 2, "\nPython's Math.Pi:\t", 3.141592653589793)