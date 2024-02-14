"""Lab  10."""
class Student:
    """Student"""
    def __init__(self, std_id, name, gpa):
        """intit"""
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        """id std"""
        return int(self.std_id)

    def get_name(self):
        """name"""
        return self.name

    def get_gpa(self):
        """gpa"""
        return self.gpa

    def print_detail(self):
        """print_details"""
        print("ID: %d\nName: %s\nGPA: %.2f"% (self.std_id, self.name, self.gpa))

class ProbHash:
    """ProbHash"""
    def __init__(self, size):
        self.hash_table = list()
        self.size = size
        for _ in range(size):
            self.hash_table.append('-')
    def hash(self, key):
        """hash"""
        return key%self.size
    def rehash(self, hkey):
        """rehash"""
        for i in range(hkey, self.size):
            if self.hash_table[i] == '-':
                return i
        for i in range(0, self.size):
            if self.hash_table[i] == '-':
                return i

    def insert_data(self, student):
        """insert_data"""
        if self.hash_table.count('-') == 0:
            return print("The list is full. %d could not be inserted."% (student.get_std_id()))

        index = self.hash(student.get_std_id())
        if self.hash_table[index] != '-':
            index = self.rehash(index)

        self.hash_table[index] = student
        print("Insert %d at index %d"% (student.get_std_id(), index))


    def search_data(self, std_id):
        """search_data"""
        for i in range(self.size):
            if self.hash_table[i] != '-' and self.hash_table[i].get_std_id() == std_id:
                print("Found %d at index %d"% (std_id, i))
                return self.hash_table[i]
        print("%d does not exist."% std_id)


def main():
    """main ja"""
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")
main()
