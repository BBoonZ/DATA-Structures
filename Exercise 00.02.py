"""Exercise 00.02"""
def main(station, time):
    """Exercise 00.02"""
    if station and time >= 240 or time >= 480:
        print('True')
    else:
        print('False')
main(input() == 'Outdoor', float(input()))
