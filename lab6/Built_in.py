import math
from time import sleep
print("Task 1")
a=[1,2,3,4,5,6]
print(math.prod(a))
print("Task 2")
def b(s):
    U=0
    L=0
    for i in s:
     if i.isupper():
       U=U+1
     if i.islower():
       L=L+1
    print(f"Upper:{U},Lower:{L}")
s=input("Input word:")
b(s)
print("Task 3")
def pal(d):
    check=d[::-1]
    if check==d:
            return "Palindrom"
    else:
        return "Not palindrom"
d=input()
print(pal(d))
print(("Task 4"))
num=int(input("Number:"))
milis=int(input("Milliseconds:"))
e=num**0.5
sleep(milis/1000)
print(f"Square root of {num} after {milis} miliseconds is {e}")
print("Task 5")
tu=(1,2,3,4,5,6)
print(all(tu))