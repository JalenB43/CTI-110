# Jalen Bowens
 # 2/20/24
 # P1HW2
 # For this assignment you will create a program that does some basic math on numbers that are entered

print("This program calculates and displays travel expenses")
print("")
user_num = int(input('Enter Budget: '))
print("")
location_var=input('Enter your destination: ')
print("")
user_num2 = int(input('Approximate amount of gas money: '))
print("")
user_num3 = int(input('Approximate amount of money for accomodations: '))
print("")
user_num4 = int(input('Approximate amount of money for food: '))
print("")
print("------------Travel Expenses------------")
#user_num2+user_num3+user_num4
print("Location:",location_var)
print("Initial Budget:",user_num)
print("")
print("Fuel:", user_num2)
print("Accomadation:", user_num3)
print("Food:", user_num4)
print("")
print("Remaining Balance:", user_num-user_num2-user_num3-user_num4)


