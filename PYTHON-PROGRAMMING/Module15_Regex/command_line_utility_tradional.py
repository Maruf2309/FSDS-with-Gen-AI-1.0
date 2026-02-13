
# This is a tradional approach , next we will try to comman line utility in atomation

def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    
    elif operation =='subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b!=0:  # Any Number can not divided by ZERO,
            return a / b # Allow when b not equal to ZERO
        else:
            return "Error: Zero Division Error  "
        
    else:
        return "Error: Invalid Operation"  # return error if out of operation (+, -,*,/)
    
# This fun return something, so need to store in a variable
result = calculator(10, 5,'add')
print("Result: ",result)
        



