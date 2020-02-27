"""
Program: problem3_2.py
Author: Vivek Kiran
Assignment #: Lab 3 Problem 3_2
Last Modified Date: 02/27/2020
Program Description:
This program checks the number of BME Courses offered

"""
import csv

BMECount = 0
substring = "BME"
courseList = []
sourceFile = open("course_list.csv","r")
headers = sourceFile.readline().rstrip()
for columns in csv.reader(sourceFile, quotechar='"', delimiter=',',
                          quoting=csv.QUOTE_MINIMAL, skipinitialspace=True):
    courseList.append(columns[0])
for text in courseList:
    if substring in text:
        BMECount += 1
print("Number of BME courses is "+ str(BMECount))