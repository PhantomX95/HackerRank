# Task

# You are given a NXM integer array matrix with space separated elements (N = rows and M = columns).
# Your task is to print the transpose and flatten results.

# Input Format
# The first line contains the space separated values of N and M.
# The next N lines contains the space separated elements of M columns.

# Output Format
# First, print the transpose array and then print the flatten.

# Sample Input
# 2 2
# 1 2
# 3 4

# Sample Output
# [[1 3]
#  [2 4]]
# [1 2 3 4]

# Solution:
import numpy as np

N, M = map(int, input().split())
lst=[]

for i in range(N):
    a = list(map(int, input().split()))
    lst.append(a)

arr = np.array(lst)
print(np.transpose(arr))
print(arr.flatten())