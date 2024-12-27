import string
import random

str_chars = string.punctuation + string.digits + string.ascii_letters + " "

print(str_chars)
list_chars = list(str_chars)
list_keys = list_chars.copy()

random.shuffle(list_keys)

print(f"chars : {list_chars}")
print(f"Keys : {list_keys}")

str_text = input("Enter a message to encrypt : ")
str_cipher = ""
# my solution
# int_index = 0
# for i in list_chars:
#     for j in str_text:
#         if j == i:
#             str_cipher += list_keys[int_index] 
#     int_index+=1

for i in str_text:
    int_index = list_chars.index(i)
    str_cipher += list_keys[int_index]            
print(str_cipher)

str_cipher = input("Enter a message to encrypt : ")
str_text  = ""

for i in str_cipher:
    int_index = list_keys.index(i)
    str_text += list_chars[int_index]
    
print(str_text)