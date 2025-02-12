#1
def generate_square(n):
    for i in range(1,n+1):
        yield i*i
n=int(input("First:"))
generator=generate_square(n)
for i in generator:
    print(i)
#2
def even(n):
    for i in range(0,n+1,2):
        yield i

n=int(input("Second:"))
eve=even(n)
print((", ".join(str(i) for i in eve)))
#3
def gene3(n):
    for i in range(0,n+1,12):
         yield i
n=int(input("Third:"))
a=gene3(n)
for i in a:
    print(i)
 #4
def square(a,b):
    for i in range(a,b+1):
        yield i**2
a=int(input("Task 4.a: "))
b=int(input("b:"))
c=square(a,b)
for i in c:
    print(i)
 # 5
def denominator(n):
     for i in range(n,0,-1):
         yield i
n=int(input("Fifth:"))
d=denominator(n)
for i in d:
    print(i)