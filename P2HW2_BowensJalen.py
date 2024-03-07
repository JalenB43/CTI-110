 #Jalen Bowens

 #3/5/2024

 #P2HW2

 #Assignment assess student understanding of Lists
my_list=[]
Module_1=float(input("Enter Module 1 Test Score: "))
my_list.append(Module_1)
Module_2=float(input("Enter Module 2 Test Score: "))
my_list.append(Module_2)
Module_3=float(input("Enter Module 3 Test Score: "))
my_list.append(Module_3)
Module_4=float(input("Enter Module 4 Test Score: "))
my_list.append(Module_4)
Module_5=float(input("Enter Module 5 Test Score: "))
my_list.append(Module_5)
Module_6=float(input("Enter Module 6 Test Score: "))
my_list.append(Module_6)
print("")
print("------------Results------------")
lowest=min(my_list)
print(f"Lowest Grade:     {lowest:.2f}")
highest=max(my_list)
print(f"Highest Grade:     {highest:.2f}")
length=len(my_list)
sum1=sum(my_list)
print(f"Sum of Grades:     {sum1:.2f}")
ave=sum1/length
print(f"Average:     {ave:.2f}")
print("---------------------------------------")
