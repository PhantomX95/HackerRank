# Task

# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.

# Input Format
# The first line contains integer n, the number of elements in the set s.
# The second line contains n space separated elements of set s.
# All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.

# Constraints
# 0 < n < 20
# 0 < N < 20

# Output Format
# Print the sum of the elements of set s on a single line.

# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5

# Sample Output
# 4

# Solution:
n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    user_order = list(input().split())
    if len(user_order) == 1:
        getattr(s, user_order[0])()
    elif len(user_order) == 2:
        num = int(user_order[1])
        if num in s:
            getattr(s, user_order[0])(num)

print(sum(s))
