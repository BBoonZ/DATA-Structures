"""Lab 07"""
class BSTNode:
    """BSTNode"""
    def __init__(self, data=None):
        """__init__"""
        self.data = data
        self.left = None
        self.right = None
    def set_data(self, data):
        """set_data"""
        self.data = data
    def get_data(self):
        """set_data"""
        return self.data
    def set_left(self, left):
        """set_left"""
        self.left = left
    def get_left(self):
        """get_left"""
        return self.left
    def set_right(self, right):
        """set_right"""
        self.right = right
    def get_right(self):
        """get_right"""
        return self.right

BST_ = BSTNode(int(input()))
print(BST_.get_data())
print(BST_.get_left())
print(BST_.get_right())
