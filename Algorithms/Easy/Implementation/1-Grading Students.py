# HackerLand University has the following grading policy:
#   * Every student receives a grade in the inclusive range from 0 to 100.
#   * Any grade less than 40 is a failing grade.

# Sam is a professor at the university and likes to round each student's grade according to these rules:
#   * If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
#   * If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

# Examples
#   * grade = 84 round to 85 (85 - 84 is less than 3)
#   * grade = 29 do not round (result is less than 40)
#   * grade = 57 do not round (60 - 57 is 3 or higher)
# Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.

# Function Description
# Complete the function gradingStudents in the editor below.
# gradingStudents has the following parameter(s):
#   * int grades[n]: the grades before rounding

# Returns
#   * int[n]: the grades after rounding as appropriate

# Input Format
# The first line contains a single integer, n, the number of students.
# Each line i of the n subsequent lines contains a single integer, grade[i].

# Constraints
# 1 <= n <= 60
# 0 <= grade[i] <= 100

# Sample Input 0
# 4
# 73
# 67
# 38
# 33

# Sample Output 0
# 75
# 67
# 40
# 33

# Solution:
import os

def gradingStudents(grades):
    rounded_grades = []
    
    for grade in grades:
        if grade >= 38:
            next_multi_5 = (grade // 5 + 1)* 5
            if next_multi_5 - grade < 3:
                grade = next_multi_5
            
        rounded_grades.append(grade)
    return rounded_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
