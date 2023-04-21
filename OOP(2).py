
# The __init__() function is called automatically every time the class is being used to create a new object.

class Person:
    def __init__(self , name , age):
        self.name = name 
        self.age = age
p1 = Person("Malik Moaz" , 19)

print(p1.name)
print(p1.age)    


# The __str__() function controls what should be returned when the class object is represented as a string. If the __str__() function is not set, the string representation of the object is returned:

class Person:
    def __init__(self , name , age):
        self.name = name 
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    def myfunc(self):
        print("Hello my name is " + self.name)
print(p1.name)
print(p1.age) 
p = Person("Moaz" , 20)
p.myfunc()

# Delete The Object Property <> del p1.age 
# Delete the Object          <> del p1


# -----------------------<><><><><><><><><><><>--------------------------

# Inheritance


class Employee:
    def __init__(self , name , id , department , position ):
        self.name = name 
        self.id = id
        self.department = department
        self.position = position 

p = Employee("Malik Moaz" , 517 , "Software Engineering " , "Student")
print(p.name)
print(p.id)
print(p.department)


class Student(Employee):
    def __init__(self, name, id, department, position , aim):
        # Super will automatically INherted from Parent
        super().__init__(name, id, department, position)
        self.aim = aim
    def print(self):
        print(self.name , self.id , self.department , self.position , self.aim) 
        # Add Methods
    def welcome(self):
        print("Welcome",)   
x = Student("Malik Moaz\t" , 517, "\tSoftware Engineering\t" , "Student\t","MachineLearner" )
x.print()


# Multiple Inheritance 

class Teacher(Student):
    def __init__(self, name, id, department , position , aim , cnic):
        super().__init__(name, id, department, position, aim )
        self.cnic =  cnic
    def  print(self):
        return super().print() , print(self.cnic)

y = Teacher("Malik Moaz\t" , 517, "\tSoftware Engineering\t" , "Student\t","MachineLearner" , 35)
y.print()    