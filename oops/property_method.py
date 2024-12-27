'''
@property = Decorator used to define a method as a property (it can be accessed like an attribute)
            Benefit add additional logic when read or write or delete
            Getter Setter Deleter
'''

class Rectangle:
    def __init__(self,dbl_width,dbl_height):
        self._dbl_width = dbl_width
        self._dbl_height = dbl_height
    
    @property    
    def width(self):
        return f"{self._dbl_width:.2f}cm"
    
    @property
    def height(self):
        return f"{self._dbl_height:.2f}cm"
    
    @width.setter
    def width(self,dbl_new_width):
        if dbl_new_width > 0:
            self._dbl_width = dbl_new_width
        else:
            print("Width must be > 0")
            
    @height.setter
    def height(self,dbl_new_height):
        if dbl_new_height > 0:
            self._dbl_height = dbl_new_height
        else:
            print("height must be > 0")
            
    @height.deleter
    def height(self):
        del self._dbl_height
        print("height has been removed")
        
    @width.deleter
    def width(self):
        del self._dbl_width
        print("width has been removed")
    
        
obj_rect = Rectangle(3,4)

obj_rect.width = 5
obj_rect.height = 10  
    
print(obj_rect.width)
print(obj_rect.height)

del obj_rect.width
del obj_rect.height

