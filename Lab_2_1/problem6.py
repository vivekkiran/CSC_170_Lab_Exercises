"""
Program: problem6.py
Author: Vivek Kiran
Assignment #: Lab 2 Problem 6
Last Modified Date: 02/20/2020
Program Description:
This is program that reads a file and calculates the
sum of items sold for each item type
"""
GLASS_TYPE = "Glass"
FURNITURE_TYPE = "Furniture"
OTHER_TYPE = "Other articles"
MENTAL_TYPE = "Metal"
TANKS_TYPE = "Tanks"

glassCount = 0
glassSold = 0
furnitureCount = 0
furnitureSold = 0
otherCount = 0
otherSold = 0
metalCount = 0
metalSold = 0
tanksCount = 0
tanksSold = 0
sourceFile = open("business-price.csv", 'r')  # read the csv file
headers = sourceFile.readline().rstrip()
# headings = headers.split(",")
for line in sourceFile:
    row = line.rstrip()
    columns = row.split(",")
    description = columns[4]
    sold = int(columns[3])
    if description == GLASS_TYPE:
        glassCount = glassCount + 1
        glassSold = glassSold + sold
    elif description == FURNITURE_TYPE:
        furnitureCount = furnitureCount + 1
        furnitureSold = furnitureSold + sold
    elif description == OTHER_TYPE:
        otherCount = otherCount + 1
        otherSold = otherSold + sold
    elif description == MENTAL_TYPE:
        metalCount = metalCount + 1
        metalSold = sold + sold
    elif description == TANKS_TYPE:
        tanksCount = tanksCount + 1
        tanksSold = tanksSold + sold
print('{:20}'.format('Item Type'), '{:1}'.format('Number Sold'))
print('{:20}'.format(GLASS_TYPE), '{:10,}'.format(glassSold))
print('{:20}'.format(FURNITURE_TYPE), '{:10,}'.format(furnitureSold))
print('{:20}'.format(OTHER_TYPE), '{:10,}'.format(otherSold))
print('{:20}'.format(MENTAL_TYPE), '{:10,}'.format(metalSold))
print('{:20}'.format(TANKS_TYPE), '{:10,}'.format(tanksSold))
