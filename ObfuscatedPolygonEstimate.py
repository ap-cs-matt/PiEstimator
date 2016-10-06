s,l,g=6*2**(len(bin((int(input("Enter Max Sides"))//6)))-3),1,lambda n:len(bin(n))-3
for k in range(g(s//6)):l=((1-((1-(l/2)**2)**.5))**2+(l/2)**2)**.5
print("Pi Approximation of Program Results\nNumber of Sides:\t",s,"\nPI Approximation:\t",(s*l)/2,"\nPython's Math.Pi:\t",3.141592653589793)