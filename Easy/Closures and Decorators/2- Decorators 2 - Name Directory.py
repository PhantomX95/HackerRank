# Let's use decorators to build a name directory! You are given some information about N people.
# Each person has a first name, last name, age and sex. Print their names in a specific format sorted by
# their age in ascending order i.e. the youngest person's name should be printed first.
# For two people of the same age, print them in the order of their input.

# For Henry Davids, the output should be:

# Mr. Henry Davids
# For Mary George, the output should be:

# Ms. Mary George

# Input Format
# The first line contains the integer N, the number of people.
# N lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

# Constraints
# 1 <= N <= 10

# Output Format
# Output N names on separate lines in the format described above in ascending order of age.

# Sample Input
# 3
# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F

# Sample Output
# Mr. Mike Thomson
# Ms. Andria Bustle
# Mr. Robert Bustle

# Solution:
import operator

def person_lister(f):
    def inner(people):
        data = sorted(people, key=lambda person: int(person[2]))
        sorted_people = []
        
        for person in data:
            sorted_people.append(f(person))
        return sorted_people

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')