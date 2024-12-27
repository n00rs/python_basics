'''
Decorator = A function that extends the behavior of another function w/o modifing the
            base function
            Pass the base function as an argument to the decorator
'''


'''
this func will be called when we add it as decorator 
@add_sprinkles
in order to handle that write an wrapper function which is returned 
a parameter function will passed to it
'''
def add_sprinkles(func):
    print("befor wrapper")
    def wrapper(*args,**kwargs):
        print("sprinkles added")
        func(*args,**kwargs)
    
    return wrapper

# another decorator function

def add_fudge(func):
    def wrapper(*args,**kwargs) :
        print("Fudge added")
        func(*args,**kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(str_flavor):
    print(f"Here's your ice cream {str_flavor}")
    
get_ice_cream("Choco")

