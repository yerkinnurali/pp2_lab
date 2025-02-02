class shape:
    class square:
        def __init__(self):
            self.length=0
        def get(self):
            self.length=int(input())
        def area(self):
            print("Area:",self.length*self.length)
    class rectangle:
        def __init__(self):
            self.a=0
            self.b=0
        def get(self):
            self.a=int(input("Width:"))
            self.b=int(input("Length:"))
        def area(self):
            print("Area:",self.a*self.b)
s=shape()
re=s.rectangle()
re.get()
re.area()