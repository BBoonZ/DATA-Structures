"""Exercise 01.01"""
def main(num, output=''):
    """12012"""
    for i in num:
        output += i
    print(output)
main([input() for _ in range(5)])
