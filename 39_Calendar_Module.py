# Question Link
# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true


import calendar

day, month, year = map(int, input().split())


day_index = calendar.weekday(year, day, month)
if day_index == 0:
    print('MONDAY')
if day_index == 1:
    print('TUESDAY')
if day_index == 2:
    print('WEDNESDAY')
if day_index == 3:
    print('THURSDAY')
if day_index == 4:
    print('FRIDAY')
if day_index == 5:
    print('SATURDAY')
if day_index == 6:
    print('SUNDAY')
