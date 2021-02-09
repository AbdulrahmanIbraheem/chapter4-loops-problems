# 13. The Greatest and Least of These
# Write a program with a loop that lets the user enter a series of integers. The user should
# enter −99 to signal the end of the series. After all the numbers have been entered, the
# program should display the largest and smallest numbers entered

list_numbers = []

while True:

 number = int( input("enter an integer number ".capitalize()).strip() )

 list_numbers.append(number)

 if number == -99:

   break


print("-----------------------------------------------------")
# print(f"the list of numbers are {list_numbers}".capitalize())
print(f"the largest number is {max(list_numbers)}".capitalize() )
print(f"the smallest number is {min(list_numbers)}".capitalize() )
