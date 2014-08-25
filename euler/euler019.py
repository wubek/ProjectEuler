# author wukat
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def create_months_list():
    return ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def create_length_of_months_dict():
    return {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31}

def check_if_leap_year(year):
    return True if year % 4 == 0 and year % 400 != 0 else False

def get_feb_length(year):
    return 29 if check_if_leap_year(year) else 28

def count_sundays_on_first_day_of_month_between_dates():
    sundays = 0
    first_day = 366 % 7
    lengths = create_length_of_months_dict()
    for year in range(1901, 2001):
        lengths["Feb"] = get_feb_length(year)
        for month in create_months_list():
            first_day += lengths[month] % 7
            if first_day % 7 == 0:
                sundays += 1
    if first_day % 7 == 0: # we've checked also 1 Jan 2001
        sundays -= 1
    return sundays

if __name__ == "__main__":
    print(count_sundays_on_first_day_of_month_between_dates())