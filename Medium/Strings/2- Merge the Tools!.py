# Task


# There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'.
# The first substring is all 'A' characters, so u1 = 'A'.
# The second substring has all distinct characters, so u2 = 'BCA'.
# The third substring has 2 different characters, so u3 = 'DE'.
# Note that a subsequence maintains the original order of characters encountered.
# The order of characters in each subsequence shown is important.

# Function Description
# Complete the merge_the_tools function in the editor below.
# merge_the_tools has the following parameters:
#   * string s: the string to analyze
#   * int k: the size of substrings to analyze

# Prints
# Print each subsequence on a new line. There will be n/k of them. No return value is expected.

# Input Format
# The first line contains a single string, s.
# The second line contains an integer, k, the length of each substring.

# Constraints
# 1 <= n <= 10 power 4, where  is the length of 
# 1 <= k <= n 
# It is guaranteed that n is a multiple of k.

# Sample Input
# STDIN       Function
# -----       --------
# AABCAAADA   s = 'AABCAAADA'
# 3           k = 3

# Sample Output
# AB
# CA
# AD

# Solution:
def merge_the_tools(string, k):
    lst = list(string[i:i+k] for i in range(0, len(string), k))
    for S in lst:
        print(''.join(sorted(set(S), key=S.index)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)