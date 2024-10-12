# Task

# You are given a space separated list of integers. If all the integers are positive,
# then you need to check if any integer is a palindromic integer.

# Input Format
# The first line contains an integer N. N is the total number of integers in the list.
# The second line contains the space separated list of N integers.

# Constraints
# 0 < N < 100

# Output Format
# Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

# Sample Input
# 5
# 12 9 61 5 14 

# Sample Output
# True

# Solution:
N, list_nums = int(input()), list(map(str, input().split()))
print(True if all(int(n) > 0 for n in list_nums) and any(n == n[::-1] for n in list_nums) else False)
