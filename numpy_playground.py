import numpy as np

# -------------------------------
# 1. Create a NumPy array
# -------------------------------
# Create a 1D array of integers from 0 to 9
arr = np.arange(10)
print("Original array:", arr)

# -------------------------------
# 2. Indexing and slicing
# -------------------------------
# Get the first 5 elements
first_five = arr[:5]
print("First five elements:", first_five)

# Get every second element
every_second = arr[::2]
print("Every second element:", every_second)