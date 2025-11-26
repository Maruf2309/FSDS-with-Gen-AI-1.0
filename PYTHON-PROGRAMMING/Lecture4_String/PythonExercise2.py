
"""
Excercise - 2: 
ATM Machine menu

1. Pin change 
2. balance check
3. withdraw 
4. Deposit
5. Exit
"""

menu = input(
    """
    Hi, Welcome the ATM Booth,
    Please Choose!
    1. Enter 1 for pin change
    2. Enter 2 for Balance check
    3. Enter 3 for Withdraw
    4. Enter 4 for Deposit
    5. Enter 5 for Exit

    """
)

# Logic Writing
if menu =="1":
    print("Pin Change")
elif menu =="2":
    print("Balance Check")
elif menu == "3":
    print("Withdaw")
elif menu =="4":
    print("Deposit")
else:
    print("Exit")
