# 6. Distance Traveled
# The distance a vehicle travels can be calculated as follows:
# distance = speed * time
# For example, if a train travels 40 miles per hour for 3 hours, the distance traveled is
# 120 miles.
# Write a program that asks the user for the speed of a vehicle (in miles per hour) and how
# many hours it has traveled. The program should then use a loop to display the distance the
# vehicle has traveled for each hour of that time period. Here is an example of the output:
# What is the speed of the vehicle in mph? 40
# How many hours has it traveled? 3
# Hour Distance Traveled


speed_per_hour = int( input("enter the speed the vehicle travels ".title() ).strip() )
time_in_hour = int(input("enter the time the vehicle reavels in hours ".title() ).strip())

print()
print("-------------------------------------------------")
print("time in hours\t\t\t\t\tdistance traveled".title())
print("-------------------------------------------------")

if all([speed_per_hour >= 0, time_in_hour > 1]):
    
  for time in range(1,time_in_hour+1):

    distance = speed_per_hour * time

    print(f"||\t{str(time).zfill(2)}\t\t\t\t\t\t\t\t\t{str(distance).zfill(3)}     ||")

else:
   
  print(f"error, unasccbtibale a negative number for {speed_per_hour}".title() )
  print(f"error, {time_in_hour} should not be less than 1".title() )
  print("please, try again later".title() )

print("-------------------------------------------------")
