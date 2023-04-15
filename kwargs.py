#-------------------------------------------------------------
 # We can take n arguments in function

# Args Concept
def sum(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum(5,2,3,7))

# Kwargs Concept 
def sum2(**kwargs):
    sum = 0
    for k , v in kwargs.items():
        sum+=v
    return sum
print(sum2(coffee = 2.4 , cake = 1.9 ))    

# While Loop
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # It will move to the 4 & will not print 3 
    #break  # output 1 2 3 
  print(i)

# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))