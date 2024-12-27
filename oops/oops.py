 
 
 
'''
 object =  A bundle of related attributes (variables) and methods (functions)
           Ex. phone, cup , book
           you need a "class" many objects
Class = (blueprint) used to design the structure of object
'''

class Car:
    def __init__(self,model,year,color,bln_sale=False):
        print(self)  
        self.model=model
        self.year = year
        self.color=color
        self.bln_sale=bln_sale
    
    def drive(self):
        return f"You drive {self.color} {self.model}"
    def stop(self):
        return f"You stop {self.color} {self.model}"
    def describe(self):
        print(f"{self.year} {self.color} {self.model} ")
        
car1 = Car("mustang",2024,"red")

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.bln_sale)

print(car1.drive())
print(car1.stop())
car1.describe()

'''
Class variables = shared among all instances of a class
                  Defined outside the constructor
                  Allow you to share data among all objects created from that class
'''

class Student:
    # class variable
    class_year = 2024
    int_total_students = 0
    def __init__(self,str_name,int_age):
        self.str_name = str_name
        self.int_age = int_age
        Student.class_year = 2025
        Student.int_total_students += 1
cls_std1 = Student("Jane",24)
cls_std2 = Student("Jon",14)

print(cls_std1.str_name)
print(cls_std2.str_name)
print(cls_std1.class_year)
print(cls_std2.class_year)
# it good to access it directly from class
print(Student.class_year)
print(Student.int_total_students)

'''
Inheritance = Allows a class to inherit attributes and method from another class
              Helps with code maintablilty and extensibility
              class child(parent)

'''

class Animal:
    def __init__(self,name):
        self.name = name 
        self.bln_alive = True 
    
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
# class Dog inherits all properties of class animal
class Dog(Animal):
    
    def speak(self):
        print("Woof..!")

# class Cat inherits all properties of class animal
class Cat(Animal):
    
    def speak(self):
        print("Meow..!")

# class Mouse inherits all properties of class animal
class Mouse(Animal):
    
    def speak(self):
        print("Squeek..!")

cls_cat = Cat("Tom")
cls_dog = Dog("Scobee")
cls_mouse = Mouse("Tom")

print(cls_cat.name)
print(cls_dog.name)
print(cls_mouse.name)
cls_cat.speak()
cls_dog.speak()
cls_mouse.speak()

'''
multiple inheritance = inherit from more than one parent class
                       C(A,B)
multilevel inheritance = inherit from a parent which inherits from another parent
                         c(B) <- B(A) <- A
'''
class Animal:
    def __init__(self,str_name):
        self.str_name = str_name
        
    def eat(self):
        print(f"This {self.str_name} is eating")

    def sleep(self):
        print(f"This {self.str_name} is sleeping")

class Prey(Animal):
    # def __init__(self):
    #     pass
    def flee(self):
        print(f"This {self.str_name} is fleeing ")
    
class Predator(Animal):
    # def __init__(self):
    #     pass 
    def hunt(self):
        print(f"This {self.str_name} is Hunting")
    
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

cls_rabbit = Rabbit("Bunny")
cls_hawk = Hawk("Tony")
cls_fish = Fish("Nemo")

cls_rabbit.flee()
# cls_rabbit.hunt() --> doesn't inherit Predator
cls_hawk.hunt()
# cls_hawk.flee() --> doesn't inherit Prey

cls_fish.flee() # -->  has both 
cls_fish.hunt() 
# using Parents Parents artbutes
cls_rabbit.eat()
cls_rabbit.sleep()

cls_hawk.eat()
cls_hawk.sleep()
    
cls_fish.eat()
cls_fish.sleep()

