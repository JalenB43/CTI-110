 # Jalen Bowens

 # 4/18/24

  # P4HW2

  #The program however will calculate gross pay for multiple employees, determined by user
totOT = 0
totreg_pay = 0
totgross = 0
count = 0
employee=input("Enter employee's"+ " name or 'Done' to terminate: ")
while employee !="Done":
    hours=float(input("Enter number of hours " + employee +" worked: "))
    payr=float(input("Enter " + employee + "'s pay rate: "))
    print("-"*37)
    print("Employee Name:",employee)
    print("")
    print('Hours     Pay Rate     Overtime    OverTime Pay     RegHour Pay  Gross Pay ')
    print("-"*80)
    if hours>40:
        reg_hours = 40
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

    totOT= totOT + OT_pay
    totreg_pay = totreg_pay + reg_pay
    totgross = totgross + gross
    count = count + 1

    print(hours," "*10,payr," "*10,OT," "*10,OT_pay," "*10,reg_pay," "*10,gross)
    print()
    print()
    print()
    employee=input("Enter employee's"+ " name or 'Done' to terminate: ")

print("Total amount of employees entered: ", str(count))
print("Total amount paid for overtime: ", str(format(totOT,'.2f')))
print("Total amount paid for regular hours: ", str(format(totreg_pay,'.2f')))
print("Total amount paid in gross: ", str(format(totgross,'.2f')))
print("Program has exited")

##print(payr)
##print(OT)
##print(OT_pay)
##print(reg_pay)
##print(gross)
