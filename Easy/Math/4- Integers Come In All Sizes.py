# Task

# Read four numbers, a, b, c, and d, and print the result of a power b + c power d.

# Input Format
# Integers , , , and  are given on four separate lines, respectively.

# Constraints
# 1 <= a <= 1000
# 1 <= b <= 1000
# 1 <= c <= 1000
# 1 <= d <= 1000

# Output Format
# Print the result of a power b + c power d on one line.

# Sample Input
# 9
# 29
# 7
# 27

# Sample Output
# 4710194409608608369201743232  

# Solution:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(pow(a, b) + pow(c, d))
