myset = {"apple", "banana", "cherry"}
print(myset)
print(type(myset))
for x in myset:
  print(x)
print("banana" in myset)
myset.add("orange")
print(myset)
tropical = {"pineapple", "mango", "papaya"}
myset.update(tropical)
print(myset)
myset.remove("pineapple")
myset.discard("mango")
print(myset)
for i in myset:
    print(i)
#union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set3 = set1 | set2
print(set3)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
set3 = set1.difference(set2)

print(set3)
set3 = set1.symmetric_difference(set2)

print(set3)