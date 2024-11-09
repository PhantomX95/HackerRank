# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# 1. The elements of the first array are all factors of the integer being considered
# 2. The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

# Example
# a = [2, 6]
# b = [24, 36]

# There are two numbers between the arrays: 6 and 12.
# 6%2 = 0, 6%6 = 0, 24%6 = 0 and 36%6 = 0 for the first value.
# 12%2 = 0, 12%6 = 0 and 24%12 = 0, 36%12 = 0 for the second value. Return 2.

# Function Description
# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.
# getTotalX has the following parameter(s):
#   * int a[n]: an array of integers
#   * int b[m]: an array of integers

# Returns
#   * int: the number of integers that are between the sets

# Input Format
# The first line contains two space-separated integers, n and m, the number of elements in arrays a and b.
# The second line contains n distinct space-separated integers a[i] where 0 <= i < n.
# The third line contains m distinct space-separated integers b[j] where 0 <= j < m.

# Constraints
# 1 <= n, m <= 10
# 1 <= a[i] <= 100
# 1 <= b[j] <= 100

# Sample Input
# 2 3
# 2 4
# 16 32 96

# Sample Output
# 3

# Solution:
import math
import os
from functools import reduce

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def lcm_array(arr):
    return reduce(lcm, arr)

def gcd_array(arr):
    return reduce(math.gcd, arr)

def getTotalX(a, b):
    lcm_a = lcm_array(a)
    gcd_b = gcd_array(b)
    
    count = 0
    multiple = lcm_a
    
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
