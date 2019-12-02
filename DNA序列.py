string = input().strip()
size = int(input().strip())

max = 0
max_string = ''
for i in range(0, len(string) - size + 1):
    print(i)
    count_tmp = string[i: i + size].count('G') + string[i: i + size].count('C')
    if count_tmp > max:
        max_string = string[i: i + size]
        max = count_tmp
print(max_string)