# Task

# You are given a date. Your task is to find what the day is on that date.

# Input Format
# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

# Constraints
# 2000 < year < 3000

# Output Format
# Output the correct day in capital letters.

# Sample Input
# 08 05 2015

# Sample Output
# WEDNESDAY

# Solution:
import calendar
month, day, year = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(year, month, day)].upper())
