# Task
# You are given two classes, Person and Student, where Person is the base class and Student is the derived class.
# Completed code for Person and a declaration for Student are provided for you in the editor.
# Observe that Student inherits all the properties of Person.

# Complete the Student class by writing the following:

# A Student class constructor, which has  parameters:
# A string, .
# A string, .
# An integer, .
# An integer array (or vector) of test scores, .
# A char calculate() method that calculates a Student object's average and returns
# the grade character representative of their calculated average:

#     Grading Scale
# Letter      Average(a)
#   O       90 <= a <= 100
#   E        80 <= a < 90
#   A        70 <= a < 80
#   P        55 <= a < 70
#   D        40 <= a < 55
#   T           a < 40


# Input Format

# The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments.
# It also calls the calculate method which takes no arguments.
# The first line contains firstName, lastName, and idNumber, separated by a space.
# The second line contains the number of test scores. The third line of space-separated integers describes .

# Constraints
# 1 <= length of firstName, length of lastName <= 10
# length of idNumber = 7
# 0 <= score <= 100

# Output Format

# Output is handled by the locked stub code. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

# Sample Input

# Heraldo Memelli 8135627
# 2
# 100 80
# Sample Output

#  Name: Memelli, Heraldo
#  ID: 8135627
#  Grade: O

# Solution:
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        self.avg = sum(scores) / len(scores)
    
    def calculate(self):
        if 90 <= self.avg <= 100:
            return 'O'
        elif 80 <= self.avg < 90:
            return 'E'
        elif 70 <= self.avg < 80:
            return 'A'
        elif 55 <= self.avg < 70:
            return 'P'
        elif 40 <= self.avg < 55:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())