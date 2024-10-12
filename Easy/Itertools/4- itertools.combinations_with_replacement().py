# Task

# You are given a string S.
# Your task is to print all possible size K replacement combinations of the string in lexicographic sorted order.

# Input Format
# A single line containing the string K and integer value  separated by a space.

# Constraints
# 0 < K <= len(S)
# The string contains only UPPERCASE characters.

# Output Format
# Print the combinations with their replacements of string S on separate lines.

# Sample Input
# HACK 2

# Sample Output
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

# Solution:
from itertools import combinations_with_replacement

string, repeat = input().split()
repeat = int(repeat)

result = list(combinations_with_replacement(sorted(string), repeat))
print('\n'.join(sorted(''.join(x) for x in result)))
