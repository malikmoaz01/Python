# Lists are used to store multiple items in a single variable.


list = ["apple", "banana", "cherry"]
# Add element into List
list.append("Kiwi")
list.insert(len(list),"Pomegranute")
list.insert(2,"add 2nd") # Add on 3rd index 
list.extend(["A" , "B" , "C "]) # Add one or more Elements in List
print(list)


# Change Element with other 
list[1] = "Patato"
print(list)


# Delete Element from List
list.remove("apple")
list.clear() # Delete All List 
# list.pop("A")
print(list)
 

 # Use of Loop Contructor with List 
for x in list:
    print(x)


# tAKE lENGTH OF THE fOLLOWING LIST 
for x in range(len(list)):
    print(x)



# We want to Comprehension Some list in another list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "e" in x:
    newlist.append(x)

print(newlist)

# ---------------------------------------------------------------------

# Sorting the List

# Ascending the List

listA = ["D" , "A" , "B" , "C"]
listA.sort()
print(listA)

# Descending the List

listA = ["D" , "A" , "B" , "C"]
listA.sort(reverse=True)
print(listA)

# Reverse The List
listA = [ 100 , 320 , 450 , 650]
listA.reverse()
print(listA)

# If we want to print a list in case Sensitive Order 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# ----------------------------------------------------------------------------------

# Copy The List

listZ = ["Z" , "Y" , "X"]
copylist = listZ.copy()
print(copylist)

# ----------------------------------------------------------------------------------

# Joining the Lists 

l1 = ["A" , "B" , "C"]
l2 = [1 , 2 , 3 ]
l3 = l1 + l2
print(l3)

# 2nd Way is appending all the items from list2 into list1, one by one:

l1 = ["A" , "B" , "C"]
l2 = [1 , 2 , 3 ]
for x in l2:
    l1.append(x)
    print(l1)


# 3rd way Use the extend() method to add list2 at the end of list1:  

l1 = ["A" , "B" , "C"]
l2 = [1 , 2 , 3 ]
l1.extend(l2)

print(l1)



# Lists Method 

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list