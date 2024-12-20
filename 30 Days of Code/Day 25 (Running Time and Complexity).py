# Task

# A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# Given a number, n, determine and print whether it is Prime or Not prime.

# Note: If possible, try to come up with a O(√n) primality algorithm, or see what sort of optimizations
# you come up with for an O(n) algorithm. Be sure to check out the Editorial after submitting your code.

# Input Format
# The first line contains an integer, T, the number of test cases.
# Each of the T subsequent lines contains an integer, n, to be tested for primality.

# Constraints
# 1 <= T <= 30
# 1 <= n <= 2 x 10^9

# Output Format
# For each test case, print whether n is Prime or Not prime on a new line.

# Sample Input
# 3
# 12
# 5
# 7

# Sample Output
# Not prime
# Prime
# Prime

# Solution:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    print("Prime" if is_prime(n) else "Not prime")