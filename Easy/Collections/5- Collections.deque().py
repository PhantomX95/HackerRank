# Task

# Perform append, pop, popleft and appendleft methods on an empty deque d.

# Input Format
# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.

# Constraints
# 0 < N <= 100

# Output Format
# Print the space separated elements of deque .

# Sample Input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# Sample Output
# 1 2

# Solution:
from collections import deque

d = deque()
for _ in range(int(input())):
    command = input().split()
    if len(command) == 1:
        getattr(d, command[0])()
    elif len(command) == 2:
        num = command[1]
        getattr(d, command[0])(num)

print(' '.join(d))
