# 9. Ocean Levels
# Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
# application that displays the number of millimeters that the ocean will have risen each year
# for the next 25 years.

total = 0

for year in range(1,25+1):
  
  # milemiter += 1
  increasment = year * 1.6
  total += increasment

  print(f"the ocean will increase in year {year} is [ {increasment:.2f} ] milemeters".capitalize())

print(f"in 25 years will be {total} millimeters")
