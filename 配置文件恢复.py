while True:
    try:
        list_start = [
            "reset",
            "reset board",
            "board add",
            "board delet",
            "reboot backplane",
            "backplane abort"
        ]
        list_ans = [
            "reset what",
            "board fault",
            "where to add",
            "no board at all",
            "impossible",
            "install first"
        ]


        while True:
            string = input().strip()

            ans = ''
            for i in range(len(list_start)):
                if list_start[i].startswith(string):
                    if "reset".startswith(string) and string != '':
                        ans = "reset what"
                    elif ans == '':
                        ans = list_ans[i]
                    else:
                        ans = "unkown command"
                        break
            print(ans)
    except:
        break