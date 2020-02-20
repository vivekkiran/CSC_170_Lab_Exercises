"""
Program: problem7_2.py
Author: Vivek Kiran
Assignment #: Lab 2 Problem 7_2
Last Modified Date: 02/20/2020
Program Description:
This is program that calculates weighted student CGPA, assigns letter grade and penalty, reads and writes to a file
"""
import csv

GPA_SUM = 0
withdrawals = 0
credits = 0
gradePoints = 0
sourceFile = open("BME Student Grade.csv", 'r')  # read the csv file
headers = sourceFile.readline().rstrip()
gradeDict = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
}
for columns in csv.reader(sourceFile, quotechar='"', delimiter=',',
                          quoting=csv.QUOTE_MINIMAL, skipinitialspace=True):
    # row = line.rstrip()
    # columns = row.split(",")
    # print(columns[2])
    if columns[2] != '':
        credit = int(columns[2])
        credits = credits + credit
    gradePoints = gradeDict.get(columns[4])

print(credits)
print(gradePoints)

#     description = columns[4]
#     sold = int(columns[3])
# gradeCounter = 0
# numberOfGrades = int(input("How many grades do you want to enter? "))

# while gradeCounter < numberOfGrades:
#     gradeCounter = gradeCounter + 1
#     gradeInput = int(input("Enter the grade for Subject " + str(gradeCounter) + ": "))
#     GPA_SUM = GPA_SUM + gradeInput
# print("Total Grades Entered: ", gradeCounter)
# print("Average Grade: ", round(GPA_SUM / numberOfGrades, 2))
