"""
Program: problem7_1.py
Author: Vivek Kiran
Assignment #: Lab 2 Problem 7_1
Last Modified Date: 02/20/2020
Program Description:
This is program that calculates weighted student CGPA, assigns letter grade and penalty, takes inputs from user
"""

GPA_SUM = 0
gradeCounter = 0
numberOfGrades = int(input("How many grades do you want to enter? "))

while gradeCounter < numberOfGrades:
    gradeCounter = gradeCounter + 1
    gradeInput = int(input("Enter the grade for Subject " + str(gradeCounter) + ": "))
    GPA_SUM = GPA_SUM + gradeInput
print("Total Grades Entered: ", gradeCounter)
print("Average Grade: ", round(GPA_SUM / numberOfGrades, 2))
