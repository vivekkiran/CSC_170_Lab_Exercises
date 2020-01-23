"""
Program: problem2.py
Author: Vivek Kiran
Assignment #: Lab Exercise 2
Last Modified Date: 01/23/2020
Program Description:
Program to find Monthly Income from Annual Income and Convert it into Yen and Euros and determine if it is above the national median income
"""
NATIONAL_MEDIAN_INCOME_DOLLARS = 61000.00
RATE_OF_EURO_PER_DOLLAR = 109.45
RATE_OF_YEN_PER_DOLLAR = 0.90

familyYearlyIncome = float(input("Enter your Family Yearly Income: "))
monthlyIncomeInDollars = familyYearlyIncome/12
monthlyIncomeInEuro = monthlyIncomeInDollars * RATE_OF_EURO_PER_DOLLAR
monthlyIncomeInYen = monthlyIncomeInDollars * RATE_OF_YEN_PER_DOLLAR
print("Monthly Family Income In Dollars: %.2f" % monthlyIncomeInDollars)
print("Monthly Family Income in Euro: %.2f " % monthlyIncomeInEuro)
print("Monthly Family Income in Yen: %.2f " % monthlyIncomeInYen)
if familyYearlyIncome > NATIONAL_MEDIAN_INCOME_DOLLARS:
    print "Family income is above the national median income: ", True
else:
    print "Family income is above the national median income: ", False
