# Variable = A Container for a value (string,integer,float,boolean)

# strings
first_name = "Jane"
food = "Burger"
email = "Janie@gmailcom" 
print(f"Name is {first_name}")
print(F"Food is {food}")
print(F"Mail id is {email}")

# integers
age = 29
quantity = 3
students = 35
print(F"You are {age}")
print(F"you are buying {quantity} items")
print(F"There are {students} in your class")

#Float

price = 10.99
gpa = 3.2
distance = 5.5
print(f"The Price is ${price}")
print(F"Ypur Gpa is {gpa}")
print(F"Ypu ran {distance}Km")

#Boolean True or False
is_student = True

if is_student:
    print(F"you are a student")
else:
    print("you are not a student")
    
for_sale = True
if for_sale:
    print("ITEM is for sale")
else:
    print("Item is not for sale")

is_online = True
if is_online:
    print("You are Online")
else:
    print("You are offline")
    
    
#TYPECASTING 
#           the process of converting a variable from one data type to another 
#            str(),int(),float(),bool()

name = "James"
age = 29
gpa = 5.6
is_student = True 

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

age = float(age)
age = str(age) #--> converting to string
# age +=1 
# thows exception TypeError: can only concatenate str (not "int") to str

'''
converting to boolean
only returns True or False
if an falsy value is passed then bool() funtion returns False an vice verca
'''
name = bool(name) # returns True

print(age,name)