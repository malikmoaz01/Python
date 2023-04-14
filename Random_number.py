# # Slicing of Strings 
# b = "Hello, World!"
# print(b[:6])
# b = "Hello, World!" # Get the characters from position 2 to position 5 
# print(b[2:5])
# b = "Hello, World!"
# print(b[-5:-2])

# # Console Input
# user_num_1 = input('First number is: ')
# user_num_2 = input('Second number is: ')
# user_sum = user_num_1 + user_num_2
# print(user_sum)

# # Modify The Strings 
# v = " Malik Moaz"
# print(v.upper())
# print(v.lower())
# print(v.strip()) # Remove Extra Spaces 
# print(v.replace("M" , "Z")) #Z will replaced on M where M will be Found 
# print(v.split(","))

# #Slicing the Strings 
# print(v[2:5]) #return characters from 2nd index to 5th Index 

# # Concatentate Stings 
# y = "Malik " 
# z = "Moaz "
# o = y+z 
# print(o)

# # Formate The Strings 
# name = "Malik Moaz"
# age = 19
# university = "PUCIT Lahore"
# language = "Python"
# x = "My name is {0} & I am {1} year old . I am currently doing software Enginering from {2} & I like {3}"
# print(x.format(name,age,university,language))

# # Escaping the Characters 
# t = "My name is \"Malik\" Moaz" #Single Quotes 
# t1 = "My name is Malik\n Moaz" #End Line
# t2 = "My name is Malik\t Moaz\t." #Tab Space 
# print(t)
# print(t1)
# print(t2)


# #  Conditional Statements 

# loyalty_customer = True
# total_bill = 124

# if loyalty_customer and total_bill > 100:
#     #give 20% discount
#     total_bill = total_bill - (float(total_bill)/ 100) * 20
# elif total_bill > 100:
#     #give 10% discount
#     total_bill = total_bill - (float(total_bill)/ 100) * 10
# else:
#     #sorry no discount, 5% service charge applied.
#     print('Sorry, nodiscount ...')

# print('Total Bill: ', float(total_bill))
 
# Switch Statements 

# http_request = 200

# match http_request :
#     case 250 | 201:
#         print("Success")
#     case 404:
#         print("Bad Request")
#     case 504 | 200:
#         print("Response Failed")
#     case _:
#         print("Unknown")            

# Loops Constructing 

# For Loop

# for i in range(10):
#     print("Looping",i)

alphabets = ["AB" , "CD" , "EF"]
# for i in alphabets:
#     print("The letters is" , i)



# While Loop

count = 0
while count < len(alphabets) :
    print('The Alphabets are ' , alphabets[count])
    count+=1

#  Usage of Break , Contniue & Pass 

# Break is used for stop the exececution

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break 
else:
    print('No sorry, not a dessert on my list')


# Continue can be used to control the iteration of the loop. 

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) 

# Pass statement allows you to run through the loop in its entirety and effectively ignore that the if condition has been satisfied.

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 
else:
    print('No sorry, not a dessert on my list')


