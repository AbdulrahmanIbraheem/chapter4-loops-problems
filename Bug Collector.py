# prblem 1

total = 0

print("*" * 80)
print("total number of bug collected in 5 day".capitalize().center(80,"#"))
print("*" * 80)
print('\n')

for day in range(5):

  bugs_collected = int( input(f"enter the number of bugs collected in day {day + 1}: ".capitalize() ).strip())

  total += bugs_collected
print(f"the total number of bug collected in 5 days are {total} bugs".capitalize() )

