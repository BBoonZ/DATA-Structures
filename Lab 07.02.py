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

class BST:
    """BST"""
    def __init__(self):
        """__init__"""
        self.root = None
    def get_root(self):
        """get_root"""
        return self.root
    def set_root(self, root):
        """set_root"""
        self.root = root
    def insert(self, data):
        """insert"""
        #self.root.data = data
        new_node = BSTNode(data)
        current = self.get_root()
        if self.root == None:
            self.root = new_node
        else:
            while True:
                if data < current.get_data():
                    if current.get_left() == None:
                        current.set_left(new_node)
                        break
                    current = current.get_left()
                elif data >= current.get_data():
                    if current.get_right() == None:
                        current.set_right(new_node)
                        break
                    current = current.get_right()

    def is_empty(self):
        """is_empty"""
        return self.root == None

    def preorder(self, root=None):
        """preorder"""
        if root != None:
            print("->", root.get_data(), end=' ')
            if root.get_left() != None:
                self.preorder(root.get_left())
            if root.get_right() != None:
                self.preorder(root.get_right())
        else:
            root = self.get_root()
            self.preorder(root)

def main():
    """main"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
 
    print("Preorder: ", end="")
    my_bst.preorder()
main()
