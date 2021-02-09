# 12. Celsius to Fahrenheit Table
# In Programming Challenge 10 of Chapter 3you were asked to write a program that
# converts a Celsius temperature to Fahrenheit. Modify that program so it uses a loop
# to display a table of the Celsius temperatures 0–20, and their Fahrenheit equivalents.


temperature_in_celsius = int( input("enter the temperature in Celsius system ".capitalize() ).strip() )
print()

print("-----------------------------------------------")
print("Celsius\t\t\t\t\t\t\t\tFahrenheit")
print("-----------------------------------------------")
for number in range(1,temperature_in_celsius+1):

  temperature_in_Fahrenheit = float(number) * 9/5 + 32

  print(f"{str(number).zfill(2)}\t\t\t\t\t\t\t\t\t\t{temperature_in_Fahrenheit}")
