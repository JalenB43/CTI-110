#calculate a students average
##Desicion Structure

#gets the grades from user, adds together for total
#divide total by number of grades for average
#use average for letter grade

grade1 = int(input("Enter the first grade: "))
grade2 = int(input("Enter the second grade: "))
grade3 = int(input("Enter the third grade:" ))
grade4 = int(input("Enter the fourth grade:" ))
grade5 = int(input("Enter the fifth grade:" ))

total = grade1+grade2+grade3+grade4+grade5
ave=total/5
print(ave)

#figure out letter grade that corresponds with numeric grade
#use decision structure

if ave>=89.5:
    letter = "A"
    
else:
     if ave>=79.5:
        letter="B"
        
     else:
          if ave>=69.5:
             letter="C"
        
          else:
               if ave>=59.5:
                  letter ="D"

               else:
                   letter="F"
        
