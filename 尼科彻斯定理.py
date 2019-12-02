while True:
    try:
        number = int(input().strip())

        number_to_the_power_of_3 = number * number * number

        if number == 1:
            print(1)
        else:
            avarage = int(number_to_the_power_of_3 / number)
            avarage_count = number // 2
            rst = []
            if number % 2 == 0:
                for i in range(number):
                    rst.append(str(avarage - (avarage_count - i) * 2 + 1))
            else:
                for i in range(number):
                    rst.append(str(avarage - (avarage_count - i) * 2))
        print('+'.join(rst))

    except:
        raise