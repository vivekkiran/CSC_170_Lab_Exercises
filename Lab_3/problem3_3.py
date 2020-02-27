"""
Program: problem3_3.py
Author: Vivek Kiran
Assignment #: Lab 3 Problem 3_1
Last Modified Date: 02/27/2020
Program Description:
This program checks the number of BME Courses offered

"""
import csv

dict = {}
courseList = []
defaultCount = 0

courseOffered = open("course_list.csv", "r")
studentEnrollment = open("student_classes.csv", "r")

headers = courseOffered.readline().rstrip()
studentEnrollmentHeaders = studentEnrollment.readline().rstrip()

for columns in csv.reader(courseOffered, quotechar='"', delimiter=',',
                          quoting=csv.QUOTE_MINIMAL, skipinitialspace=True):
    dict[columns[0]] = defaultCount
for columns in csv.reader(studentEnrollment, quotechar='"', delimiter=',',
                          quoting=csv.QUOTE_MINIMAL, skipinitialspace=True):
    courseList.append(columns[1])
    courseList.append(columns[2])
    courseList.append(columns[3])
for courseName in dict:
    for courses in courseList:
        if courseName in courses:
            dict[courseName] = dict[courseName] + 1
#print(dict)
print('{:20}'.format('Course'), '{:1}'.format('Enrollment'))
for courseName in dict:
    print('{:20}'.format(courseName), '{:1}'.format(dict[courseName]))
