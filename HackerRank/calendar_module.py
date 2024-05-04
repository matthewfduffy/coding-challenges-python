"""
Task:  You are given a date. Your task is to find what the day is on that date.

Input Format: A single line of input containing the space separated month, day and year, respectively, in MMDDYYYY Format

Sample Input: 08 05 2015
Sample Output: Wednesday
"""
import calendar

prompt = input().split()
date_to_convert = []
days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

for i in range(len(prompt)):
    if prompt[i][0] == str(0):
        date_to_convert.append(prompt[i][1])
    else:
        date_to_convert.append(prompt[i])

day_num = calendar.weekday(int(date_to_convert[2]), int(date_to_convert[0]), int(date_to_convert[1]))
    
print(days[day_num])


# Option 2
import calendar
prompt = input()

def find_day(date):
    month, day, year = (int(i) for i in date.split(' '))
    day_number = calendar.weekday(year, month, day)

    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

    return days[day_number]

print(find_day(prompt))