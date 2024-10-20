# Task

# Given a year, determine whether it is a leap year. If it is a leap year,
# return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
# It is only necessary to complete the is_leap function.

# Input Format
# Read year, the year to test.

# Constraints
# 1900 <= year <= 10 power 5

# Output Format
# The function must return a Boolean value (True/False). Output is handled by the provided code stub.

# Sample Input 0
# 1990

# Sample Output 0
# False

# Solution:
def is_leap(year):
    return True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False

year = int(input())
print(is_leap(year))