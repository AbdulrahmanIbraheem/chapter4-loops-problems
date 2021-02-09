
# Membership Fees Increase
# A country club, which currently charges $2,500 per year for membership, has
# announced it will increase its membership fee by 4% each year for the next six years.
# Write a program that uses a loop to display the projected rates for the next six years

current_fee = 2500
yearl_inclreasment = 0.04
number_of_years = 6

print("years\t\t\t\t\t\t\tprice".title())
print("----------------------------------------")


for year in range(number_of_years):
  current_fee = (current_fee * yearl_inclreasment) + current_fee
  
  print(f"{str(year+1).zfill(2)}\t\t\t\t\t\t\t\t${current_fee:.2f}")
