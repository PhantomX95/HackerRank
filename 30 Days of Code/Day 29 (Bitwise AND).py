# Task

# Given set S = {1, 2, 3, ... , N}. Find two integers, A and B (where A < B), from set S such that the value of A&B is the maximum
# possible and also less than a given integer, K. In this case, & represents the bitwise AND operator.

# Function Description
# Complete the bitwiseAnd function in the editor below.

# bitwiseAnd has the following paramter(s):
# - int N: the maximum integer to consider
# - int K: the limit of the result, inclusive

# Returns
# - int: the maximum value of A&B within the limit.

# Input Format
# The first line contains an integer, T, the number of test cases.
# Each of the T subsequent lines defines a test case as 2 space-separated integers, N and K, respectively.

# Constraints
# 1 <= T <= 10^3
# 2 <= N <= 10^3
# 2 <= K <= N

# Sample Input
# STDIN   Function
# -----   --------
# 3       T = 3
# 5 2     N = 5, K = 2
# 8 5     N = 8, K = 5
# 2 2     N = 8, K = 5

# Sample Output
# 1
# 4
# 0

# Solution:
import os

def bitwiseAnd(N, K):
    max_bitwise = 0
    
    for i in range(1, N + 1):
        for j in range(1, i):
            bitwise = i & j
            if max_bitwise < bitwise < K:
                max_bitwise = bitwise
    return max_bitwise

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
