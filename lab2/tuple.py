tuple=("apple", "banana", "cherry")
print(tuple)
print(type(tuple))
x=list(tuple)
x[1]="melon"
x.append("orange")
tuple=list(x)
print(tuple)
(a,b,c,d)=tuple
print(a)
print(b)
print(c)
print(d)
print()
for i in tuple:
    print(i)