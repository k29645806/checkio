import calendar

def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """
    first_day = calendar.weekday(year,1,1)
    last_day = calendar.weekday(year,12,31)
    lst = [6,0,1,2,3,4,5]  # represtent from Sun to Sat
    index1 = lst.index(first_day)
    first_week = lst[index1:]
    lst.reverse()      # count back from the last day
    index2 = lst.index(last_day)
    last_week = lst[index2:]
    days2count = first_week + last_week

    days_name = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    number_of_days = [days2count.count(i) for i in range(7)]
    max_value = max(number_of_days)
    max_index = [i for i,j in enumerate(number_of_days) if j==max_value]
    result = [days_name[i] for i in max_index]
    return result

print most_frequent_days(56)
