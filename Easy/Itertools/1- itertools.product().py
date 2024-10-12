# Task

# You are given a two lists A and B. Your task is to compute their cartesian product AXB.

# Example
# A = [1, 2]
# B = [3, 4]

# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
# Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

# Input Format
# The first line contains the space separated elements of list A.
# The second line contains the space separated elements of list B.
# Both lists have no duplicate integer elements.

# Constraints
# 0 < A < 30
# 0 < B < 30

# Output Format
# Output the space separated tuples of the cartesian product.

# Sample Input
#  1 2
#  3 4

# Sample Output
#  (1, 3) (1, 4) (2, 3) (2, 4)

# Solution:
if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AxB = []
    
    for num in A:
        for number in B:
            AxB.append((num, number))
    
    for tup in AxB:
        print(tup, end=' ')
