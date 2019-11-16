"""
Author: Ben
Date: 11/16/2019
"""
import math


def insert_num(x, y, num_list):
    last_x, last_y = num_list[-1][0], num_list[-1][1]
    step = math.trunc((y-last_y)/(x-last_x))
    for num in range(1, x - last_x):
        num_list.append([last_x + num, last_y + step * num])


while True:
    try:
        m, n = [int(i) for i in input().split()]
        num_list = []
        for i in range(int(m)):
            x, y = [int(j) for j in input().split()]
            if len(num_list) > 0:
                if num_list[-1][0] == x:
                    # 如果测量序号与上一次相同，则忽略。
                    continue
                elif num_list[-1][0] + 1 < x:
                    # 如果测量序号比上一次大1，则表示该结果是有丢失的，需要调用insert_num函数补上丢失的。
                    insert_num(x, y, num_list)
                    num_list.append([x, y])
                else:
                    # 如果测量序号比上一次小，则表示该组信号是新的一组信号。
                    num_list.append([x, y])
            else:
                num_list.append([x, y])
        for number in num_list:
            print(number[0], number[1])
    except:
        break