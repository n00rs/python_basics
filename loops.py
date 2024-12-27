'''
WHILE LOOP = execute some code WHILE some condition remains True
'''

# str_name = ""

while str_name =="":
    str_name = input("Enter Your name: ")

print(f"Hi, {str_name}")

int_age = int(input("Enter Your age"))

while int_age <=0:
    print("INVALID_AGE")
    int_age = int(input("Enter Your age"))

print(f"You are {int_age} old")

str_food = input("Enter a food you like (press q to quit): ")

while str_food != "q":
    print(f"you like {str_food}")
    str_food = input("Enter another food you like (press q to quit) : ")

print("Bye")

int_num = int(input("Enter a number between 0 to 10 : "))

while int_num < 1 or int_num > 10:
    print(f"{int_num} is not valid")
    int_num = int(input("Enter a number between 0 to 10 : "))

# print(f"Entered number is {int_num}")

'''
python compound interest calculator
'''
dbl_princple = 0
int_time = 0
dbl_intrest_rate = 0

while dbl_princple <=0:
    dbl_princple = float(input("Enter the princple amount : "))
    if dbl_princple <= 0:
        print("Princple can't be zero ")
        
while dbl_intrest_rate <=0:
    dbl_intrest_rate = float(input("Enter the interest rate : "))
    if dbl_intrest_rate <= 0:
        print("interest rate can't be zero ")
        
while int_time <=0:
    int_time = int(input("Enter the duration of deposit : "))
    if int_time <= 0:
        print("duration of deposit can't be zero ")
        
print(dbl_intrest_rate)
print(dbl_intrest_rate)
print(int_time)

dbl_compound_amount = dbl_princple * pow(1+(dbl_intrest_rate/100),int_time)

print(f"Balance after {int_time} years is {dbl_compound_amount}")