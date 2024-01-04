"""Exercise 00.03"""
def main(name, new_name):
    """Exercise 00.03"""
    while name:
        noi = name[0]
        for i in name:
            if noi > i:
                noi = i
        new_name.append(name.pop(name.index(noi)))
    print(*new_name, sep='\n    ')
main([input() for _ in range(int(input()))], [])
