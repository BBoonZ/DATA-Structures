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
        if not self.is_empty():
            return self.data[-1]
        print("Underflow: Cannot get stack top from an empty list")
        return None
    def get_size(self):
        """size"""
        return self.size
    def print_stack(self):
        """print"""
        print(self.data)

def main(infix):
    """main"""
    postfix = ''
    check = ArrayStack()
    for i in infix:
        if i in ['+', '-']:
            while not check.is_empty():
                postfix += check.pop()
            check.push(i)
        elif i in ['*', '/']:
            while not check.is_empty() and check.get_stack_top() in ['*', '/']:
                postfix += check.pop()
            check.push(i)
        elif i != ' ':
            postfix += i

    while not check.is_empty():
        postfix += check.pop()
    print(postfix)
main(input())
