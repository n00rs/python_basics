# Python calculator

str_operator = input("Enter an operator (+,-,*,/): ")
dbl_num1 = float(input("Enter a number 1: "))
dbl_num2 = float(input("Enter a number 1: "))

if str_operator == "+":
    result = dbl_num1 + dbl_num2
elif str_operator == "-":
    result = dbl_num1 - dbl_num2
elif str_operator == "*":
    result = dbl_num1 * dbl_num2
elif str_operator == "/":
    result = dbl_num1 / dbl_num2
else:
    print("Invalid operator....!")
    
print(F"the result is {round(result,2)}")
 
#python weight converter
dbl_weight = float(input("Enter an Weight: "))
str_unit = input("Kilograms or Pounds? (K OR L) ")

if str_unit == "K":
    dbl_weight *= 2.205
    str_unit = "Kg."
    print(F"Your Weight is: {round(dbl_weight,1)} {str_unit}")
if str_unit == "L":
    dbl_weight /= 2.205
    str_unit = "Lbs"
    print(F"Your Weight is: {round(dbl_weight,1)} {str_unit}")    
else:
    print(F"{str_unit} is invlaid")
    
#temperatur converter
str_unit = input("Is this temperatur in Celsius or Fahrenheit (C/F) ?:")
dbl_temp = float(input("Enter the Temperature ")) 

if str_unit == "C":
    dbl_temp = round((9*dbl_temp)/5+32,1)
    print(f" Temperatur is {dbl_temp} Fahrenheit")
elif str_unit == "F":
    dbl_temp = round((dbl_temp - 32)* (5/9),1)
    print(f" Temperatur is {dbl_temp} Celsius")
else:
    print("Invaild Temperature unit")
    
