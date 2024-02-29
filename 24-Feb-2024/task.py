class Shape():
    def __init__(self,area,perimeter):
        self.area = area
        self.perimeter = perimeter
    
    def area(self):
        return 0
    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return self.width  + self.length * 2

    
class Square(Shape):
    def __init__(self,length):
        self.length = length

    
    def area(self):
        return self.length * self.length
        
    def perimeter(self):
        return self.length * 4

rectangle = Rectangle(8,2)
square = Square(6)


print("+---------------------------+")
print("|        Rectangle          |")
print("+---------------------------+")
print(f"| Area : {rectangle.area()}                 |")    
print(f"| Perimeter : {rectangle.perimeter()}            |")           
print("+---------------------------+")
print("|          Square           |")
print("+---------------------------+")
print(f"| Area : {square.area()}                 |")    
print(f"| Perimeter : {square.perimeter()}            |")
print("+---------------------------+")
