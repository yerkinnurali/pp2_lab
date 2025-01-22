#boolean
print(10 > 9)
print(10 == 9)
print(10 < 9)
#message
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#Evaluate two variables
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#Check if an object is an integer or not:
x = 200

print(isinstance(x, int))