# Task

# Complete the insert function in your editor so that it creates a new Node(pass data as the Node constructor argument)
# and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added,
# return the reference to the  node.

# Note: The head argument is null for an empty list.

# Input Format
# The first line contains T, the number of elements to insert.
# Each of the next T lines contains an integer to insert at the end of the list.

# Output Format
# Return a reference to the head node of the linked list.

# Sample Input
# STDIN   Function
# -----   --------
# 4       T = 4
# 2       first data = 2
# 3
# 4
# 1       fourth data = 1

# Sample Output
# 2 3 4 1

# Solution:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
        new_data = Node(data)
        
        if not head:
            return new_data
        else:
            current = head
            while current.next:
                current = current.next
        current.next = new_data
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  