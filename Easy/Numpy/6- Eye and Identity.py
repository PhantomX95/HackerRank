# Task

# Your task is to print an array of size NXM with its main diagonal elements as 1's and 0's everywhere else.

# Note
# In order to get alignment correct, please insert the line numpy.set_printoptions(legacy='1.13')
# below the numpy import.

# Input Format
# A single line containing the space separated values of N and M.
# N denotes the rows.
# M denotes the columns.

# Output Format
# Print the desired NXM array.

# Sample Input
# 3 3

# Sample Output
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

# Solution:
import numpy as np

np.set_printoptions(legacy='1.13')
N, M = map(int, input().split())
print(np.eye(N, M, k=0))