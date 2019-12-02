while True:
    try:
        string = input().strip()
        list_rst = []
        list_duplicated = []
        for i in string:
            if i in list_rst and i not in list_duplicated:
                list_rst.remove(i)
                list_duplicated.append(i)
            elif i in list_duplicated:
                continue
            else:
                list_rst.append(i)
        if list_rst:
            print(list_rst[0])
        else:
            print('-1')

    except:
        break