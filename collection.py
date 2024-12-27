'''
collection : single variable holds multiple values
    list = [] ordered and changeable , Duplicates ok
    set = {} unordered and immutable but add/remove Ok No duplicates 
    Tuple = () ordered and 
'''

list_fruits = ["apple","orange","mango","Jack fruit"]

# print(list_fruits[4]) throws an IndexError: list index out of range

print(list_fruits[::-1])

'''
looping through the list
'''
# for i in list_fruits:
#     print(i)

# print(dir(list_fruits))
'''
methods of list
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
'__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
# to get the list's length
print(len(list_fruits))
# check whether an item is in list
print("pineapple" in list_fruits)
# assign pineapple to index 0
# list_fruits[0] = "pineapple"

# add an element to the end of list
list_fruits.append("pineapple")
print(list_fruits)
# remove an apple element from list
list_fruits.remove("apple")
print(list_fruits)
# insert an element to an index
list_fruits.insert(0,"apple")
print(list_fruits)
# to sort in alphabetical order
list_fruits.sort()
print(list_fruits)
# to reverse the list 
list_fruits.reverse()
print(list_fruits)
# to remove all elements in list
# list_fruits.clear() 

# to get index of specfic element
# when given an value that is not in list will throw exception ->ValueError: 'capple' is not in list
# print(list_fruits.index("capple"))

# to count no.of occurences
print(list_fruits.count("capple"))



set_fruits = {"apple","orange","banana","mango"}

print(set_fruits)
# print(dir(set_fruits))
'''
set methods
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', 
'__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', 
'__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 
'__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 
'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
'''
print(len(set_fruits))
# to see an value is in set 
print("banana" in set_fruits)
# we can't use index in set 
# print(set_fruits[0]) # throws TypeError: 'set' object is not subscriptable
# to add an new element to set 
set_fruits.add("pineapple")
print(set_fruits)
# to remove an element when mentioned an element that is not in list throws an exception KeyError
set_fruits.remove("apple")
print(set_fruits)
# pop will remove first element(ie , random)
set_fruits.pop()
# to remove all element use clear method
set_fruits.clear()

print(set_fruits)


'''
TUPLES - collection that is surrounded by paranthesis
ordered and unchangeable and allow duplicates are ok 
Faster
'''
tuple_fruits = ("apple","orange","mango","banana","apple")
print(tuple_fruits)

# print(dir(tuple_fruits))

'''
tuple methods
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', 'count', 'index']
'''
# find length of a tuple
print(len(tuple_fruits))
# check whether an value is in tuple
print("apple" in tuple_fruits)
# to find index of an element 
#  when mentioned a element ie not in tuple throws ValueError: tuple.index(x): x not in tuple
# print(tuple_fruits.index("capple"))

# to count all occurence of an element 
print(tuple_fruits.count("apple"))

# iterate over tuple
for fruit in tuple_fruits:
    print(fruit)
    
print("=================================SHOPPING CART")

'''
SHOPPING CART PROGRAM 
                    for implementin collections
'''
list_foods = []
list_prices = []
dbl_total = 0

while True:
    str_food = input("Enter a food to buy (q to quit)")
    if str_food.lower() == "q":
        break
    else:
        dbl_price = float(input(f"Enter the price of {str_food} :"))
        list_foods.append(str_food)
        list_prices.append(dbl_price)
    
print(list_foods)

for food in list_foods:
    print(food)
    
for price in list_prices:
    dbl_total += price

print(f"Your total is : {dbl_total:.2f}")




















