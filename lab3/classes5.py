
class Account:
    def __init__(self,name):
        self.person=name
        self.balanse=0
    def show(self):
        print(f"Balanse is:{self.balanse}")

    def deposit(self,money):
        if money>0:
            self.balanse=self.balanse+money
            print(f"Now balanse:{self.balanse}")
        else:
            print("invalid money")
    def withdraw(self,numb):
        if(numb>self.balanse) or numb<=0:
            print("Invalid")
        else:
            print(f"Withdrawed:{numb}")
            self.balanse=self.balanse-numb
            print(f"Balanse:{self.balanse}")








name=input("New persons name:")
a=Account(name)
while True:
    op = input("Enter(q,show,deposit,withdraw):")

    if op == "q":
        break
    elif op=="show":
        a.show()
    elif op=="deposit":
        money=int(input("Deposit:"))
        a.deposit(money)
    elif op=="withdraw":
        numb=int(input("Money to withdrawal:"))
        a.withdraw(numb)
    else:
        print("Invalid command")