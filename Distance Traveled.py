
speed = float( input("ener the speed travel per hours ".capitalize() ).strip() )

time_travel = float(input("enter the time travels in hours ".capitalize() ).strip() )

print()
print("Hour(S)\t\tDistance Travels")
print("--------------------------")
print()

for hour in range(1,int(time_travel+1) ):
  distance = speed * hour

  print(f"{hour}\t\t\t\t{int(distance)} ")
