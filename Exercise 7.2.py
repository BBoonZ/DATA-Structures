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

    def inorder(self, root=None):
        """inorder"""
        if root != None:
            if root.get_left() != None:
                self.inorder(root.get_left())
            print("->", root.get_data(), end=' ')
            if root.get_right() != None:
                self.inorder(root.get_right())
        else:
            root = self.get_root()
            self.inorder(root)

    def postorder(self, root=None):
        """postorder"""
        if root != None:
            if root.get_left() != None:
                self.postorder(root.get_left())
            if root.get_right() != None:
                self.postorder(root.get_right())
            print("->", root.get_data(), end=' ')
        else:
            root = self.get_root()
            self.postorder(root)
    def traverse(self):
        """traverse"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder()
        print('\nInorder: ', end='')
        self.inorder()
        print('\nPostorder: ', end='')
        self.postorder()

    def find_min(self):
        """find_min"""
        if self.is_empty():
            return None
        current = self.get_root()
        while current:
            if current.get_left() == None:
                return current.get_data()
            current = current.get_left()

    def find_max(self):
        """find_max"""
        if self.is_empty():
            return None
        current = self.get_root()
        while current:
            if current.get_right() == None:
                return current.get_data()
            current = current.get_right()

    def delete(self, data):
        """kking of 'if else' is kittipich 018 bro is my idol"""
        current = self.root
        prev = current
        if self.is_empty():
            return print("Delete Error, {data} is not found in Binary Search Tree."\
            .format(data=data))
        try:
            while current:

                #case 1
                if current.data == data and current.left == None and current.right == None:
                    #print("case 1")
                    #case root
                    if self.root.data == data:
                        self.root = None

                    if data < prev.data:
                        prev.set_left(None)
                    else:
                        prev.set_right(None)
                    return data

                #case 2
                if current.data == data and current.left != None and current.right == None:
                    #print("case 2")
                    #case root
                    if self.root.data == data:
                        self.root = current.left

                    if data < prev.data:
                        prev.set_left(current.left)
                    else:
                        prev.set_right(current.left)
                    return data

                #case 3
                if current.data == data and current.left == None and current.right != None:
                    #print("case 3", prev.data, current.data)
                    #case root
                    if self.root.data == data:
                        self.root = current.right

                    if data < prev.data:
                        prev.set_left(current.right)
                    else:
                        prev.set_right(current.right)
                    return data

                #case 4!!!!
                if current.data == data and current.left != None and current.right != None:
                    #print("case 4")
                    #find_max of min
                    min_left = current.left
                    while min_left:
                        if min_left.right == None:
                            min_left = min_left.data
                            break
                        min_left = min_left.right
                    #print(min_left)

                    if self.root.data == data:
                        self.delete(min_left)
                        self.root.data = min_left

                    if current.data == data:
                        self.delete(min_left)
                        current.data = min_left
                    break

                #case not found
                if current.data != data and current.left == None and current.right == None:
                    return print("Delete Error, {data} is not found in Binary Search Tree."\
                    .format(data=data))

                prev = current

                if data < current.data:
                    current = current.get_left()
                elif data >= current.data:
                    current = current.get_right()

        except AttributeError:
            print("Delete Error, {data} is not found in Binary Search Tree.".format(data=data))
def main():
    """main"""
    my_bst = BST()
    data_list = []
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
            data_list.append(int(data))

    total = 0
    for i in data_list:
        count = 0
        current = my_bst.get_root()
        while current:
            if i == current.data:
                count += 1
                total = max(total, count)
                break

            if i < current.data:
                current = current.get_left()
            elif i >= current.data:
                current = current.get_right()
            count += 1
    print(total)
main()
