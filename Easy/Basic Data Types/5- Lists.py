# Consider a list (list = []). You can perform the following commands:

# 1. insert i e: Insert integer e at position i.
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands
# where each command will be of the 7 types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

# Example
# N = 4
# append 1
# append 2
# insert 3 1
# print
#   * append 1: Append 1 to the list, arr = [1].
#   * append 2: Append 2 to the list, arr = [1, 2].
#   * insert 3 1: Insert 3 at index 1, arr = [1, 3, 2].
#   * print: Print the array.

# Output:
# [1, 3, 2]

# Input Format
# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints
#   * the elements added to the list must be integers. 

# Output Format
# For each command of type print, print the list on a new line.

# Sample Input 0
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output 0
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

# Solution:
if __name__ == '__main__':
    N = int(input())
    num_list = []

    while N:
        user_input = list(input().split())
        command = user_input[0]
        if command == 'insert':
            index = int(user_input[1])
            element = int(user_input[-1])
            num_list.insert(index, element)
            N -= 1
        elif command == 'print':
            print(num_list)
            N -= 1
        elif command == 'remove':
            value = int(user_input[1])
            num_list.remove(value)
            N -= 1
        elif command == 'sort':
            num_list.sort()
            N -= 1
        elif command == 'pop':
            num_list.pop()
            N -= 1
        elif command == 'reverse':
            num_list.reverse()
            N -= 1
        elif command == 'append':
            num = int(user_input[1])
            num_list.append(num)
            N -= 1