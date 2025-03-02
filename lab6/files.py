import os
from os import write
from os.path import isdir, join, isfile
print("Task 1")
def directory(path):
    r=[]
    for i in os.listdir(path):
        if isdir(join(path,i)):
            r.append(i)
    return r
def files(path):
       r=[]
       for i in os.listdir(path):
        if isfile(join(path,i)):
            r.append(i)
       return r
path=input("Enter path:")
print("Directories:",directory(path))
print("Files:",files(path))
print()



print("Task 2")
print("Exist",os.path.exists(path))
print("Readable:",os.access(path,os.R_OK))
print("Writeable:",os.access(path,os.W_OK))
print("Executability:",os.access(path,os.X_OK))


print("Task 3")
path=input("Path:")
if os.path.exists(path):
    print(f"Path {path} exists")
    print("Directory:",os.path.dirname(path))
    print("Filename:",os.path.basename(path))
else:print(f"Path {path} does not exicts")
print("Task 4")
file=open(path)
s=file.readlines()
print("Line numbers:",len(s))
file.close()
print("Task 5")
path=input("Enter path to text file:")
list=["Apple","Banana","Cherry"]
file=open(path,"w")
for i in list:
 file.write(i+'\n')
print("Task 6")
path=input("Enter directory:")
for i in range(65,91):
 n=f"{chr(i)}.txt"
 pat=os.path.join(path,n)
 f=open(pat,"w")
 f.write(f"This is file {chr(i)}")
 f.close()
print("Task 7")
path=input("Enter file to copy:")
new=input("Enter new file path")
f=open(path,"r")
n=f.read()
f.close()
c=open(new,"w")
c.write(n)
c.close()
print("Task 8")

 
