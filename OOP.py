# The object oriented paradigm was introduced in the 1960s by Alan Kay. At the time, the paradigm was not the best computing solution given the small scalability of software developed then. As the complexity of software and real-life applications improved, object oriented principles became a better solution. 

# You previously encountered the four main pillars of object oriented programming. These are:  encapsulation, polymorphism, inheritance and abstraction. Let's look at a few examples that demonstrate how these principles translate when using Python.

# Encapsulation
# The idea of encapsulation is to have methods and variables within the bounds of a given unit. In the case of Python, this unit is called a class. And the members of a class become locally bound to that class.

class Alpha:

 def __init__(self):
    self._a = 2.  # Protected member ‘a’
    self.__b = 2.  # Private member ‘b’

# Polymorphism

# Polymorphism refers to something that can have many forms. In this case, a given object. Remember that everything in Python is inherently an object, so when I talk about polymorphism, it can be an operator, method or any object of some class. I can illustrate the case for polymorphism using built-in functions and operations, for example:  
# 
string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)  


# Inheritance
# Inheritance in Python will be covered later in the course, but the basic template for it is as follows:

# class Parent:
    # Members of the parent class

#  class Child(Parent):
    # Inherited members from parent class
    # Additional members of the child class

# Abstraction
# Abstraction can be seen both as a means for hiding important information as well as unnecessary information in a block of code. The core of abstraction in Python is the implementation of something called abstract classes and methods, which can be implemented by inheriting from something called the abc module. "abc" here stands for abstract base class. It is first imported and then used as a parent class for some class that becomes an abstract class. Its simplest implementation can be done as below.    

# from abc import ABC,   
# class ClassName(ABC):
#     pass