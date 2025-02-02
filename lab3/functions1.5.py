from itertools import permutations


def b(a):
    p = permutations(a)
    for i in p:
        print(i)

a=input()
print(b(a))