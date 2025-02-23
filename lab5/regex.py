import re
with open("rowtxt.txt","r") as file:
    data=file.readlines()

print("Task 1")
for row in data:
 a = re.findall("a.*b", row)
 print(a)
print("Task 2")
for row in data:
 a=re.findall("ab{2,3}",row)
 print(a)
print("Task 3")
for row in data:
    a=re.findall("[a-z]+_[a-z]+",row)
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
    a=re.sub(r"_([a-z])",lambda a:a.group(1).upper(),row)
    print(a)
print("Task 8")
for row in data:
    a=re.sub(r"([A-Z])",r"@\1",row)
    b=re.split("@",a)
    print(b)
print("Task 9")
for row in data:
    a=re.sub(r"([A-Z])",r" \1",row)
    print(a)
print("Task 10")
for row in data:
    a=re.sub(r"([A-Z])",r"_\1",row)
    b=re.sub(r"_([A-Z])",lambda c:"_"+c.group(1).lower(),a)
    print(b)

