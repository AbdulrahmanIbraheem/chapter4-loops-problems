 

# 6. Miles to Kilometers Table
# Write a program that displays a table of distances in miles and their equivalent distances in
# kilometers, rounded to 2 decimal places. One mile is equivalent to 1.60934 kilometers. The
# table should be generated using a loop, and should include values in 10 mile increments from
# 10 to 80.

print("Distance in miles \t\t\tDistance in Killograms")
print("----------------------------------------------------")
for distances in range(10,80+1,10):

  distance_in_kg = distances *   1.60934

  print(f"{distances}\t\t\t\t\t\t\t\t{distance_in_kg:.2f}")

