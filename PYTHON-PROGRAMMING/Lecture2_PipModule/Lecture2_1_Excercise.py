
"""
Excercise - 1
Find the minimum number from 3 given number
"""

num1 = int(input("Enter the first number: "))  # input return str
num2 = int(input("Enter the second number: ")) 
num3 = int(input("Enter the third number: ")) 

# print(num1, num2, num3)

if num1<num2 and num1<num3:  # and logical operator
    print ("Minimum number is : ", num1)

elif num2<num1 and num2<num3:
    print("Minimum is : ", num2)

else:
    print("Minimum number is : ", num3)