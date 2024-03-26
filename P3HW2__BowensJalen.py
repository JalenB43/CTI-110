 # Jalen Bowens

 # 3/26

  # P3HW2

  # You are to create a program that is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay)

employee=input("Enter employee's name: ")
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


print(hours)
print(payr)
print(OT)
print(OT_pay)
print(reg_pay)
print(gross)
