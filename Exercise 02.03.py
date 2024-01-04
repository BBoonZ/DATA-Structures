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

def main(label):
    """main"""
    lable_1 = ArrayStack()
    lable_2 = ArrayStack()
    lable_3 = ArrayStack()
    check_1 = check_2 = check_3 = 0
    for i in label:
        if i == '(':
            lable_1.push(i)
            check_1 += 1
        elif i == ')':
            lable_1.pop()
            check_1 -= 1

        if i == '[':
            lable_2.push(i)
            check_2 += 1
        elif i == ']':
            lable_2.pop()
            check_2 -= 1

        if i == '{':
            lable_3.push(i)
            check_3 += 1
        elif i == '}':
            lable_3.pop()
            check_3 -= 1

    if lable_1.is_empty() and lable_2.is_empty() and lable_3.is_empty() and \
        (check_1 == check_2 == check_3 == 0):
        return print('True')
    return print('False')
main(input())
