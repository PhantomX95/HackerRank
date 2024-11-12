# Given an array of integers and a positive integer k, determine the number of (i, j) pairs where i<j and ar[i] + ar[j] is divisible by k.

# Example
# ar = [1, 2, 3, 4, 5, 6]
# k = 5

# Three pairs meet the criteria: [1, 4], [2, 3], and [4, 6].

# Function Description
# Complete the divisibleSumPairs function in the editor below.
# divisibleSumPairs has the following parameter(s):
#   * int n: the length of array ar
#   * int ar[n]: an array of integers
#   * int k: the integer divisor
# Returns
# - int: the number of pairs

# Input Format
# The first line contains 2 space-separated integers, n and k.
# The second line contains n space-separated integers, each a value of arr[i].

# Constraints
# 2 <= n <= 100
# 1 <= k <= 100
# 1 <= ar[i] <= 100

# Sample Input
# STDIN           Function
# -----           --------
# 6 3             n = 6, k = 3
# 1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]

# Sample Output
#  5

# Solution:
import os

def divisibleSumPairs(n, k, ar):
    divisible = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                divisible += 1
    return divisible

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
