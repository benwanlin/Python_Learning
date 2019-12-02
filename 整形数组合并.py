while True:
    try:
        count1, list1, count2, list2 = int(input().strip()), list(map(int, input().strip().split())), int(input().strip()), list(map(int, input().strip().split()))
        print(''.join([str(i) for i in sorted(list(set(list1 + list2)))]))
    except:
        break