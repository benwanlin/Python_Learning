while True:
    try:

        start = input()
        if start.isdigit():

            a, b, c = 15, 9, 1
            total_cost = 300

            for i in range(int(300/15)):
                for j in range(int(300/9) - i):
                    for k in range(300 - i - j):
                        if 15 * i + 9 * j + k == 300 and i + j + k == 100:
                            print(i, j, k)

    except:
        break