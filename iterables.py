'''
Iterables = An object/collection that can return its element one at a time 
            allowing it to be iterated over in a loop
'''

list_numbers =  [1,2,3,4,5,6,7]

for int_num in list_numbers:
    print(int_num,end=" - ")
    
tuple_numbers = (1,2,3,4,5,6,7)

for int_num in tuple_numbers:
    print(int_num)
    
# sets
set_numbers = {1,2,3,4,5,6,7}
# can't be reversed
for int_num in set_numbers:
    print(int_num)
    
# strings
str_name = "Brocode"

for str in str_name:
    print(str)
    
# Dictionary 
dict_num = {"A://":1,"B":2,"C":3}
# by default keys
for key in dict_num:
    print(key)
    
# to values use 
for value in dict_num.values():
    print(value)

# to get both key and value
for key,value in dict_num.items():
    print(key,value)
    
'''
memebership operator (in , not in)
        checks whether a value exists in seq
        list,string,tuple,set,dictionary
'''    
str_word = "apple"

str_letter = input("Guess a letter in the secret word ")

if str_letter in str_word:
    print(f"there is a {str_letter} in {str_word}")
else:
    print(F"{str_letter} not found")


if str_letter not in str_word:
    print(F"{str_letter} not found")    
else:
    print(f"there is a {str_letter} in {str_word}")
 

# sets
set_students = {"sam","sali","james"}

str_student = input("Enter a student name ?:")

if str_student in set_students:
    print(f"{str_student} is in the class")
else:
    print(F"{str_student} is not in the class")

# dictionary
dict_grades = { "sandy":"A","Sam":"C","sali":"B","spongebob":"D" }

str_student = input("Enter the name of student ?: ")

if str_student in dict_grades:
    print(f"{str_student} grade is {dict_grades.get(str_student)}")
else:
    print(f"{str_student}'s grade is not availabe")

str_email = "noobie@gmail.com"

if "@" in str_email and "." in str_email:
    print("Valid email")
else:
    print("invalid email")


'''
List comprehension = A concise way to create lists in python
                     Compact and easier to read than traditional loops 
                     [expression for val in iterable if condition]
'''
list_numbers = []

for i in range(1,11) :
    list_numbers.append(i*2)
print(list_numbers)

# another way using list comprehension
list_numbers = [i*2 for i in range(1,11)]
print(list_numbers)

list_triples = [i * 3 for i in range(1,11)]
print(list_triples)

list_fruits = ["apple","orange","mango","pineapple"]
# upper case
list_fruits = [fruit.upper() for fruit in list_fruits]
# first char
list_chars = [fruit[0] for fruit in list_fruits]
print(list_fruits,list_chars)

list_numbers = [1,2,3,4,5,-7,-8,-11]

list_post_num = [int_num for int_num in list_numbers if int_num >= 0]
list_neg_num = [int_num for int_num in list_numbers if int_num <0]
list_odd_num = [int_num for int_num in list_numbers if int_num %2==1]
list_even_num = [int_num for int_num in list_numbers if int_num %2==0]
print(f"{list_numbers} : {list_post_num} : {list_neg_num} : {list_odd_num} : {list_even_num}")

list_grades = [25,35,95,66,44,22,88,77]

list_pass_grades = [int_grade for int_grade in list_grades if int_grade > 60]
print(list_pass_grades)




























