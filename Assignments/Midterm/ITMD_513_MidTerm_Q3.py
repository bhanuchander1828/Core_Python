'''
ITMD 513 : MidTerm- Q3 - Bhanu kureti
Summary : This program will import the student.csv file and perform basic operations mentioned in question
'''

# Importing the modules
import numpy as np
import pandas as p
import scipy as s
import matplotlib.pyplot as plt
import csv
import statistics as st

''' Import the student datset'''
with open('/Users/bhanuchanderkureti/Python_Projects_Anaconda/Student_grades.csv', 'r') as S:
    Student_grades = list(csv.reader(S, delimiter=','))

'''Converting student dataset in to numPy array'''
Student_grades = np.array(Student_grades[1:], dtype=np.float)  # skips the header [1:]

print("\nDispaly number of Students in dataset")
print("\nThere are", Student_grades.shape[0], "students in the dataset")


print("\nDisplay numbers of rows and columns")
print(Student_grades.shape)


print("\nDispaly datatype for dataset")
print(Student_grades.dtype)

Student_OverPer = Student_grades[:, 31]
print(Student_OverPer)

print("\nDispaly min score of percentages")
print(Student_grades[:, 31].min())

print("\nDispaly max score of percentages")
print(Student_grades[:, 31].max())

print("\nDispaly mean score of percentages")
print(Student_grades[:, 31].mean())

print("\nDispaly median score of percentages")
print(st.median(Student_grades[:, 31]))

print("\nDispaly std of percentages")
print(Student_grades[:, 31].std())

print("\nDispaly mode of percentages")
print(st.mode(Student_grades[:, 31]))

print("\nDispaly 25th percentile of percentages")
print("25th percentile : ",
      np.percentile(Student_grades[:, 31], 25))

print("\nDispaly 75th percentile of percentages")
print("75th percentile  : ",
      np.percentile(Student_grades[:, 31], 75))


# Assigning  zeros to variables
i = 0
A = 0
B = 0
C = 0
D = 0
F = 0
l = len(Student_grades[:, 31])
while i < l:
    if Student_grades[i, 31] >= 90.00:
        A += 1
    elif Student_grades[i, 31] >= 80.00:
        B += 1
    elif Student_grades[i, 31] >= 70.00:
        C += 1
    elif Student_grades[i, 31] >= 60.00:
        D += 1
    else:
        F += 1
    i += 1

print("\nDispaly number of students received grades mentioned below respectively")
grade = [A, B, C, D, F]
for i in grade:
    print(i)

# Creating a pie chart of Grades
grades = [A, B, C, D, F]
grade = ['A Grade', 'B Grade', 'C Grade', 'D Grade', 'F Grade']
plt.pie(grades, labels=grade, startangle=45, autopct='%.1f%%')
plt.title('Student Grade Percentages')
plt.show()
