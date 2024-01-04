"""Lab 01.06"""
class Elevator:
    """class"""
    def __init__(self, max_floor):
        """intit"""
        self.val_n = 0
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        """go tototo"""
        if floor <= self.max_floor:
            self.current_floor = floor
        else:
            self.val_n += 1

    def report_current_floor(self):
        """report"""
        for _ in range(self.val_n):
            print('Invalid Floor!')
        print(self.current_floor)

def main():
    """main"""
    max_floor = int(input())
    elevator = Elevator(max_floor)
    while True:
        floor = input()
        if floor == 'Done':
            elevator.report_current_floor()
            break
        elevator.go_to_floor(int(floor))
main()
