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

class Project:
    """Project"""
    def __init__(self, name, val_n):
        """wat?"""
        self.name = name
        self.val_n = val_n
        self.member = sorted([input() for _ in range(val_n*2)])
    def showprojectname(self):
        """showprojectname"""
        print('Hello There! This is', self.name)
        print('This project has %d members' %self.val_n)
    def showmember(self):
        """showmember"""
        for i in self.member:
            if not i.isalnum():
                Person(name=i, age=None).say_hello()
def main():
    """main runner"""
    name = Project(input().rstrip(), int(input()))
    name.showprojectname()
    name.showmember()
main()
