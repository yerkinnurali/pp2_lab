import re
with open("rowtxt.txt","r") as file:
    data=file.readlines()

print("Task 1")
for row in data:
 a = re.findall("a.*b", row)
 print(a)
print("Task 2")
for row in data:
 a=re.findall("a.*b{2,3}",row)
 print(a)
print("Task 3")
for row in data:
    a=re.findall("[a-z]_[a-z]",row)
    print(a)
print("Task 4")
for row in data:
    a=re.findall("[A-Z][a-z]*",row)
    print(a)
print("Task 5")
for row in data:
    a=re.findall("a.*b$",row)
    print(a)
print("Task 6")
for row in data:
    a=re.sub(r"[ ,.]",":",row)
    print(a)
print("Task 7")

for row in data:
    a=re.sub(r"_[a-z]","A-Z",row)
    print(a)
