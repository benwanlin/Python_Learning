while True:
    try:
        string1 = input().strip()
        string2 = input().strip()
        if len(string1) < len(string2):
            string1, string2 = string2, string1

        # 将较短的字符串左边补0，以达到两个字符串的长度相同，便于下面的便利字符串相加操作。
        string2 = '0' * (len(string1) - len(string2)) + string2

        carry = 0
        result = ''

        # 从字符串尾部开始遍历，直到将字符串遍历完毕。每一位转换成int再相加，保留carry位。
        for i in range(len(string1) - 1, -1, -1):
            tmp_sum = int(string1[i]) + int(string2[i]) + carry
            if tmp_sum > 9:
                tmp_sum %= 10
                carry = 1
            else:
                carry = 0
            result = str(tmp_sum) + result

        # 如果carry位不为0，则前置追加到result字符串中来。
        if carry != 0:
            result = str(carry) + result

        print(result)

    except:
        break