# 4. Calories Burned
# Running on a particular treadmill you burn 3.6 calories per minute. Write a program that
# uses a loop to display the number of calories burned after 5, 10, 15, 20, 25, and 30 minutes.


print("time\t\t\t\t\tcalories burned".title())
print("----------------------------------------")

for number in range(5,30+1,5):

   CaloriesBurned = number * 3.6

   print(f"{number}\t\t\t\t\t\t\t {CaloriesBurned}")
