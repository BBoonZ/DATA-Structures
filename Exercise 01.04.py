"""Exercise 01.04"""
def main(kilo):
    """main"""
    if 52.900 < kilo <= 58.855:
        print("Chon Buri")
    elif 35.477 < kilo <= 52.900:
        print("Chachoengsao")
    elif 5.032 < kilo <= 35.477:
        print("Samut Prakarn")
    elif 0 <= kilo <= 5.032:
        print("Bangkok")
    else:
        print("InValid")
main(float(input()))
