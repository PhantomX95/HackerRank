# Task

# You are given a 2-D array with dimensions NXM.
# Your task is to perform the sum tool over axis 0 and then find the product of that result.

# Input Format

# The first line of input contains space separated values of N and M.
# The next N lines contains M space separated integers.

# Output Format
# Compute the sum along axis 0. Then, print the product of that sum.

# Sample Input
# 2 2
# 1 2
# 3 4

# Sample Output
# 24

# Solution:
import numpy as np

N, M = map(int, input().split())
array = np.array([input().split() for i in range(N)], dtype=int)
print(np.prod(np.sum(array, axis=0)))
