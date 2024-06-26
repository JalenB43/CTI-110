# Jalen Bowens
# 4/18/24
# PH4HW1
# the program will use a loop. Also, after displaying score average (after dropping lowest score) , the program is to display a letter grade for the calculated average.

choice = 'yes'
while choice.lower() == 'yes':
    num = int(input("Enter the number of grades you would like to add up: "))
    grade_list=[]
    for i in range(1,num + 1):
        grade = float(input("Enter grade #" + str(i) + ": "))
        while grade < 0 or grade > 100:
            print("Invalid, retry!")
            print("Grade must be between 1 and 100")
            grade = float(input("Enter grade #" + str(i) + " again: "))
        grade_list.append(grade)
    lowest=min(grade_list)
    grade_list.remove(lowest)
    ave=sum(grade_list)/len(grade_list)
    if ave>=90:
        letter="A"
    elif ave>=80:
        letter="B"
    elif ave>=70:
        letter="C"
    elif ave>=60:
        letter="D"
    else:
        letter="F"
                
    print("")
    print("")
    print("")
         
    print("-"*14,"Results","-"*14)
    print("Lowest Score : ",lowest)
    print("Modified List : ", grade_list)
    print("Scores Average : ",format(ave,".2f"))
    print("Grade       : ",letter)
    print("-"*35)
    choice = input("Would you like to run the program again? Enter yes or no: ")
    print("Program has exited!")
