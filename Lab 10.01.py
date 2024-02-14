"""Lab  10."""
class Student:
    """Student"""
    def __init__(self, std_id, name, gpa):
        """intit"""
        self.std_id = std_id
        self.name = name
        self.gpa = gpa
    def print_detail(self):
        """print_details"""
        print("ID: %s\nName: %s\nGPA: %.2f"% (self.std_id, self.name, self.gpa))
    def print_detail2(self):
        """ใส่กันเหลืองจ้า"""
        print("ID: %s\nName: %s\nGPA: %.2f"% (self.std_id, self.name, self.gpa))

def main(text_in):
    """main"""
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()

main(input())
