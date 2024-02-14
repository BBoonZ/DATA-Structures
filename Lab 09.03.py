"""main"""
def main():
    """main"""
    num = input()
    check = 9
    total = 0
    for i in range(1, len(num)):
        total += check*(i+1)
        num = int(num)-check
 
        check = int('9' + '0'*i)
    print(total+(num*(len(str(check))+1)))
main()
