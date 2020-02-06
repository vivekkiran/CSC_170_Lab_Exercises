"""
Program: problem7.py
Author: Vivek Kiran
Assignment #: Lab Exercise 7
Last Modified Date: 02/06/2020
Program Description:
CGPA Calculator
"""

numberGrade = int(input("How many grade do you want to average:"))
sumGrade = 0
grade = float(input("Enter a grade: "))
for count in range (numberGrade):
    grade = float(input("Enter a grade:"))
    sumGrade+=grade
averageGrade = sumGrade/numberGrade

print("Average grade is:", averageGrade)