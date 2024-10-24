# Task

# Your local library needs your help! Given the expected and actual return dates for a library book,
# create a program that calculates the fine (if any). The fee structure is as follows:

# 1. If the book is returned on or before the expected return date, no fine will be charged (i.e.:fine=0) .
# 2. If the book is returned after the expected return day but still within the same calendar month and year
#    as the expected return date, fine = 15 Hacktos x (the number of days late).
# 3. If the book is returned after the expected return month but still within the same calendar year as the expected
#    return date, the fine = 500 Hacktos x (the number of mounths late).
# 4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hacktos.

# Example
# d1, m1 y1 = 12312014 returned date
# d2, m2, y2 = 112015 due date
# The book is returned on time, so no fine is applied.
# d1, m1, y1 = 112015 returned date
# d2, m2, y2 = 12312014 due date

# The book is returned in the following year, so the fine is a fixed 10000.

# Input Format
# The first line contains 3 space-separated integers denoting the respective day, mounth, and year
# on which the book was actually returned.
# The second line contains 3 space-separated integers denoting the respective day, mounth, and year
# on which the book was expected to be returned (due date).

# Constraints
# 1 <= D <= 31
# 1 <= M <= 12
# 1 <= Y <= 3000
# It is guaranteed that the dates will be valid gregorian calendar dates

# Output Format
# Print a single integer denoting the library fine for the book received as input.

# Sample Input
# STDIN       Function
# -----       --------
# 9 6 2015    day = 9, month = 6, year = 2015 (date returned)
# 6 6 2015    day = 6, month = 6, year = 2015 (date due)

# Sample Output
# 45

# Solution:
def calculate_fine(date_returned, date_due):
    '''
    calculate the fine, the date must be in this format:
    dd/mm/yyyy
    '''
    day_r, mounth_r, year_r = date_returned
    day_d, mounth_d, year_d = date_due
    fine = 0
    
    if year_r == year_d:
        if mounth_r == mounth_d:
            if day_r > day_d:
                fine = (day_r - day_d)* 15
        elif mounth_r > mounth_d:
            fine = (mounth_r - mounth_d)* 500
    elif year_r > year_d:
        fine = 10000
    
    return fine

if __name__ == '__main__':
    date_returned = list(map(int, input().split()))
    date_due = list(map(int, input().split()))
    fine = calculate_fine(date_returned, date_due)
    print(fine)