while True:
    try:
        a = input()
        b = input()
        if len(a)>len(b):
            a, b = b, a
        lcs = ''
        for i in range(len(a)):
            for j in range(i, len(a)):
                temp = a[i:j+1]
                if b.find(temp)<0:
                    break
                elif len(lcs)<len(temp):
                    lcs = temp
        print(lcs)
    except:
        break