# Task

# You are given a polynomial P of a single indeterminate (or variable), x.
# You are also given the values of x and k. Your task is to verify if P(x) = k.

# Constraints
# All coefficients of polynomial P are integers.
# x and y are also integers.

# Input Format
# The first line contains the space separated values of x and k.
# The second line contains the polynomial P.

# Output Format
# Print True if P(x) = k. Otherwise, print False.

# Sample Input
# 1 4
# x**3 + x**2 + x + 1

# Sample Output
# True

# Solution:
x, result = map(int, input().split())
val = eval(input())
print(True if val == result else False)
