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

class SinglyLinkedList:
    """SinglyLinkedList"""
    def __init__(self):
        """init"""
        self.count = 0
        self.head = None

    def traverse(self):
        """traverse"""
        if self.head != None:
            loop = self.head
            while loop.get_next() != None:
                print(loop.get_data(), end=' -> ')
                loop = loop.get_next()
            print(loop.get_data())
        else:
            print("This is an empty list.")

    def insert_last(self, data):
        """insert_last"""
        pnew = DataNode(data)
        if self.head == None:
            self.head = pnew
        else:
            loop = self.head
            while loop.get_next() != None:
                loop = loop.get_next()
            loop.set_next(pnew)
        self.count += 1

    def insert_front(self, data):
        """insert_front"""
        pnew = DataNode(data)
        pnew.set_next(self.head)
        self.head = pnew
        self.count += 1

    def insert_before(self, node, data):
        """insert_before"""
        pnew = DataNode(data)
        loop = self.head
        if self.head == None:
            return print("Cannot insert, %s does not exist." %node)
        while True:
            if self.head.get_data() == node:
                self.insert_front(data)
                break
            elif loop.get_next().get_data() == node:
                pnew.set_next(loop.get_next())
                loop.set_next(pnew)
                self.count += 1
                break
            elif loop.get_next().get_next() == None:
                return print("Cannot insert, %s does not exist." %node)
            loop = loop.get_next()

    def delete(self, data):
        """delete"""
        loop = self.head
        if self.head == None or (self.count == 1 and self.head.get_data() != data):
            return print("Cannot delete, %s does not exist." %data)
        if self.head.get_data() == data:
            self.head = loop.get_next()
            self.count -= 1
            return None
        while loop.get_next():
            if loop.get_next().get_data() == data:
                loop.set_next(loop.get_next().get_next())
                self.count -= 1
                break
            elif loop.get_next().get_next() == None and loop.get_data() != data:
                return print("Cannot delete, %s does not exist." %data)
            loop = loop.get_next()

def main():
    """main"""
    singly = SinglyLinkedList()
    while True:
        data = input()
        if data == 'Last':
            break
        singly.insert_last(data)

    node = int(input())
    if singly.count >= node >= 1:
        last = singly.head
        for _ in range(node-1):
            last = last.get_next()
        print(last.get_data())
    else:
        return print("Error")
main()