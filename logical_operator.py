'''
Logical operators = evaluate multiple conditions (or,and,not)
                or = atleast one condition must be true
                and = both conditions must be true
                not = inverts the condition    
'''

dbl_temp = 25
is_raining = True

if dbl_temp > 35 or dbl_temp < 0 or is_raining:
    print("the outdoor event is cancelled  ...")
else :
    print("The Event is On")
    
    
dbl_temp = 20
bln_sunny = False

if dbl_temp >=28 and bln_sunny:
    print("It's Hot Outside")
elif dbl_temp <=0 and bln_sunny:
    print("it's cool outside && it's an sunny day")
elif 28 >= dbl_temp > 0 and bln_sunny:
    print("'it's warm outside")
elif dbl_temp >=28 and not bln_sunny:
    print("It's Hot & CLOUDY Outside")
elif dbl_temp <=0 and not bln_sunny:
    print("it's cool outside && it's an  CLOUDY day")
elif 28 >= dbl_temp > 0 and not bln_sunny:
    print("'it's warm & CLOUDY outside")    
    
    
'''
conditional expressions = A online shortcut for id else stament (ternanry operator)
choose one or the other value on a condition X if condition else Y
'''
dbl_num1 = 1
print("postive" if dbl_num1 > 0 else "Negative")

print("ODD" if dbl_num1 %2 !=0 else "EVEN")

a = 6
b = 7
int_max = a if a>b else b
int_min = a if a<b else b
print(int_max,int_min)

int_age = 25 

str_status = "Adult" if int_age > 18 else "minor"
print(str_status)

user_role = "admin"

print("Full Access" if user_role =="admin" else "Limited Acess")