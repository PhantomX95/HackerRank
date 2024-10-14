# Task

# You are given two integer arrays, A and B of dimensions NXM.
# Your task is to perform the following operations:

# 1. Add (A + B)
# 2. Subtract (A - B)
# 3. Multiply (A * B)
# 4. Integer Division (A / B)
# 5. Mod (A % B)
# 6. Power (A ** B)

# Note
# There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

# Input Format
# The first line contains two space separated integers, N and M.
# The next N lines contains M space separated integers of array A.
# The following N lines contains M space separated integers of array B.

# Output Format
# Print the result of each operation in the given order under Task.

# Sample Input
# 1 4
# 1 2 3 4
# 5 6 7 8

# Sample Output
# [[ 6  8 10 12]]
# [[-4 -4 -4 -4]]
# [[ 5 12 21 32]]
# [[0 0 0 0]]
# [[1 2 3 4]]
# [[    1    64  2187 65536]] 

# Solution:
import numpy as np

np.set_printoptions(legacy='1.13')
N, M = map(int, input().split())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

print(np.add(A, B))
print(np.subtract(A, B))
print(np.multiply(A, B))
print(np.floor_divide(A, B))
print(np.mod(A, B))
print(np.power(A, B))