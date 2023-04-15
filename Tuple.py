
# Tuples are used to store multiple items in a single variable.

# Properties of Tuples 
# Ordered ------ When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable ------ Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates -------- Since tuples are indexed, they can have items with the same value:

# A tuple can contain different data types or can be of any data type:
# tuple1 = ("abc", 34, True, 40, "male")

tupleA = ("Onion" , "Patato" , "Carrot" )
print(tupleA[1:3]) # The search will start at index 1 (included) and end at index 2 (not included).


print(tupleA[-1]) 
# Negative Indexingmeans start from the end. -1 refers to the last item, -2 refers to the second last item etc.


if "Carrot" in tupleA:
        print("Yes , Carrot included in this tuppleA")

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called
 
# W e can add , update & remove item by converting into lists 
# we can delete the tuples by using del keyword 

y = list(tupleA)
y.remove("Carrot") 
y[1] = "Chilli"
tupleB = tuple(y)
print(tupleB)
del tupleB
# print(tupleB)  # this will raise an error because the tuple no longer exists


# Add items into The Tuple
z = ("Orange" , )
tupleA += z
print(tupleA)
        
# ----------------------------------------------------------------------------------------
# Unpacking a Tuple # When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

newTuple = ( "A" , "B" , "C")
(a , b , c) = newTuple
print(a)
print(b)
print(c)

# Important Note
# --------------------------------- The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list  ------------------------------------------------------------------------------------

newTupleB = ( "Z" , "Y" , "X" , "W")
(z , *y , x) = newTupleB
print(z)
print(y)
print(x)

# ------------------------------------------------------------------------------------

# Loop Constructing in Tuples
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# While Loop

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


# ------------------------------------------------------------------------------------
# Joining the Tuple

  fruits = ("apple", "banana", "cherry")
  number = ( 1 , 2 , 3)
mytuple = fruits * 2
z1 = fruits + number

print(mytuple)
print(z1)

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

x = (1, 2 , 2 , 2 , 3 , 4)
print(x.count(2))
print(x.index(3))