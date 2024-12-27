'''
INPUT Function (input())
A Funtion that Prompts the user to Enter data 
and Returns the Entered Data as a string
'''
name = input("What's Your Name?: ")
age = int(input("How Old are You?: "))
age = age +1

print(F"name is {name}")
print(F"You are {age} old")
print("Happy B'day")


# Find the area of Rectangle 

length = float(input("Enter the Length: "))
width = float(input("Enter the width: "))

print(F"area is {length*width} cm")

#shopping cart program
item = input("what would you like to buy?: ")
price = float(input("What is the price ?: "))
quantity = int(input("How many Would you like ?:"))

total = price * quantity

print (total)
print(f"you have bought {quantity} * {item}/s")
print(F"Your Total is: ${total}")

'''
Madlibs game 
word game where you create a story 
by filling in blanks with random words
'''
str_adjective = "Enter an adjective (description): "
adjective1 = input(str_adjective)
adjective2 = input(str_adjective)
adjective3 = input(str_adjective)
noun1 = input("Enter a noun (person,place,thing): ")
verb1 = input("Enter a verb ending with 'ing'")


print(F"Today I went to a {adjective1} zoo")
print(F"In an Exhibit, I saw an {noun1}")
print(F"{noun1} was {adjective2} and {verb1}")
print(F"I was {adjective3}")