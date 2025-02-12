import math

from math import radians
#1
degree=int(input("Input degree:"))
print("Output radian:",radians(degree))
#2
height=int(input("Height:"))
first=int(input("Base, first value:"))
second=int(input("Base, second value:"))
print("Area:",(first+second)*height/2)
#3
side=int(input("Input number of sides:"))
length=int(input("Input the length of a side:"))
print("Area:",((side)*(length)**2)/(4*math.tan(math.pi/side)))
#4
base=int(input("Length of base:"))
h=int(input("Height of parallelogram:"))
print("Area:",base*h)