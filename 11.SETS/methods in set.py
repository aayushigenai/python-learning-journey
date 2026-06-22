collection=set()
#adding an element
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("Aayushi")
collection.add("bhatt")

print(len(collection))
print(collection)

#removing an element
collection.remove(2)

#emptying whole set
#collection.clear()

#returns a any unique value
print(collection.pop())

print(collection)

#union of two sets

set1={1,2,3,4,5,6}
set2={4,5,6,7,8}
print(set1.union(set2))

#intersection returns common values

print(set1.intersection(set2))