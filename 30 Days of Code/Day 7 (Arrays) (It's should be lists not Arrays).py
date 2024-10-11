# Task
# Given an list, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

# Example
# A = [1, 2, 3, 4]

# Print 4 3 2 1. Each integer is separated by one space.

# Input Format

# The first line contains an integer, N (the size of our list).
# The second line contains N space-separated integers that describe list 's elements.

# Constraints
# 1 <= N <= 1000
# 1 <= A[i] <= 10000. where A[i] is the i integer in list

# , where  is the  integer in the list.
# Output Format

# Print the elements of list A in reverse order as a single line of space-separated numbers.

# Sample Input

# 4
# 1 4 3 2
# Sample Output

# 2 3 4 1

# Solution:
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    print(' '.join(map(str, reversed(arr))))