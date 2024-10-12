# Task

# You are given a string S.
# Your task is to print all possible permutations of size K of the string in lexicographic sorted order.

# Input Format
# A single line containing the space separated string S and the integer value K.

# Constraints
# 0 < K <= len(S)

# The string contains only UPPERCASE characters.

# Output Format
# Print the permutations of the string  on separate lines.

# Sample Input
# HACK 2

# Sample Output
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH

# Solution:
from itertools import permutations
perm, num = input().split()

for chars in sorted(permutations(perm, int(num))):
    print(''.join(chars))
