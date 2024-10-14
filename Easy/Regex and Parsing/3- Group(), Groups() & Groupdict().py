# Task

# You are given a string S.
# Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.

# Input Format

# A single line of input containing the string S.

# Constraints
# 1 < len(S) < 100

# Output Format

# Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

# Sample Input

# ..12345678910111213141516171820212223
# Sample Output

# 1

# Solution:
import re

repeating = re.search(r"([A-Za-z0-9])(?=\1)", input())
print(repeating.group() if repeating else -1)