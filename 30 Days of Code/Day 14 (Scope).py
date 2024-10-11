# Task
# Complete the Difference class by writing the following:

# A class constructor that takes an array of integers as a parameter and saves it to the __elements instance variable.
# A computeDifference method that finds the maximum absolute difference between any 2 numbers in __elements and stores it in the maximumDifference instance variable.

# Input Format

# You are not responsible for reading any input from stdin. The locked Solution class in the editor reads in 2 lines of input. The first line contains N,
# the size of the elements array. The second line has N space-separated integers that describe the __elements array.

# Constraints
# 1 <= N <= 10
# 1 <= __elements[i] <= 100, where 0 <= i <= N - 1

# Output Format

# You are not responsible for printing any output; the Solution class will print the value of the maximumDifference
# instance variable.

# Sample Input

# STDIN   Function
# -----   --------
# 3       __elements[] size N = 3
# 1 2 5   __elements = [1, 2, 5]
# Sample Output

# 4

# Solution:
class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        mx = max(self.__elements)
        mn = min(self.__elements)
        maximum = mx - mn
        
        self.maximumDifference = maximum
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)