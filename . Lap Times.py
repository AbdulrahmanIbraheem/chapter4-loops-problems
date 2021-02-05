

number_of_suden = int(input("enter the number of sutudent ").strip() )

number_of_test = int(input("enter the number of test ").strip() )

total = 0

for sudent in range(number_of_suden):
  
  print("\n")
  print("*" * 60)
  print(f"...S udent Number {sudent+1}...".center(60,"#"))
   # print("--")

  print("*" * 60)


  for test in range(number_of_test):

    print(f"test number {test+1}: ", end = '')

    scor = float(input())

    total += scor

  average = total / number_of_test

  print(f"the average of the student {sudent+1} is {average}")

  if average >= 90:

    print("your GPA is A")
  elif average >= 80:

    print("your GPA is A-")
  elif average >= 70:

    print("your GPA is B")
  
  elif average >= 60:

    print("your GPA is C")

