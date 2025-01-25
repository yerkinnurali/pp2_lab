#list
mylist=["apple","banana","cherry"]
print(mylist)
print(len(mylist))
print(type(mylist))
print(mylist[1])
print(mylist[-1])
print(mylist[1:2])
print(mylist[1:])
if "apple" in mylist:
    print("Apple in the list")
mylist[1]="mango"
print(mylist)
mylist[1:2]=["mango","orange"]
print(mylist)
mylist.insert(2,"watermelon")
print(mylist)
mylist.append("raspberry")
print(mylist)
newlist = ["kiwi","pineapple"]
mylist.extend(newlist)
print(mylist)
mylist.remove("pineapple")
print(mylist)
mylist.pop(6)
print(mylist)
del mylist[5]
print(mylist)
mylist.clear()
print(mylist)
#loop list
mylist = ["apple", "banana", "cherry"]
for i in mylist:
    print(i)
print()
for i in range(len(mylist)):
    print(mylist[i])
print()
i=0
while i<len(mylist):
    print(mylist[i])
    i=i+1
#loop comprehension
newlist=[]
for i in mylist:
    if 'a' in i:
        newlist.append(i)
print(newlist)
newlist.clear()
newlist=[i.upper() for i in mylist]
print(newlist)
#sortlist
mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
#listcopy
newlist=[]
newlist=mylist.copy()
print(newlist)
newlist= mylist[:]
print(newlist)
#joinlist
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)