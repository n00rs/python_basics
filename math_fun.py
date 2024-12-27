friends = 10
''' augmented assignment operator'''
# friends = friends +1
# friends+=1 

# friends = friends - 1
# friends -=1 # augmented assignment operator

# friends = friends * 3
# friends *= 3

# friends = friends / 2
# friends /= 2

# friends = friends ** 2
# friends **= 2

# print(friends)
'''Modulous operater'''
remainder = friends % 3
print(remainder)

x = 3.14
y = -2
z = 6
#round function which rounds to nearest integer
result = round(x) 
# absolute function return the distance to zero as a whole number
result = abs(y)
# pow function return the power of fist val to the sec val
result = pow(2,8)
# max function return the maximum value of given numbers
result = max(x,y,z)

# min function return the minimum value of given numbers
result = min(x,y,z)


print(result)

import math

print(f"pi value is {math.pi}")
print(F"the electron charge val is : {math.e}")

int_num1 = 9
# sqrt function returns the square root of that number
result =math.sqrt(int_num1)
print(result)


'''ceil and floor functions'''
int_num2 = 3.1
result = math.ceil(int_num2)
print(result)
result = math.floor(int_num2)
print(result)

# # circumference and area of circle
radius = float(input(" Enter radius of circle "))
circumference = 2 * math.pi * radius
print(F"the circumference is {round(circumference,2)}")

area = math.pi * pow(radius,2)

print(F"area of the circle is: {round(area,2)}")

# Hypotenous of triangle square root of a^2 + b^2
a = float(input("Enter the side A: "))
b = float(input("Enter the side B: "))
c = math.sqrt(pow(a,2)+pow(b,2))

print(f" the Hypotenous is {a}")