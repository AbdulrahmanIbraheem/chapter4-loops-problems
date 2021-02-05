
tuition_increase = 0.03
tuition = 8000
tuition_total = 0
years = 5

print('tuition_total\t\t\tyears')
print('-------------------------------')
for years in range (1, years + 1):
    
  tuition +=   tuition_increase * tuition
  print(f"years\t\t\t\t\t{tuition * 2:.2f}")

