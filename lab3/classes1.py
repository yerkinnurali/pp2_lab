class str:
    def __init__(self):
        self.s=""
    def get(self):
        self.s=input()
    def print(self):
        print(self.s.upper())
a=str()
a.get()
a.print()