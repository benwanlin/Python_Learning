def print_8_ljust(string):
    while len(string) > 8:
        print(string[0:8])
        string = string[8:]
    if len(string) > 0:
        print(string.ljust(8, '0'))

while True:
    try:
        for i in range(2):
            print_8_ljust(input())
    except:
        break