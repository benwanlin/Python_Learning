while True:
    try:
        s = list(input())
        max = 0
        if len(s) == 2:
            if s[0] == s[1]:
                print(2)
            else:
                print(0)
        else:
            for i in range(1, len(s) -1):
                if s[i] == s[i+1]:
                    num = 0
                    start = i
                    end = i + 1
                    while start >=0 and end <= (len(s) - 1) and s[start] == s[end]:
                        num += 2
                        start -= 1
                        end += 1
                    if num > max:
                        max = num

                if s[i - 1] == s[i+1]:
                    num = 1
                    start = i -1
                    end = i + 1
                    while start >=0 and end <= (len(s) - 1) and s[start] == s[end]:
                        num += 2
                        start -= 1
                        end += 1
                    if num > max:
                        max = num
            print(max)

    except:
        break