# Task

# The National University conducts an examination of N students in X subjects.
# Your task is to compute the average scores of each student.
# Average = Sum of scores obtained in all subject by a student / Total number of subjects

# The format for the general mark sheet is:

# Student ID → ___1_____2_____3_____4_____5__               
# Subject 1   |  89    90    78    93    80
# Subject 2   |  90    91    85    88    86  
# Subject 3   |  91    92    83    89    90.5
#             |______________________________
# Average        90    91    82    90    85.5 

# Input Format
# The first line contains  and  separated by a space.
# The next  lines contains the space separated marks obtained by students in a particular subject.

# Constraints
# 0 < N <= 100
# 0 < X <= 100

# Output Format
# Print the averages of all students on separate lines.
# The averages must be correct up to  decimal place.

# Sample Input
# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5

# Sample Output
# 90.0 
# 91.0 
# 82.0 
# 90.0 
# 85.5        

# Solution:
nums_subjects, nums_scores = map(int, input().split())
list_scores = [map(float, input().split()) for i in range(nums_scores)]

for subject_score in zip(*list_scores):
    print(sum(subject_score) / nums_scores)
