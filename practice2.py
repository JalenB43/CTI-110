def main():
   #displayinfo()
   num=getnumber()
   tot=getTotalgrades(num)
   ave=calcAve(num,tot)
   letter=getLettergrade(ave)
   displayResults(number,total,average,letter)

def displayinfo():
    print ("Jalen Bowens")
    print ("4/25/24")
    print ("This program will calculate the average letter grade out a set of grades")
    print()
    



def getnumber():
    number=int(input("Enter number of grades to average: "))
    return number

def getTotalgrades(n):
    total=0
    for i in range(1,n + 1):
        grade=int(input("Enter grade # "+str(i)+": "))
        total+=grade
    return total

def calcAve(number,total):
    return total/number

def getLettergrade(ave):
    if ave>=89.5:
        letter= "A"
    elif ave>=79.5:
        letter="B"
    elif ave>=69.5:
        letter="C"
    elif ave>=59.5:
        letter="D"
    else:
        letter="F"
    return letter

def displayResults(n,t,a,l):
    print("Number of grades: ",n)
    print("Grade Total: ",t)
    print("Grade Average: ",a)
    print("Letter Grade: ",l)

        
        
        
main()

