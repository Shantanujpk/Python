# what is method overriding ? 
# why to use it ?
# how to use it ? 



class shape:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y

class shape_circle(shape):
    def __init__(self, r):
        self.r = r
        super().__init__(r, r)
    def area_of_circle(self):
        return 3.14 * super().area() # overriding here 
    

rect =  shape(3,4)
print(rect.area())
    
circle = shape_circle(10)
print(circle.area_of_circle())
