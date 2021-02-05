# 11. Sleep Debt
# A “sleep debt” represents the di#erence between a person’s desirable and actual amount
# of sleep. Write a program that prompts the user to enter how many hours they slept each
# day over a period of seven days. Using 8 hours per day as the desirable amount of sleep,
# determine their sleep debt by calculating the total hours of sleep they got over the seven-day
# period and subtracting that from the total hours of sleep they should have got. If the user
# does not have a sleep debt, display a message expressing your jealousy




hours_of_sleep = 8
period = 7

total = 0


sleep_list = []
for day in range(1,8):

  sleep_hours = float( input(f"how many hours did you sleep in day {day}: ").strip() )

  total += sleep_hours
  
  Sleep_debt =  (hours_of_sleep * 7) - total

 
print(f"the total hours you need to sleep in 7 days is {hours_of_sleep * period} you slept {total} hour(s) the sleep debt is {Sleep_debt} hours")
