while True:
    try:
        string = input().strip()

        count = 0
        for i in string:
            if i.isupper():
                count += 1
        print(count)

    except:
        break