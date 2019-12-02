while True:
    try:
        num_set = set()
        for i in range(int(input())):
            num_set.add(int(input()))
        for i in sorted(list(num_set), reverse=False):
            print(i)

    except:
        raise