str_name = input("PLEASE ENTER YOUR NAME: ")

# to find the length of given string
print(len(str_name))
#to find index of the first occurence use find
print(str_name.find("n")) 
#to find index of the first occurence use find
print(str_name.rfind("n")) 
# to captialize 
print(str_name.capitalize())
# to convert to UPPER case 
print(str_name.upper())
# to convert to lower case
print(str_name.lower())
# to check whether the string is digit 
print(str_name.isdigit())
# to count how many characters are there in string 
print(str_name.count("s"))
# to replace a character with other 
print(str_name.replace("n","N"))
# to see all string methods 
# print(help(str)) 

'''
Validate user input excerise 
        username is no more than 12 chars
        username must not contains space 
        username must not contain digits
'''

if len(str_name)>12:
    print('username must not be more that 12')
elif str_name.find(" ") != -1:
    print("username contain's sapces")
elif not str_name.isalpha():
    print("USER_NAME_CONTINS_DIGIT")
else :
    print(F"welcome {str_name}")
    
'''
indexing = accessing elements of sequence using [] (indexing operator)
            [start: end: step]
'''
str_card_num = "1234-7894-5214-7894"

print(str_card_num[0:20:2])
# to get last use -1
print(str_card_num[-1])
#get last 4 digit of credit card number 
print(str_card_num[-4:])
# to reverse the string using -1 in step
print(str_card_num[::-1])

'''
format specifiers {value:flag} format a value based on what flags are passed
.(number)f = round to that many decimals
:(number) = allocate that many spaces 
:03 = alocate and zero pad that many spaces 
:< = left justify
:> = right justify
:^ = center align
:+ = use a plus sign to indicate postive value
:= = place sign to leftmost positive value
: = insert space before +ve numbers
:, = comma sepreator

'''
dbl_price1 = 314159
dbl_price2 = -16554152
dbl_price3 = 123401

print(f"Price 1 is {dbl_price1:.2f}") # rounding to 2 floating number
print(f"Price 2 is {dbl_price2:.2f}")
print(f"Price 3 is {dbl_price3:.2f}")

#total spaces will be 10
print(f"Price 1 is {dbl_price1:10}") 
print(f"Price 2 is {dbl_price2:10}")
print(f"Price 3 is {dbl_price3:10}")

#total spaces will be 10 and blank space will be 0
print(f"Price 1 is {dbl_price1:010}") 
print(f"Price 2 is {dbl_price2:010}")
print(f"Price 3 is {dbl_price3:010}")

#to align left use <
print(f"Price 1 is {dbl_price1:<10}") 
print(f"Price 2 is {dbl_price2:<10}")
print(f"Price 3 is {dbl_price3:<10}")

#to align right use >
print(f"Price 1 is {dbl_price1:>10}") 
print(f"Price 2 is {dbl_price2:>10}")
print(f"Price 3 is {dbl_price3:>10}")

#to align center use ^
print(f"Price 1 is {dbl_price1:^10}") 
print(f"Price 2 is {dbl_price2:^10}")
print(f"Price 3 is {dbl_price3:^10}")

#to give + sign to all postive number
print(f"Price 1 is {dbl_price1:+}") 
print(f"Price 2 is {dbl_price2:+}")
print(f"Price 3 is {dbl_price3:+}")

#to see the amount comma sepreated us :,
print(f"Price 1 is {dbl_price1:,}") 
print(f"Price 2 is {dbl_price2:,}")
print(f"Price 3 is {dbl_price3:,}")

#suing combination of formate seprators :,
print(f"Price 1 is {dbl_price1:,.2f}") 
print(f"Price 2 is {dbl_price2:,.2f}")
print(f"Price 3 is {dbl_price3:,.2f}")
