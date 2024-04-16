# Jalen Bowens
 # 4/16/24
 # P4LAB2
 # Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.
 
num1 = int(input())
num2 = int(input())

if num2 < num1:
    print("Second integer can't be less than the first.")
else:
    for i in range(num1, num2 + 1, 5):
        print(f'{str(i)}', end=' ')
    print()
