days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = 1901
day_of_week = 2  # Tuesday
month = 0       # start from Feb since we've already considered Jan

count_sundays = 0
while not (year == 2000 and month == 10):
    day_of_week += days_in_month[month]

    # check for leap year
    if month == 1:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            day_of_week += 1
    
    day_of_week %= 7
    if day_of_week == 0:
        count_sundays += 1

    month += 1
    if month == 12:
        year += 1
        month = 0

print(count_sundays)