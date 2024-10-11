# Task
# Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer
# denoting the maximum number of consecutive 1's in n's binary representation.
# When working with different bases, it is common to show the base as a subscript.

# Example
# n = 125

# The binary representation of  is . In base , there are  and  consecutive ones in two groups. Print the maximum, 5.

# Input Format

# A single integer, n.

# Constraints
# 1 <= n <= 10 power 6

# Output Format

# Print a single base-10 integer that denotes the maximum number of consecutive 1's in the binary representation of n.

# Sample Input 1

# 5
# Sample Output 1

# 1
# Sample Input 2

# 13
# Sample Output 2

# 2

# Solution:
def max_num_consecutive(n):
    binary = bin(int(n))[2:]
    repeated = 1
    max_num = 1

    for i in range(1, len(binary)):
        if binary[i] == binary[i - 1]:
            repeated += 1
            max_num = max(repeated, max_num)
        else:
            max(max_num, repeated)
            repeated = 1

    return max_num

if __name__ == '__main__':
    n = int(input().strip())
    print(max_num_consecutive(n))