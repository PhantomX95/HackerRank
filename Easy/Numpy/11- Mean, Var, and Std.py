# Task

# You are given a 2-D array of size NXM.
# Your task is to find:

# 1. The mean along axis 1
# 2. The var along axis 0
# 3. The std along axis None

# Input Format
# The first line contains the space separated values of N and M.
# The next N lines contains M space separated integers.

# Output Format
# First, print the mean.
# Second, print the var.
# Third, print the std.

# Sample Input
# 2 2
# 1 2
# 3 4

# Sample Output
# [ 1.5  3.5]
# [ 1.  1.]
# 1.11803398875

# Solution:
import numpy as np

N, M = map(int, input().split())
lst = []

for i in range(N):
    lst.append(list(map(int, input().split())))

arr = np.array(lst)

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
np.set_printoptions(legacy='1.13')
std = np.std(arr, axis=None)
print(std if std == 0.0 else f"{std:.11f}")