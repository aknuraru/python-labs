#Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#remove item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#loop items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)