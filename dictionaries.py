'''
Dictionary : collection of {Key:Value} pairs ordered and changeable .No ducplicates allowed 
'''

dict_capitals = {
    "USA":"WashingTon D.c",
    "India":"New Delhi",
    "China":"Beijing",
    "Russia":"Moscow"
}

print(dict_capitals)
# print(dir(dict_capitals))
'''
Dictionary methods
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', 
'__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', 
'__setitem__', '__sizeof__', '__str__', '__subclasshook__',
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
'''
# get value corresponding to a key
# when given invalid key returns none
print(dict_capitals.get("India"))

# to add an new key value or update an existing
dict_capitals.update({"Germany":"Berlin"})
dict_capitals.update({"USA":"manhan"})

print(dict_capitals)
# to remove an key value 
dict_capitals.pop("China")
print(dict_capitals)
# to remove last item 
dict_capitals.popitem()
print(dict_capitals)

# to clear ths dictionary 
# dict_capitals.clear()
print(dict_capitals)

# to get all keys 
print(dict_capitals.keys())
# iterate over keys
for str_key in dict_capitals.keys():
    print(str_key)

# to get all values of dictionary
print(dict_capitals.values())

# iterating through 
for value in dict_capitals.values():
    print(value)
    
# items method returns list of 2d tuples with 2 elements 0-> key 1->value
print(dict_capitals.items())

for [key,value] in dict_capitals.items():
    print(key,value)
    
'''
concession stand program
'''
dict_menu = {
    "Pizza":1.00,
    "Popcorn":2.00,
    "Nachos":3.00,
    "Fries":4.00,
    "Chips":5.09,
    "Pretzel":6.99,
    "Soda":3.50,
    "Lemonade":4.45
}
print(dict_menu)
print("========MENU===========")
for key,value in dict_menu.items():
    print(f"{key:10}:{value:5,.2f}")
print("------------------------")

list_food = [] #to hold values selected by customer
dbl_total = 0 # for call
while True:
    str_food = input("Select an item from menu (q to quit)")
    if str_food.lower() == "q":
        break
    elif dict_menu.get(str_food) is not None:
        list_food.append(str_food)
    else :
        print("Selected food not in menu")
print("--------Your order ---------")        
for str_food in list_food:
    print(f"{str_food:10}: {dict_menu.get(str_food)}")
    dbl_total +=  dict_menu.get(str_food)
print()
print(f"Your bill Amount is :{dbl_total}")


