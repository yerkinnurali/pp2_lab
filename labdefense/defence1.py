"""def a(b):
   sum=0
   for i in b:
     d=int(i)
     sum=sum+d
   return sum



b=input()
print(a(b))"""
class Car:
    def __init__(self,b,m):
        self.brand=b
        self.model=m
    def start(self):
        print("Car is starting")


class ElectricCar(Car):
    def start(self):
        print(f"{self.model} car is starting silently")
b=input("Brand:")
m=input("Model:")

print("Choose car type(n,e)")
t=input()
if t=="n":
    a=Car(b,m)
elif t=="e":
    a=ElectricCar(b,m)

a.start()

