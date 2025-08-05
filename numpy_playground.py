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
# 3. Reshaping arrays
# -------------------------------
# Reshape the 1D array into a 2D array (2 rows, 5 columns)
reshaped = arr.reshape(2, 5)
print("Reshaped to 2x5:\n", reshaped)

# -------------------------------
# 4. Broadcasting
# -------------------------------
# Add 10 to every element using broadcasting
broadcasted = arr + 10
print("After broadcasting (add 10):", broadcasted)

# -------------------------------
# 5. Mathematical operations
# -------------------------------
# Square each element
squared = arr ** 2
print("Squared elements:", squared)