class shape:
    class square:
        def __init__(self):
            self.length=0
        def get(self):
            self.length=int(input())
        def area(self):
            print("Area:",self.length*self.length)
s=shape()
sq=shape.square()
sq.get()
sq.area()
