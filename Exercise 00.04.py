"""Exercise 00.04"""
class Person:
    """Person"""
    def __init__(self, name, age):
        """wat?"""
        self.name = name
        self.age = age
    def get_details(self):
        """get_details"""
        print(self.name + ', ' + self.age + ' years old')
    def say_hello(self):
        """say_hello"""
        print("Hello, my name is %s!"% self.name)
def main():
    """main runner"""
    name = Person(input().rstrip(), input())
    name.get_details()
    name.say_hello()
main()