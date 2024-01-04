"""Exercise02-1"""
class ArrayStack:
    """____stack"""

    def __init__(self):
        """____"""
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
        """delete data"""
        try:
            self.size -= 1
            return self.data.pop()
        except (TypeError, ValueError, ArithmeticError, AttributeError, IndexError):
            # print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        """check empty data"""
        return len(self.data) == 0

    def get_stack_top(self):
        """get top of the stack"""
        try:
            return self.data[-1]
        except (TypeError, ValueError, ArithmeticError, AttributeError, IndexError):
            # print("Underflow: Cannot get stack top from an empty list")
            return None

    def get_size(self):
        """return size"""
        return len(self.data)

    def print_stack(self):
        """PRINT"""
        print(self.data)


def infixtopostfix(expression: str):
    """main function"""
    convert = {'+': 1, '-': 1, '*': 2, '/': 2}
    mem = ArrayStack()
    ans = ""
    for i in expression:
        if i in '+-*/':
            if mem.is_empty() or mem.get_stack_top() == '(':
                mem.push(i)
            elif convert[i] > convert[mem.get_stack_top()]:
                mem.push(i)
            else:
                while not mem.is_empty() and convert[i] <= convert[mem.get_stack_top()]:
                    ans += mem.pop()
                    if mem.get_stack_top() == '(':
                        break
                mem.push(i)
        elif i == '(':
            mem.push(i)
        elif i == ')':
            while mem.get_stack_top() != '(':
                ans += mem.pop()
            mem.pop()
        else:
            ans += i
    while not mem.is_empty():
        ans += mem.pop()
    print(ans)
infixtopostfix(input().strip().replace(' ', ''))