"""Lab 01.05"""
class Point:
    """class"""
    def __init__(self, val_x=0, val_y=0):
        """self"""
        self.set_coordinates(val_x, val_y)
 
    def set_coordinates(self, val_x, val_y):
        """set values"""
        self.val_x = val_x
        self.val_y = val_y
 
    def get_coordinates(self):
        """get coorinates"""
        return (self.val_x, self.val_y)
 
    def calculate_distance(self, other_point):
        """return cal"""
        return "%.2f"%(((other_point.val_x - self.val_x)**2 + \
        (other_point.val_y - self.val_y)**2) ** 0.5)
 
def main():
    """main"""
    art = Point(float(input()), float(input()))
    boss = Point(float(input()), float(input()))
    #print(art, boss)
    result = art.calculate_distance(boss)
    print(result)
    # print(point.calculate_distance(float(input()), float(input())))
main()
