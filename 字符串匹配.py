while True:
    try:

        # def check(string1, string2):
        #     # 遍历短字符串，检查字符是否在长字符串中存在。
        #     # 一旦遇到不存在的，就返回'false'；如果没有遇到不存在的，就在最后返回'true'
        #     for i in string1:
        #         if i not in string2:
        #             return 'false'
        #     return 'true'
        #
        #
        # string1 = input().strip()
        # string2 = input().strip()
        #
        # # 如果string1的长度更长，则交换一下string1和string2的值
        # if len(string1) > len(string2):
        #     string1, string2 = string2, string1
        #
        # # 调用函数
        # print(check(string1, string2))

        a, b = set(input().strip()), set(input().strip())
        print('true' if a & b == a else 'false')

    except:
        break