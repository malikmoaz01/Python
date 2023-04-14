list = ["apple", "banana", "cherry"]
# Add element into List
list.append("Kiwi")
print(list)
# Change Element with other 
list[1] = "Patato"
print(list)
# Delete Element from List
list.remove("apple")
print(list)
 
 # Use of Loop Contructor with List 
for x in list:
    print(x)
# tAKE lENGTH OF THE fOLLOWING LIST 
for x in range(len(list)):
    print(x)

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]    