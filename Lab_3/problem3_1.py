"""
Program: problem3_1.py
Author: Vivek Kiran
Assignment #: Lab 3 Problem 3_1
Last Modified Date: 02/27/2020
Program Description:
This program checks if the course is being offered

"""
import csv

courseList = []

sourceFile = open("course_list.csv", "r")
headers = sourceFile.readline().rstrip()
for columns in csv.reader(sourceFile, quotechar='"', delimiter=',',
                          quoting=csv.QUOTE_MINIMAL, skipinitialspace=True):
    courseList.append(columns[0])
courseId = input("Enter Course Id: ")
while len(courseId) > 0:
    if courseId in courseList:
        print(courseId + " is being offered")
    else:
        print(courseId + " is not being offered")
    courseId = input("Enter Course Id: ")

