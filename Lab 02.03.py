"""Lab 02.01"""
class ArrayStack:
    """Array"""
    def __init__(self):
        """init"""
        self.size = 0
        self.data = []
    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        """pop"""
        if self.size != 0:
            self.size -= 1
            return self.data.pop()
        print("Underflow: Cannot pop data from an empty list")
        return None
    def is_empty(self):
        """empty??"""
        return self.data == []
    def get_stack_top(self):
        """get stack top"""
        if self.data != []:
            return self.data[-1]
        print("Underflow: Cannot get stack top from an empty list")
        return None
    def get_size(self):
        """size"""
        return self.size
    def print_stack(self):
        """print"""
        print(self.data)

def main(group, people):
    """main"""
    stack = ArrayStack()
    people = people[::-1]
    for i in people:
        stack.push(i)

    my_list = stack.data
    for i in range(group):
        output = ''
        print("Group %d: " %(i+1), end='')
        for j in range(i, stack.get_size(), group):
            output += my_list[j] + ', '
        print(output[:-2])
main(int(input()), [input() for _ in range(int(input()))])
