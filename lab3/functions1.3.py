def fun(head,leg):
   rabbit = (leg-2*head)/2
   chicken = head - rabbit
   print("Rabbit:",rabbit)
   print("Chicken:",chicken)
head=int(input())
leg=int(input())
print(fun(head,leg))



