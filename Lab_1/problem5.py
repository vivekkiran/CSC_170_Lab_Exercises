"""
Program: problem5.py
Author: Vivek Kiran
Assignment #: Lab Exercise 5
Last Modified Date: 01/23/2020
Program Description:
Program for Calculating Fibonacci Sequence with input from user to calculate number of terms
"""

numberOfFibonacciTerms = int(input("Enter Number of Fibonacci Terms to Calculate: "))


def fibonacci_formula(n):
    if n <= 1:
        return n
    else:
        return fibonacci_formula(n - 1) + fibonacci_formula(n - 2) # the nth term is the sum of (n-1)th and (n-2)th term


# check if the number of terms is valid
if numberOfFibonacciTerms <= 0:
    print("***Please enter a positive integer***")
else:
    print("Fibonacci sequence:")
    for i in range(numberOfFibonacciTerms):
        print(fibonacci_formula(i))