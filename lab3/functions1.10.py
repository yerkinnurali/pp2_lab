def a(list):
    b=sorted(list)
    c=[b[0]]
    for i in range(1,len(list)):
        if  b[i]!=b[i-1]:
            c.append(b[i])
    return c


print(a([1,2,4,0,0,7,5]))
print(a([1,0,2,4,0,5,7]))
print(a([1,7,2,0,4,5,0]))