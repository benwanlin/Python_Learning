while True:
    try:
        count, k = input().strip().split()
        print(" ".join([ str(j) for j in sorted([int(i) for i in input().strip().split()])[:int(k)]]))
    except:
        raise