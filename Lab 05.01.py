"""Lab 05.01"""
class DataNode:
    """DateNode"""
    def __init__(self, data=None):
        """init"""
        self.__data = data
        self.__next = None
    def get_data(self):
        """get_data"""
        return self.__data
    def set_data(self, data):
        """set_data"""
        self.__data = data
    def get_next(self):
        """get_next"""
        return self.__next
    def set_next(self, next_node):
        """set"""
        self.__next = next_node

DATA_ = DataNode(input())

print(DATA_.get_data())
print(DATA_.get_next())
