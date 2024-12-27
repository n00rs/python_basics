'''
Polymorphism Greek word that means have many forms and faces
    Two ways to acheive polymorphism
    Inheritence = An object could be treated of the same type as parent class
    DuckTyping = Object must have necassary attributes/methods
'''
from abc import ABC,abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,dbl_radius):
        self.dbl_radius = dbl_radius
        super().__init__()

    def area(self):
        return 3.14 * self.dbl_radius * self.dbl_radius

class Square(Shape):
    def __init__(self,dbl_width):
        super().__init__()
        self.dbl_width = dbl_width
        
    def area(self):
        return self.dbl_width * self.dbl_width

class Triangle(Shape):
    def __init__(self,dbl_width,dbl_height):
        super().__init__()
        self.dbl_width = dbl_width
        self.dbl_height = dbl_height
    
    def area(self):
        return self.dbl_width * self.dbl_height * 0.05

class Pizza(Circle):
    def __init__(self,str_topping,dbl_radius):
        super().__init__(dbl_radius)
        self.str_topping = str_topping
        self.dbl_radius = dbl_radius
        


list_shapes = [Circle(4),Square(5),Triangle(6,7),Pizza("pepproni",15)]

for shape in list_shapes:
    print(shape.area())


'''
Duck Typing = Another way to achieve polymorphism besides inheritence 
              Object must have the minmum necessary attributes /methods
'''   

class Animals:
    bln_alive = True
    
# 
class Dog(Animals):
    def speak(self):
        print("Woof !")
        
# 
class Cat(Animals):
    def speak(self):
        print("Meow !")
    
# has an speak method
class Car:
    # add an class var alive to match all methods of animals
    bln_alive = False
    def speak(self):
        print("Honk !")

list_animals = [Dog(),Cat(),Car()]

for animal in list_animals:
    animal.speak() 
    print(animal.bln_alive)
