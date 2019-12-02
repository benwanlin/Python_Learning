# while True:
#     try:
#         def checking(num_list, num):
#             if sum(num_list) == num:
#                 return True
#             else:
#                 for i in num_list:
#                     if sum(num_list) - i == num:
#                         return True
#             return False
#
#
#         num_list = list(set(int(i) for i in input().strip().split()))
#         if checking(num_list, 24):
#             print("true")
#         else:
#             print("false")
#     except:
#         break

def helper(arr, item):
    if item < 1:
        return False
    if len(arr) == 1:
        return arr[0] == item
    for i in range(len(arr)):
        # print(arr[:i], arr[i+1:])
        L = arr[:i] + arr[i+1:]
        print(L)
        v = arr[i]
        if helper(L, item-v) or helper(L, item+v) or helper(L, item*v) or helper(L, item/v):
            print("***********", L, v)
            return True
    return False
while True:
    try:
        arr = list(map(int, input().split(' ')))
        if helper(arr, 24):
            print("true")
        else:
            print("false")
    except:
        break