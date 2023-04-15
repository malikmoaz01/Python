
#Function with zero Parameter

a = 7 
b = 8
def calculate_fuel_cost():
    return a*b
print(calculate_fuel_cost())

# Function with Parameters

def sum(c,d):
    return a + b / 100

print(sum(7,9))

# Scoping In Python

# Local Scope 

def get_total(a, b):
    #local variable declared inside a function
    total = a + b
    return total
print(get_total(5, 2))


# Accessing variable outside of the function:
# print(total)
# NameError: name 'total' is not defined

# -------------------------------------------------
# Enclosing Scope refers to a function inside another function or what is commonly called a nested function. 

def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()
    #double variable will not be accessible
    # print(double)

    return total

# -----------------------------------------

# Global scope is when a variable is declared outside of a function. This means it can be accessed from anywhere. 


special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total