while True:
    try:
        """
        Author: TheSRE
        Date: 11/17/2019
        Filename: 统计每个月兔子的总数
        """

        def getNum(k):

            one_count = 1
            two_count = 0
            three_count = 0

            month = 1
            while month < k:
                # 将年龄为1个月大的兔子数量，存在tmp_count变量
                tmp_count = one_count
                # 计算年龄在第1个月（[0-1]）的兔子数量，存在one_count变量。（请注意，刚出生的兔子，包括刚晋级的新妈妈兔子以及生二胎以上的妈妈兔子生产的兔子，因此等于two_count + three_count）
                one_count = two_count + three_count
                # 计算年龄在第2个月（[1-2]）的兔子数量，存在two_count变量。（请注意，年龄在第2个月的，全部是上个月年龄在1个月大的，因此等于上个月的one_count）
                two_count = tmp_count
                # 计算年龄在第3个月及以上（[2-*]）的兔子数量，存在three_count变量。（请注意，年龄在第3个月及以上的兔子，每只都会生产一只兔子，因此three_count = one_count）
                three_count = one_count

                month += 1
            return one_count + two_count + three_count

        print(getNum(int(input())))

        # 直接使用斐波那契数列求：
        # month = int(input()) # 获取月数
        # num_list = [1, 1] # 初始两个月的兔子数量
        # while len(num_list) < month:
        #     num_list.append(num_list[-1] + num_list[-2]) # 将每个月的兔子数量存入列表中
        # print(num_list[-1]) # 打印最后一个月的兔子数量

    except:
        break