# Sets are used to store multiple items in a single variable.

# Properties of Sets 
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.

# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicate Values will be ignored & it doesnt allowed in Sets 

# Additem into Set 
setA = { " A " , " B " , "C"}
setB = {"Z"  , "Y"}
setA.add("D")
setA.update(setB)
print(setA)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

setC = [" P " , " Q "]
setA.update(setC)
print(setA)

setA.remove('D')  # Remove Element & we cant remove list dictionary element from the set 
setA.discard("Z") # Remove ELement but it has one advantage it will not return an error if the element doesnt exist in the set 
setA.pop()   # It will remove an element unknown 
# setA.clear() # It will clear all the Set 
# del setA     # it will delete the Set 
print(setA)

# Loop Constructing in Sets 

for x in setA:
    print(x)


# ---------------------------------------------------------------------


# Joining Sets
 
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

# The union() method returns a new set with all items from both sets:

setU = {"A" , "B"}
setU1 = {1, 2 , "A" }
print(setU.union(setU1))

# The update() method inserts the items in set2 into set1:
setU.update(setU1)
print(setU)

# The intersection_update()  & intersction method will keep only the items that are present in both sets.
# The values True and 1 are considered the same value in sets, and are treated as duplicates:

print(setU.intersection(setU1))
setU.intersection_update(setU1)
print(setU)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
print(x.symmetric_difference(y))


# Sets Method


# add()	                Adds an element to the set
# clear()	            Removes all the elements from the set
# copy()	            Returns a copy of the set
# difference()	        Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	            Remove the specified item
# intersection()    	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	        Returns whether two sets have a intersection or not
# issubset()	        Returns whether another set contains this set or not
# issuperset()	        Returns whether this set contains another set or not
# pop()             	Removes an element from the set
# remove()	            Removes the specified element
# symmetric_difference()	        Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	    inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others