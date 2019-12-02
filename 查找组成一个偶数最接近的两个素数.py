while True:
    try:


        # 先找出小于number的所有素数
        number = int(input())
        prime_list = []
        for i in range(3, number, 2):
            for j in range(3, i):
                if (i % j) == 0:
                    break
            else:
                prime_list.append(i)

        # 然后从"中间"开始遍历这个列表
        list_size = len(prime_list)
        rst = []
        difference = number
        for i in range(0, list_size):
            for j in range(list_size - 1, i - 1, -1):
                if prime_list[i] + prime_list[j] == number:
                    if prime_list[j] - prime_list[i] < difference:
                        difference = prime_list[j] - prime_list[i]
                        rst = [prime_list[i], prime_list[j]]
        print(rst[0])
        print(rst[1])

    except:
        break