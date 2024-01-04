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

def is_parenthese_matching(parentehse):
    """()"""
    stack = ArrayStack()
    check1 = check2 = 0
    for i in parentehse:
        if i == '(':
            stack.push(i)
            check1 += 1
        if i == ')':
            stack.pop()
            check2 += 1
    if check1 != check2:
        return False
    return stack.is_empty()

def main(parentehse):
    """print"""
    if is_parenthese_matching(parentehse):
        print("Parentheses in %s are matched"%parentehse)
        print(True)
    else:
        print("Parentheses in %s are unmatched"%parentehse)
        print(False)
main(input())
