# while True:
#     try:
#
#         user_score_dict = {}
#         count = int(input().strip())
#         reverse = input().strip()
#         for i in range(count):
#             user, score = input().strip().split()
#             if score in user_score_dict.keys():
#                 user_score_dict[score].append(user)
#             else:
#                 user_score_dict[score] = [user]
#
#         # print(user_score_dict)
#         if reverse == '0':
#             for i in sorted(user_score_dict.keys(), reverse=True):
#                 for j in sorted(user_score_dict[i], reverse=False):
#                     print(j + " " + str(i))
#         else:
#             for i in sorted(user_score_dict.keys(), reverse=False):
#                 for j in sorted(user_score_dict[i], reverse=True):
#                     print(j + " " + str(i))
#
#     except:
#         break

while True:
    try:
        n = int(input())
        flag1 = input()
        flag = True if flag1 == 0 else False
        arr = []
        for i in range(n):
            s = input().strip()
            arr.append(s)
        # print(arr)
        arr1 = sorted(arr, key=lambda x: int(x.split()[1]), reverse=flag)
        for i in arr1:
            print(i)
    except:
        break