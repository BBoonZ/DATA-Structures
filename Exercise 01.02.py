"""Exercise 01.02"""
class Food:
    """Food"""
    def __init__(self):
        """init"""
        self.menu = ['Pizza', 'Fried Chicken', 'Hamburger', 'Steak']
        self.random = 0
    def random_food(self):
        """ + random """
        self.random += 1
    def list_foods(self):
        """list foods"""
        print(sorted(self.menu))
 
def main():
    """main"""
    Food().list_foods()
main()