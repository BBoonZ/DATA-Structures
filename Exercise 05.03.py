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
    val_n = int(input())
    score_sum = 0
    singly_id = SinglyLinkedList()
    singly_score = SinglyLinkedList()
    for _ in range(val_n):
        _id, score = input().split()
        singly_id.insert_last(_id)
        singly_score.insert_last(float(score))

    current = singly_score.head
    while current:
        score_sum += current.get_data()
        current = current.get_next()
    score_sum /= val_n

    current_score = 0
    current = singly_score.head
    while current:
        if current.get_data() <= score_sum and current_score < current.get_data():
            current_score = current.get_data()
        current = current.get_next()

    current_id = singly_id.head
    current_sc = singly_score.head
    while current_sc:
        if current_sc.get_data() == current_score:
            print(current_id.get_data(), current_sc.get_data(), sep='\t')
            break
        current_id = current_id.get_next()
        current_sc = current_sc.get_next()
main()
