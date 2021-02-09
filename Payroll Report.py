# 15. Payroll Report
# Write a program that displays a weekly payroll report. A loop in the program should
# ask the user for the employee number, gross pay, state tax, federal tax, and FICA withholdings. The loop will terminate when 0 is entered for the employee number. After the
# data is entered, the program should display totals for gross pay, state tax, federal tax,
# FICA withholdings, and net pay.
# Programming Challenges 295
# Input Validation: Do not accept negative numbers for any of the items entered. Do
# not accept values for state, federal, or FICA withholdings that are greater than the
# gross pay. If the sum state tax + federal tax + FICA withholdings for any employee is
# greater than gross pay, print an error message and ask the user to reenter the data for
# that employee.

print("*" * 80)
print("   welcome to the weekly Payroll Repor   ".capitalize().center(80,"#"))
print("*" * 80)


number_of_employee = int( input("enter the number of emploee ".capitalize() ).strip() )

for employee in range(1,number_of_employee+1):
  
  print("-------------------------------------------------")
  print(f"the weekly report for the employee number {employee}".capitalize() )
  
  
  employee_number = int( input("enter the employee number ".capitalize () ).strip() )

  if employee_number == 0:

    break

  else:

    gross_pay = float( input("enter the gross pay $".capitalize() ).strip() )
    state_tax = float( input("enter the state tax ".capitalize( ) ).strip() )
    federal_tax = float( input("enter the federal tax ".capitalize( )).strip() )
    FICA_withholdings = float( input("enter the FICA withholdings ".capitalize() ).strip() )

    if any([gross_pay < 0, state_tax < 0, federal_tax < 0, FICA_withholdings < 0]):

      print("the values can not be a negative".capitalize() )

      break
    
    else:

      total_state_tax = (gross_pay * state_tax)  
      total_federal_tax = (gross_pay * federal_tax)
      total_FICA_withholdings = (gross_pay * FICA_withholdings)


    if total_federal_tax + total_state_tax + total_FICA_withholdings > gross_pay:

      print(f"error, please reenter the datat for emploee {employee}".capitalize() )
      break

    else:

      print(f"the rest of the gross pay for the employee {employee} is ${gross_pay - (total_federal_tax + total_state_tax + total_FICA_withholdings)}".capitalize() )

    
