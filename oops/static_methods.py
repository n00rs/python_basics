'''
Static method = A method that belong to the class rather than any object from that class (instance)
                used for utility function
                
instance method = for operations on instance of class    
static method = method that no nedd to access the object | class data
'''

class Employee:
    def __init__(self,str_name,str_position):
        self.str_name =  str_name
        self.str_position  = str_position 
        
    # instance method depened on other class data
    def get_info(self):
        return f"{self.str_name} = {self.str_position}"
    
    # static method to chech whether an position is valid
    @staticmethod
    def position_is_valid(str_position:str):
        list_positions = ["Manager","Cook","Cashier","Janitor"]
        return str_position in list_positions
    
# to call static method no need to create instance

print(Employee.position_is_valid("Manager"))

obj_emp1 = Employee("James","Manager")
obj_emp2 = Employee("Salam","Cashier")
obj_emp3 = Employee("Sali","Cook")

print(obj_emp1.get_info())
print(obj_emp2.get_info())
print(obj_emp3.get_info())


'''
Class Methods : allow opertaions related to the class itself 
                Take (self) as the parameter which represent the class itself

'''

class Student:
    
    int_count = 0
    dbl_total_gpa = 0
    def __init__(self,str_name,dbl_gpa):
        self.str_name = str_name
        self.dbl_gpa = dbl_gpa
        Student.int_count += 1
        Student.dbl_total_gpa += dbl_gpa
    # INSTANCE METHOD
    def get_info(self):
        return f"{self.str_name}'s gpa is {self.dbl_gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total no.of students in the class is {cls.int_count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.int_count == 0 :
            return 0
        else:
            return f"{cls.dbl_total_gpa/cls.int_count}"



obj_std1 = Student("Jame",9.6)
obj_std2 = Student("Neymar",7.6)
obj_std3 = Student("Doe",5.1)

print(obj_std1.get_info())

print(Student.get_count())

print(Student.get_avg_gpa())