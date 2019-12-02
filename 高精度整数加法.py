"""
Author: TheSRE
Date: 11/19/2019
Filename: 高精度整数加法
"""


while True:
    try:
        def sum_of_two_string(num1, num2):
            """Sum function"""
            sign = ''
            # 两个数都是正数，或者两个数都是负数。
            if (num1.startswith('-') and num2.startswith('-')) or (not num1.startswith('-') and not num2.startswith('-')):
                if num1.startswith('-') and num2.startswith('-'):
                    sign = '-'
                    num1, num2 = num1[1:], num2[1:]

                carry = 0
                if len(num1) > len(num2):
                    num2 = '0' * (len(num1) - len(num2)) + num2
                elif len(num1) < len(num2):
                    num1 = '0' * (len(num2) - len(num1)) + num1

                # print('num1', num1)
                # print('num2', num2)

                rst = ''
                while num1 != '' or num2 != '':
                    # print(num1[-1], num2[-1])
                    tmp_sum = int(num1[-1]) + int(num2[-1]) + carry
                    # print(num1[-1], num2[-1], tmp_sum, carry)
                    carry = tmp_sum // 10
                    tmp_rst = tmp_sum % 10
                    rst = str(tmp_rst) + rst
                    num1, num2 = num1[:-1], num2[:-1]

                    # print(rst)

                if carry > 0:
                    rst = str(carry) + rst
                while rst.startswith('0'):
                    rst = rst[1:]
                return sign + rst

            # 一正一负
            else:
                if num1.startswith('-'):
                    num1 = num1[1:]
                    negative = 'num1'
                else:
                    num2 = num2[1:]
                    negative = 'num2'
                #
                bigger = ''
                # 比较操作数的大小
                if len(num1) > len(num2):
                    bigger = 'num1'
                elif len(num1) < len(num2):
                    bigger = 'num2'
                else:
                    for i in range(len(num1)):
                        if num1[i] > num2[i]:
                            bigger = 'num1'
                            break
                        elif num1[i] < num2[i]:
                            bigger = 'num2'
                            break
                if bigger == '':
                    return 0
                elif bigger == 'num2' and negative == 'num2':
                    sign = '-'
                    # 交换操作数，将大的放到num1去。
                    num1, num2 = num2, num1
                elif bigger == 'num1' and negative == 'num1':
                    sign = '-'
                rst = ''
                carry = 0
                num2 = '0' * (len(num1) - len(num2)) + num2
                while num1 != '':
                    if int(num1[-1]) - int(num2[-1]) - carry > 0:
                        tmp_minus = int(num1[-1]) - int(num2[-1]) - carry
                        print(tmp_minus)
                        carry = 0
                    else:
                        tmp_minus = int('1' + num1[-1]) - int(num2[-1]) - carry
                        print(tmp_minus)
                        carry = 1
                    rst = str(tmp_minus) + rst
                    num1, num2 = num1[:-1], num2[:-1]
                return sign + rst

        num1, num2 = str(input().strip()), str(input().strip())
        print(sum_of_two_string(num1, num2))

    except:
        break