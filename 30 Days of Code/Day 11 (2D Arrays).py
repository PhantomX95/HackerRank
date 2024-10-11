# Context
# Given a 6 x 6 2D Array, A:

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

# Task
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

# Example
# In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.

# Input Format
# There are 6 lines of input, where each line contains 6 space-separated integers that describe the 2D Array A.

# Constraints
# -9 <= A[i][j] <= 9
# 0 <= i, j <= 5

# Output Format

# Print the maximum hourglass sum in A.

# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output

# 19

# Solution:
def maximum_hourglass(lst):
    hour_glasses = []
    for n in range(len(lst) - 2):
        for m in range(len(lst[0]) - 2):
            up_raw = lst[n][m] + lst[n][m + 1] + lst[n][m + 2]
            middle = lst[n + 1][m + 1]
            down_raw = lst[n + 2][m] + lst[n + 2][m + 1] + lst[n + 2][m + 2]
            hour_glasses.append(up_raw + middle + down_raw)

    return max(hour_glasses)

if __name__ == '__main__':
    lst = []

    for _ in range(6):
        lst.append(list(map(int, input().rstrip().split())))
    print(maximum_hourglass(lst))