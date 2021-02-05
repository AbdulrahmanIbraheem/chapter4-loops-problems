
years = int(input("enter the number of years ".capitalize() ).strip() ) 

total = 0

for year in range(1,years+1):
  
  print()
  print(f"number of year {year}")
  print("----------------------")
 
  for month in range(1,12+1):

    amount_rainfaill = int(input(f"how much of rainfain in inches for month {month}: ".capitalize()))

    total += amount_rainfaill
    average = total / month
  print(f"\nthe total amount of rainfaill in the year {year} is {total} inches/nthe average is {average}".capitalize() )
     
