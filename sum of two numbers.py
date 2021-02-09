 
# 1. Sum of Numbers
# Write a program that asks the user for a positive integer value. The program should use
# a loop to get the sum of all the integers from 1 up to the number entered. For example,
# if the user enters 50, the loop will find the sum of 1, 2, 3, 4, … 50.
# Input Validation: Do not accept a negative starting number.

number = int(input("enter an integer number ".capitalize() ).strip() )

total = 0

if not number < 0:

  for num in range(1,number+1):

    total += num 

print(total)

