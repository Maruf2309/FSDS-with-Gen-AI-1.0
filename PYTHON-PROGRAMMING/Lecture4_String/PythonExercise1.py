
"""
Excercise - 1: 
Find the minimun number from 3 given number
"""

num1 = int(input("Enter the first number: "))   # 50
num2 = int(input("Enter the second number: "))  # 60
num3 = int(input("Enter the third number: "))   # 70

if num1 < num2 and num1 < num3:
    print("Minimun Number is: ", num1)

elif num2 < num1 and num2 < num3:
    print("Minimun number is : ", num2)

else:
    print("Minimun number is: ", num3)
    