while True:
    try:

        def get_n_th_date(year, month, date):
            month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
                month_list[1] = 29
            if month == 1:
                return date
            days = 0
            for i in range(month - 1):
                days = days + month_list[i]
            return days + date


        year, month, date = int(input().strip()), int(input().strip()), int(input().strip())
        print(get_n_th_date(year, month, date))

    except:
        break