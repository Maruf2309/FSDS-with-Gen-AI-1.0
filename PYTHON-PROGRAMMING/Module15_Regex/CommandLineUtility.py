# This will show comman line Utility

import argparse
import sys

def calculator(arge):
    if arge.o =='add':  # O:operation
        return arge.a + arge.b
    elif arge.o== 'sub':
        return arge.a - arge.b
    elif arge.o == 'mul':
        return arge.a * arge.b
    elif arge.o == 'div':
        if arge.b !=0:
            return arge.a / arge.b
        else:
            return "Error: Zero Division Error"
    else:
        return "Error: Invalid Operation"
    
parser = argparse.ArgumentParser()
parser.add_argument("--a", type=float, default=1.0) #-- mean comman line for understandi
parser.add_argument("--b", type=float, default=2.0)
parser.add_argument("--o", type=str, default='add')

args = parser.parse_args()
sys.stdout.write(str(calculator(args))) 



