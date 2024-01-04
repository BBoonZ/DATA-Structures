"""Lab 1.04"""
class Rectangle:
    """class"""
    def __init__(self, height, width):
        """intit"""
        self.height = height
        self.width = width
 
    def calculate_area(self):
        """area"""
        return self.height * self.width
 
    def calculate_perimeter(self):
        """perimeter"""
        return (self.height + self.width) * 2
 
def main():
    """main"""
    rectangle = Rectangle(float(input()), float(input()))
 
    condition = input()
    if condition == "area":
        result = rectangle.calculate_area()
    else:
        result = rectangle.calculate_perimeter()
    print("%.2f" % result)
main()
