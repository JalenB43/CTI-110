# Jalen Bowens
 # 3/5/24
 # P2HW1
 # For this assignment you will create a program that does some basic math on numbers that are entered

print("This program calculates and displays travel expenses")
print("")
budget =int(input('Enter Budget: '))
print("")
location=input('Enter your destination: ')
print("")
gas = int(input('Approximate amount of gas money: '))
print("")
accomodations = int(input('Approximate amount of money for accomodations: '))
print("")
food= int(input('Approximate amount of money for food: '))
print("")
print("------------Travel Expenses------------")
#user_num2+user_num3+user_num4
print("Location:       ",str(location))
print("Initial Budget:","$",float(budget))
print("Fuel:          ","$",float(gas))
print("Accomadations:","$",float(accomodations))
print("Food:         ","$",float(food))

print("----------------------------------------")

remaining_balance = (budget - gas - accomodations - food)
print("Remaining Balance: ","$",float(remaining_balance))


