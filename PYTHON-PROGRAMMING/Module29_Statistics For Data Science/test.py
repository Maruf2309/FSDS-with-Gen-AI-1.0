
# Check Python version
import sys
print("Python version:", sys.version)

# Check basic arithmetic
a = 5
b = 10
print("Addition:", a + b)
print("Multiplication:", a * b)

# Check list and loop
numbers = [1, 2, 3, 4, 5]
print("Numbers in list:")
for n in numbers:
    print(n, end=" ")
print()

# Check if NumPy is installed and working
try:
    import numpy as np
    arr = np.array(numbers)
    print("NumPy array:", arr)
    print("Mean of array:", np.mean(arr))
except ImportError:
    print("NumPy is not installed!")

# Check if pandas is installed and working
try:
    import pandas as pd
    df = pd.DataFrame({'Numbers': numbers})
    print("Pandas DataFrame:\n", df)
except ImportError:
    print("Pandas is not installed!")
