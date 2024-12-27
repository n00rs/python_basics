'''
Functions : A Block of reusable code 
            calling :place () after function str_name to invoke it
'''

def happy_bday(str_name,int_age):
    print(F"Happy b'day {str_name}")
    print(F"You are {int_age} years old")
    print(F"Happy b'day {str_name}")
    print()
    
happy_bday("Jane",20)

def display_invoice (str_name,dbl_amount,str_due_date):
    print(f"Hello {str_name} ")
    print(f"Your bill of {dbl_amount:.2f} is due on {str_due_date}")
    
display_invoice("jon doe",9999,'01/01/1990')


'''
return : statement is used to end a function and send a value to caller

ex: to add 2 number
'''
def add(int_num1:int,int_num2:int):
    return int_num1 + int_num2
def subtract(int_num1:int,int_num2:int):
    return int_num1 - int_num2
def multiply(int_num1:int,int_num2:int):
    return int_num1 * int_num2
def divide(int_num1:int,int_num2:int):
    return int_num1 / int_num2

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_fullname(str_first_name:str,str_second_name:str):
    return str_first_name.capitalize() + " " + str_second_name.capitalize()

print(create_fullname("jon","doe"))

'''
Default arguments : A default value for certain parameter 
                    default is used when that argument is omitted 
                    makes function more flexible reduces # of argments
'''
def net_price(dbl_price,dbl_discount=0,dbl_tax=0.05):
    return dbl_price * (1-dbl_discount) *(1+dbl_tax)

# print(net_price(500,0,0.05))
print(net_price(500))


'''
Count up 
'''
import time
'''
default arguments should be after positional argumnets
 not this def counter(int_start=0,int_end):
'''
def counter(int_end:int,int_start=0):
    for i in range(int_start,int_end+1):
        print(i)
        time.sleep(1)
    print("Done ...!")
# counter(3)

'''
Keyword argument : an argument preceded by an identifier
                    helps with readablity order doesn't matter
'''
def hello(str_greet:str,str_title:str,str_first_name:str,str_last_name:str):
    print(str_greet+str_title+str_first_name+str_last_name)

hello(str_greet="Hello world",str_last_name="Doe",str_title="Mr",str_first_name="jon")

print("Hello",end=" ") # here end is an keyword argument

def get_phone(int_country_code,int_area_code,int_first_digit,int_last_digit):
    return f"{int_country_code}-{int_area_code}-{int_first_digit}-{int_last_digit}"
str_phn_num = get_phone(int_last_digit=7895,int_area_code=548,int_country_code=1,int_first_digit=456)
print(str_phn_num)


'''
*args : allows to pass multiple non-key arguments -> tuple
**kwargs : allow to pass multiple keyword-argument
* unpacking operator
'''
print("arbitary===================")
def add(*args):
    print(args)
    total = 0
    for i in args:
        total += i
    return total    
    # return a+b

print(add(1,2))

def dislay_name(*names):
    print(']]]]]]]]',names)
    for name in names:
        print(name)
        
dislay_name("john","bond")


# **KWARGS

def address(**kwargs):
    print(kwargs)
    for key,val in kwargs.items():
        print(f"{key} : {val}")
    
address(str_streer="Baker st",str_city="East",str_state = "Manchester",str_country="U.K")

#using both together
def shipping_address(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    
    print(f"{kwargs.get('str_street')}")
    print(f"{kwargs.get('str_city')},{kwargs.get('str_city')},{kwargs.get('str_zip_code') or ''}")
    print(f"{kwargs.get('str_country')}")

# first positional arguments
shipping_address("Mr.","john","bond",str_street="Baker st",str_city="East",str_state = "Manchester",str_country="U.K",str_zip_code="98745")
 

















