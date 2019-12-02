while True:
    try:
        from collections import Counter
        number_bin = bin(int(input()))
        print(Counter(str(number_bin))['1'])

        # print(bin(int(input())).count("1"))  # 一行解法

    except:
        break