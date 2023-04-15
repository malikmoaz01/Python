
# Dictionaries are used to store data values in key:value pairs.

# Properties of Dictionaries 

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

dict = {
    "name"       : "Malik Moaz" , 
    "university" : "Pucit"  ,
    "Roll_No "   : "BSEF21M517"  , 
    "name"       : "Moaz Malik" # We cant rename the same key in this  it will exist the latest one 
}

print(dict)
print(dict["university"]) # We can Access value by the Key 
print(dict["name"])


# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:


dict2 = {
    "name"       : "Malik Moaz" , 
    "university" : "Pucit"  ,
    "Roll_No "   : "BSEF21M517"  , 
    "name"       : "Moaz Malik" , # We cant rename the same key in this  it will exist the latest one 
    "colors"     : ["red", "white", "blue"]
}


print(dict2.keys())      # Access the Keys 
print("\n")
print(dict2.values())    # Access the Values 
print("\n")
print(dict2.get("name")) # We can Access by Get Method 
print("\n")


# Add New Item into the Dictionary 
dict2["department"] = "Software Engineering"
print(dict2)
print("\n")


# Values can be  Update by this way
dict2["name"] = "Malik Moaz"
print(dict2)
print("\n")

# If Condition 
if "name" in dict2:
  print("Yes, 'name' is one of the keys in the thisdict dictionary\n")

# Update Dictionary 

dict.update({"year": 2020})
print(dict)


# Same Syntax for Removing & Deleting the Dictionary
# The pop() method removes the item with the specified key name:
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# The del keyword removes the item with the specified key name:
# The del keyword can also delete the dictionary completely:
# The clear() method empties the dictionary:


# Loop Constructing in Dictionary
# for x in dict2.values():
# for x in dict2():
for x in dict2.keys():
  print(x)


# Copy the Dictionary 

print("\n")
dict3 = dict2.copy()
print(dict3)
print("\n")



# Nested The dictionary 

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

print(myfamily["child1"])



# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary