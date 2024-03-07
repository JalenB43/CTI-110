# Jalen Bowens
 # 2/29
 # P2LAB2 
 # tests student's knowledge of how to write code that uses a dictionary to store user input and displays output to the user
 

automobiles_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
    }
automobiles_list = automobiles_dict
print("The keys in the dictionary are:")
print(*automobiles_list, sep=", ")
print()
automobile=input('Enter a vehicle to see its mpg: ')
print()
mpg=automobiles_dict.get(
    automobile)
print("The",automobile,"gets",mpg,"mpg.")
print()
miles = float(input("How many miles  will drive the " + automobile + "? "))
print()
gallons=miles/mpg
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {automobile} {miles:.1f} miles.")



