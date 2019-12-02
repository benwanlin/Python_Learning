# import _thread

# def child(tid):
#     print('Hello from thread', tid)
#
# def parent():
#     i = 0
#     while True:
#         i += 1
#         _thread.start_new_thread(child, (i,))
#         if input() == 'q': break
#
# parent()


while True:
    try:
        import threading

        arr = []


        def add_char(char):
            global arr
            arr.append(char)


        for _ in range(int(input().strip())):
            for i in ['A', 'B', 'C', 'D']:
                t = threading.Thread(target=add_char, args=(i, ))
                t.start()
                t.join()

        print(''.join(arr))

    except:
        break