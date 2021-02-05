
# 2. Calories Burned
# Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
# uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

total = 0

print("*" * 80)
print("...amount of colories lost in 30 minutes...".capitalize().center(80,"#"))
print("*" * 80)
print('\n')

counter = 0

for colory in range(5,30+1, 5):

  total_colory = colory * 4.2

  total += total_colory

  print(f"the total colories will lost in {colory} minutes are {total_colory:.1f}".capitalize())

print(f"the total colories will lost in 30 minutes are {total}")

