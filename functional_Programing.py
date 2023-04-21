
# Pure Vs impure Functions 

# A pure function is a function that will return the same values given the same arguments. A function is not pure if there is something outside the function that can change its return, given the same arguments.Here is An Example :

def pure(num1,num2):
    x = ((num1+num2) / num1)
    return x

print(pure(2,16))


# An impure function is ‘influenced’ by forces outside the function. With an impure function, given the same arguments, there is no guarantee that it will return the same output. The function below is not pure. This is because it is using a variable outside the function (global variable) — num3. If that variable changes, then given the same arguments, the return will also change. So, the function is not pure because it has side effects.

num3 = [1 , 3 ,5 , 7, 9]
def listfunc(item):
    n1 = num3.copy()
    n1.append(item)
    return n1 
new_list = listfunc(2)
print(num3)
print(new_list)

# Reverse A String)

str = "Hello"
print(str[::-1]) # Traverse From Right to Left
# Function Of reversing the String
def reverse(s):
    if(len(s) == 0):
        return s
    else:
        return s[1:] + s[0]
    
print(reverse("Hi"))
# --------------------------------------------------------

# Map → Executes a function on each element of an array. Every element of the array is passed to the callback function and returns a new array with the same length.
# it returns none if condition doesnot satisfied otherwise return item on satisfied Condition

menu = ["Apple" , "Mango" , "Appricot" , "Banana"]
def find(item):
    if item[0] == 'A':
        return item
    
new_menu = map(find,menu)
print(new_menu)

for x in new_menu:
    print(x)

# filter → Remove items which don't satisfy a condition.

new_menu = filter(find,menu)
print(new_menu)

for x in new_menu:
    print(x)