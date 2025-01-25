mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict)
print(mydict["model"])
print(len(mydict))
print(type(mydict))
x=mydict.get("year")
print(x)
print(mydict.keys())
mydict["year"]=1969
print(mydict)
mydict["color"]="black"
print(mydict)
mydict.pop("color")
print(mydict)

for x in mydict:
    print(x,mydict[x])
#nested dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child1"]["year"])
print(myfamily)