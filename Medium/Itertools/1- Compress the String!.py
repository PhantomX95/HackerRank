# Task
# In this task, we would like for you to appreciate the usefulness of the groupby()
# function of itertools.
# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
# Replace these consecutive occurrences of the character 'c' with (X, c) in the string.
# For a better understanding of the problem, check the explanation.

# Input Format
# A single line of input consisting of the string S.

# Output Format
# A single line of output consisting of the modified string.

# Constraints
# All the characters of S denote integers between 0 and 9.
# 1 <= |S|<= 10 power 4

# Sample Input
# 1222311

# Sample Output
# (1, 1) (3, 2) (1, 3) (2, 1)

# Solution:
from itertools import groupby

for k, g in groupby(input()):
    print((len(list(g)), int(k)), end=" ")