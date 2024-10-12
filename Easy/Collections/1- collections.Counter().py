# Task

# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay X amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money Raghu earned.

# Input Format

# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoe size desired by the customer and Xi, the price of the shoe.

# Constraints
# 0 < X < 10 power 3
# 0 < N <= 10 power 3
# 20 < Xi < 100
# 2 < shoe size < 20

# Output Format
# Print the amount of money earned by .

# Sample Input
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# Sample Output
# 200

# Solution:
from collections import Counter

num_prod = int(input())
stock = list(map(int, input().split()))
num_orders = int(input())
orders = map(tuple, (map(int, input().split())for _ in range(num_orders)))
dict_products = Counter(stock)
earned = 0

for order in orders:
    size, price = order
    if dict_products[size]:
        dict_products[size] -= 1
        earned += price
        
print(earned)

# without importing Counter
# num_prod = int(input())
# stock = list(map(int, input().split()))
# list_orders = []

# for _ in range(int(input())):
#     list_orders.append(tuple(map(int, (input().split()))))

# earned = 0
# for order in list_orders:
#     if order[0] in stock:
#         stock.remove(order[0])
#         earned += order[1]

# print(earned)
