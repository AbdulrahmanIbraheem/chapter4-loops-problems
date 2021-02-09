# 8. Math Tutor
# This program started in Programming Challenge 15 of Chapter 3 , and was modified
# in Programming Challenge 9 of Chapter 4 . Modify the program again so it displays a
# menu allowing the user to select an addition, subtraction, multiplication, or division
# problem. The final selection on the menu should let the user quit the program. After
# the user has finished the math problem, the program should display the menu again.
# This process is repeated until the user chooses to quit the program.
# Input Validation: If the user selects an item not on the menu, display an error message
# and display the menu again.


keep_going = input("do you want to keep going ".title() ).strip().lower()  

print("\n\n")
# print("welcome to the calculator".title() )

while any([keep_going == "yes", keep_going == "y"]):
  
  print("*" * 80)
  print("...welcome to the calculator...".title().center(80,"#") )
  print("*" * 80)
  print() 

  print("------------------------------------------")
  print("operators\t\t\t\t\tsymbols".title())
  print("------------------------------------------")

  print("addition\t\t\t\t\t\t{+}".capitalize() )
  print("subtraction\t\t\t\t\t\t{-}".capitalize() )
  print("multiplication\t\t\t\t\t{*}".capitalize() )
  print("divition\t\t\t\t\t\t{/}".capitalize() )
  print("------------------------------------------")

  operator = input("enter the operator ".capitalize() ).strip()

  if not operator in ['+', "-", "/", "*", "addition", "subtraction", "division", "multiplication"]:

    break
  
  else:

    number1 = float( input("enter the first number ".capitalize() ).strip() )
    number2 = float( input("enter the second number ".capitalize() ).strip() )
    
    if any([operator == '+', operator == "addition"]):

      sum = number1 + number2
      print(f"the sum is {sum}".title() ) 

      print("-------------------------------------------")  


    elif any([operator == "subtraction", operator == "-"]):

      sum = number1 - number2
      print(f"{number1} + {number2} = {sum}".title() ) 
    
      print("-------------------------------------------")

    elif any([operator == "multiplication", operator == "*"]):

      sum = number1 * number2

      print(f"{number1} * {number2} = {sum}".capitalize() ) 
      print("-------------------------------------------")


    elif any([operator == "division", operator == "/"]):

      sum = number1 / number2
      print(f"{number1} / {number2} = {sum}".capitalize() ) 
      print("-------------------------------------------")

     

    keep_going = input("do you want to keep going ".title() ).strip().lower()  
    print()
else:

   print("see you again".capitalize() )y
   
