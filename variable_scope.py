'''
variable scope : where a variable is visible and accessible
scope resolution : (LEGB) Local -> Enclosed -> Global -> Built-in
'''
from math import e
# will print 1
def fun1():
    a=1
    print(a)
# will print 2
def fun2():
    a=2
    print(a)

fun1()
fun2()
    
def parent_func():
    a=1
    print(a,"Parent")
    def child_1():
        print(a,"child.......") # since a is not found in local access Enclosed scope a --> 1
    child_1()
    
parent_func()


def parent_func_1():
    def child_1():
        # since a is not found in local access Enclosed scope if a is not found in Enclosed check in global scope a --> 25
        print(a,"child........") 
    child_1()
    
a=25

parent_func_1()



def parent_func_2():
    def child_1():
        # since e is not found in local access Enclosed scope if e is not found in Enclosed check in global scope e 
        # if e is not in global scope check in built in  e --> 2.718281828459045
        print(e,"child......") 
    child_1()

parent_func_2()