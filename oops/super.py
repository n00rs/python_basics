'''
super()  = Function used in a class to call methods from a parent class (superclass)
            Allows you to extend the functionality of the inherited methods
'''
# 
class Shape:
    def __init__(self,str_color,bln_filled):
        self.str_color = str_color
        self.bln_filled = bln_filled
    
    def descibe(self):
        print(f"It is {self.str_color} and {"filled" if self.bln_filled else 'not filled' }")
# 
class Circle(Shape):
    def __init__(self,str_color,bln_filled,dbl_radius):
        # calling Shape's constructor function
        super().__init__(str_color,bln_filled)
        self.dbl_radius = dbl_radius
    
    def descibe(self):
        print(f"Its a circle with an area of {3.14 * self.dbl_radius * self.dbl_radius}")
        super().descibe()
# 
class Square(Shape):
    def __init__(self,str_color,bln_filled,dbl_width):
        super().__init__(str_color,bln_filled)
        self.dbl_width = dbl_width
        
    def descibe(self):
            print(f"Its a Square with an area of {self.dbl_width * self.dbl_width}")
            super().descibe()
            
# 
class Triangle(Shape):
    def __init__(self,str_color,bln_filled,dbl_width,dbl_height):
        super().__init__(str_color,bln_filled)
        self.dbl_width = dbl_width
        self.dbl_height = dbl_height
        
    def descibe(self):
        print(f"Its a Triangle with an area of {self.dbl_width * self.dbl_height/2}")
        super().descibe()

cls_cir = Circle("Red",True,5)
print(cls_cir.str_color)
print(cls_cir.bln_filled)
print(cls_cir.dbl_radius)
cls_cir.descibe()
cls_sqr = Square("Blue",True,5)
print(cls_sqr.str_color)
print(cls_sqr.bln_filled)
print(cls_sqr.dbl_width)
cls_sqr.descibe()

cls_tri = Triangle("Yellow",True,5,1)
print(cls_tri .str_color)
print(cls_tri .bln_filled)
print(cls_tri .dbl_height)
print(cls_tri .dbl_width)
cls_tri.descibe()
