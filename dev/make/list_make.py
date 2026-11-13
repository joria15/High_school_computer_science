"""
author: Anthony antczak
date: 10/17/2024
A make on lists!
"""
#input
import statistics

user_input = int(input("Enter the amount of students: "))
students = []
#processing
for i in range(user_input):
    grades = int(input("Enter the grade: "))
    students.append(grades)
num = max(students)
nums = min(students)
numss = sum(students)/user_input
numsss = statistics.median(students)
#output
print(num)
print(nums)
print(numss)
print(numsss)