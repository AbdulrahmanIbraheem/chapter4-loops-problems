# 3. Ocean Levels
# Assuming the ocean’s level is currently rising at about 1.5 millimeters per year, write
# a program that displays a table showing the number of millimeters that the ocean will
# have risen each year for the next 25 years.


print("year\t\t\t\t\t\tocean level".title() )
print("---------------------------------------")
total = 0

for year in range(1,25+1):

  rasing_level = 1.5 * year

  total += rasing_level

  print(f"{year}\t\t\t\t\t\t\t\t{rasing_level}")
print("\n\n")
print(total)
