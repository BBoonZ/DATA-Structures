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
    def add_food_item(self, name):
        """add food"""
        self.menu.append(name)

def main(val_n):
    """main"""
    food = Food()
    for _ in range(val_n):
        food.add_food_item(input())
    food.list_foods()
main(int(input()))
