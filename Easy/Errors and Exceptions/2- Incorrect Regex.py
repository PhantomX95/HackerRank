# You are given a string S.
# Your task is to find out whether S is a valid regex or not.

# Input Format
# The first line contains integer T, the number of test cases.
# The next T lines contains the string S.

# Constraints
# 0 < T < 100

# Output Format
# Print "True" or "False" for each test case without quotes.

# Sample Input
# 2
# .*\+
# .*+

# Sample Output
# True
# False

# This solution must run on Pypy 3:
import re

for _ in range(int(input())):
    try:
        print(bool(re.compile(input())))
        
    except re.error:
        print(False)
