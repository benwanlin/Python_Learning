while True:
    try:
        import re
        wildcard_string = input().strip()
        string = input().strip()

        wildcard_string = wildcard_string.replace("*", ".*").replace("?", ".?")

        # print(wildcard_string, string)

        pattern = re.compile(wildcard_string)
        # print(pattern)

        if pattern.search(string):
            print("true")
        else:
            print("false")

    except:
        break