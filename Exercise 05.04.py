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
    '''singly = SinglyLinkedList()
    singly2 = SinglyLinkedList()
    singly3 = SinglyLinkedList()

    singly2.insert_last(6)
    singly3.insert_last(7)
    singly3.insert_last(8)

    singly.insert_last(2)
    singly.insert_last(3)
    singly.insert_last(5)
    singly.insert_last(singly2)
    singly.insert_last(singly3)

    singly.traverse()

    current = singly.head
    while current:
        if type(current.get_data()) != int:
            print(current.get_data())
            singly.delete(current.get_data())
        current = current.get_next()
    singly.traverse()'''

    val_n = int(input())
    val_m = int(input())
    singly_main = SinglyLinkedList()

    for _ in range(val_m):
        data = input().split()
        singly_copy = SinglyLinkedList()
        for i in data:
            singly_copy.insert_last(i)
        singly_main.insert_last(singly_copy)

    #print(singly_main.head.get_data().traverse())
    #1 -> 2 -> 9 -> 3 -> 10 -> 2 -> 10 -> 7 -> 5 -> 8 -> 3 ->\
    #  10 -> 9 -> 5 -> 2 -> 7 -> 9 -> 5 -> 10 -> 9
    bus = SinglyLinkedList()
    total = 0
    for i in range(1, val_m+1):
        station = singly_main.head
        while station:
            if int(station.get_data().head.get_data()) == i:
                check_bus = bus.head
                while check_bus:
                    if int(check_bus.get_data()) == i:
                        bus.delete(str(i))
                        total += 1
                    check_bus = check_bus.get_next()

                people = station.get_data().head
                while people:
                    if bus.count >= val_n:
                        break
                    if int(people.get_data()) > i:
                        bus.insert_last(people.get_data())
                    people = people.get_next()

                singly_main.delete(station.get_data())
                break
            station = station.get_next()
    print(total)
main()
