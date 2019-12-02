while True:
    try:

        # 获取输入
        string = input().strip()

        # 整理成段落，放到变量中来
        string_paragraph = ''
        # 用last_i来记录上一个字符
        last_i = ''
        # 用is_within_quote变量来记录，是否处在引号里面
        is_within_quote = False
        for i in string:
            if i == ' ':
                # 如果是空格，并且不是在引号里面（is_within_quote是False），那就追加换行符
                if not is_within_quote:
                    string_paragraph += '\n'
                # 如果是空格，并且是在引号里面（is_within_quote是True），那就追加空格
                else:
                    string_paragraph += ' '
            elif i == '"':
                # 如果是引号，并且上一个字符是空格或者该引号是第一个字符，则设置is_within_quote为True，表示接下来的字符都在引号里面
                if last_i == ' ' or i == 0:
                    is_within_quote = True
                # 如果是引号，并且上一个字符是非空格并且该引号不是第一个字符，则设置is_within_quote为True，表示接下来的字符都在引号里面
                else:
                    is_within_quote = False
            else:
                # 普通情况，追加
                string_paragraph += i

            last_i = i

        print(string_paragraph.count("\n") + 1)
        print(string_paragraph)

    except:
        break