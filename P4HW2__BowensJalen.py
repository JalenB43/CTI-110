 # Jalen Bowens

 # 4/18/24

  # P4HW2

  #The program however will calculate gross pay for multiple employees, determined by user

employee=input("Enter employee's"+ " name or 'Done' to terminate: ")
while employee !="Done":
    hours=float(input("Enter number of hours worked: "))
    payr=float(input("Enter employee's pay rate: "))
    print("-"*37)
    print("Employee Name:",employee)
    print("")
    print('Hours     Pay Rate     Overtime    OverTime Pay     RegHour Pay    Gross Pay ')
    print("-"*80)
    if hours>40:
     reg_pay=payr*40
     OT=hours-40
     OT_rate=1.5*payr
     OT_pay=OT*OT_rate
     gross=reg_pay+OT_pay
    else:
     OT=0
     OT_pay=0
     reg_pay=payr*hours
     gross=reg_pay+OT_pay
    print(hours," "*5,payr," "*5,OT," "*5,OT_pay," "*5,reg_pay," "*5,gross)
    print()
    print()
    print()
employee=input("Enter employee's"+ " name or 'Done' to terminate: ")
while employee !="Done":
 hours=float(input("Enter number of hours worked: "))
 payr=float(input("Enter employee's pay rate: "))

 employee=input("Enter employee's"+ " name or 'Done' to terminate: ")
 print("Program has exited")

##print(payr)
##print(OT)
##print(OT_pay)
##print(reg_pay)
##print(gross)
