# Task

# In this challenge, the task is to debug the existing code to successfully execute all provided test files.
# Consider that vowels in the alphabet are a, e, i, o, u and y.
# Function score_words takes a list of lowercase words as an argument and returns a score as follows:
# The score of a single word is 2 if the word contains an even number of vowels.
# Otherwise, the score of this word is 1.
# The score for the whole list of words is the sum of scores of all words in the list.
# Debug the given function score_words such that it returns a correct score.
# Your function will be tested on several cases by the locked template code.

# Input Format
# The input is read by the provided locked code template. In the first line, there is a single integer n
# denoting the number of words. In the second line, there are n space-separated lowercase words.

# Constraints
# 1 <= n <= 20
# Each word has at most 20 letters and all letters are English lowercase letters

# Output Format
# The output is produced by the provided and locked code template. It calls function score_words
# with the list of words read from the input as the argument and prints the returned score to the output.

# Sample Input 0
# 2
# hacker book

# Sample Output 0
# 4

# Sample Input 1
# 3
# programming is awesome

# Sample Output 1
# 4

# Solution:
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))