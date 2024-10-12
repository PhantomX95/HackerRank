# Task

# You are given a string S.
# Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.

# Input Format
# A single line containing the string S and integer value K separated by a space.

# Constraints
# 0 < K <= len(S)
# The string contains only UPPERCASE characters.

# Output Format
# Print the different combinations of string S on separate lines.

# Sample Input
# HACK 2

# Sample Output
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK

# Solution:
from itertools import combinations

string, length = input().split()
length = int(length)
for r in range(1, length + 1):
    for c in combinations(sorted(string), r):
        print(''.join(c))
