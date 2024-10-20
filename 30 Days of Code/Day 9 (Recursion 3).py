# Function Description
# Complete the factorial function in the editor below. Be sure to use recursion.

# factorial has the following paramter:

# int n: an integer
# Returns

# int: the factorial of n
# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

# Input Format

# A single integer, n (the argument to pass to factorial).

# Constraints
# 2 <= n <= 12
# Your submission must contain a recursive function named factorial.

# Sample Input

# 3
# Sample Output

# 6

# Solution:
import os
def factorial(n):
    return n * factorial(n - 1) if n != 1 else 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()