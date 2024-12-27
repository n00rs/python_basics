'''
if = Do some code only IF some conditions is True
Else do something else 
'''

age = int(input("Enter Your Age: "))

if age>= 80:
    print("You're too old to sign up")
elif age >= 18:
    print("Your are signed up")
elif age<=0:
    print("You haven't born yet")
else:
    print("You must be 18+ to sign up")
    
chr_res = input("Would you like to have food ? (Y/N) ")

if chr_res == 'Y':
    print("Have some food")

elif chr_res == "N":
    print("Okay , thank you !")
else:
    print("Invalid input")    

str_name = input("Please Enter Your Name: ")

if str_name == "":
    print("You didn't enter your name...!")
else:
    print(F"Your name is {str_name}")
    
bln_sale = True

if bln_sale:
    print("This Item is for sale")
else:
    print("This Item is not for sale")
    
bln_online = False

if bln_online:
    print("The user is online")
else:
    print("The user is offline")
