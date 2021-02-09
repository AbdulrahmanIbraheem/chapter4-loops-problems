
"""9. Hotel Occupancy
Write a program that calculates the occupancy rate for a hotel. The program should
start by asking the user how many floors the hotel has. A loop should then iterate once
for each floor. In each iteration, the loop should ask the user for the number of rooms
on the floor and how many of them are occupied. After all the iterations, the program
should display how many rooms the hotel has, how many of them are occupied, how
many are unoccupied, and the percentage of rooms that are occupied. The percentage
may be calculated by dividing the number of rooms occupied by the number of rooms. 
'
NOTE: It is traditional that most hotels do not have a thirteenth floor. The loop in
this program should skip the entire thirteenth iteration'

nput Validation: Do not accept a value less than 1 for the number of floors. Do not
accept a number less than 10 for the number of rooms on a floor."""


floors = int( input("enter the number of floors the hotel has ".capitalize() ) )

total_rooms = 0
total_rooms_occupied = 0
number_of_rooms_unoccupied = 0
perventage_of_rooms_occupied = 0

for floor in range(1,floors+1):

  if floor == 13 or floors < 1:

    continue

  else:


    print("--------------------------------------------")
    print(f"floor number {floor}".capitalize() )

    rooms = int( input(f"enter the number of rooms in floor {floor} ".capitalize() ) )

    if rooms < 10:
      break
    rooms_occupied = int( input(f"enter the number of rooms occupied in floor {floor} ".capitalize() ) )
    
    if rooms_occupied > rooms :
      print("the number of occupied rooms should not be higher than the total rooms in the hotel ".capitalize())

      break

    else:

      total_rooms += rooms
      total_rooms_occupied += rooms_occupied
      number_of_rooms_unoccupied = total_rooms - total_rooms_occupied
      perventage_of_rooms_occupied = (rooms_occupied / rooms) * 100


 
print()   
print("----------------------------------------------------")
print(f"the number of rooms the hotel has are {total_rooms} rooms...".capitalize() )
print(f"the total number of rooms that occupied are {total_rooms_occupied} rooms...".capitalize())
print(f"the total number of rooms that unoccupied are {number_of_rooms_unoccupied} rooms...".capitalize() )
print(f"the percentage of the rooms that occupied is %{perventage_of_rooms_occupied:.2f}".capitalize() )
print("----------------------------------------------------")
