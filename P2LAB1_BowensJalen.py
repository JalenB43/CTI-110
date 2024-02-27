# Jalen Bowens
# 2/27
# P2LAB1
# tests student's knowledge of how to write code that performs mathematical calculations and displays information to users
import math
radius=float(input("What is the radius of the circle? "))
diamater=2*radius
print("the diameter of the circle is", diamater)
circumference=2*3.14*radius
print(f"the circumference of the circle is {circumference:,.2f}")
area=3.14*math.pow(radius,2)
print(f"the area of the circle is {area:.2f}")
