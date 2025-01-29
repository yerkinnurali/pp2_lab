def isprime(x):
    if x<=1:
        return False
    for i in range(2,x-1):
        if x%i==0:
            return False
    return True




def filter_prime(a):
    for i in a:
        if isprime(i):
            print(i)


a=[2,3,4,5,6,7,8,9,10]
print(filter_prime(a))
