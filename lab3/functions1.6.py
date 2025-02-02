from os.path import split

a=input()
b=split(a)
for x in range(len(b)-1,0,-1):
    print(b[x])