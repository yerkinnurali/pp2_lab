import math


class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"X:{self.x} Y:{self.y}")
    def move(self,nx,ny):
        self.x=nx
        self.y=ny
        print(f"Point is updated,now X={self.x} and Y={self.y}")
    def dist(self,sx,sy):
        print("Distance is:",math.sqrt((self.x-sx)**2+(self.y-sy)**2))


x=int(input("X point:"))
y=int(input("Y point:"))
a=point(x,y)

while True:
   op=input("Enter(q,move,show,dist):")

   if op=="q":
        break
   elif op=="move":
       nx=int(input("New X:"))
       ny=int(input("New Y:"))
       a.move(nx,ny)
   elif op=="show":
        a.show()
   elif op=="dist":
      sx=int(input("Second points X:"))
      sy=int(input("Second points Y:"))
      a.dist(sx,sy)
   else:print("Invalid command")
