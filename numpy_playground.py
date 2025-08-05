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

# Compute element-wise multiplication with another array
other = np.arange(10, 20)
multiplied = arr * other
print("Element-wise multiplication:", multiplied)

# -------------------------------
# 6. Statistical operations
# -------------------------------
# Mean of the array
mean_val = np.mean(arr)
print("Mean value:", mean_val)

# Standard deviation
std_val = np.std(arr)
print("Standard deviation:", std_val)

# Maximum and minimum
max_val = np.max(arr)
min_val = np.min(arr)
print("Max:", max_val, "Min:", min_val)

# 7. Boolean indexing
# -------------------------------
# Find elements greater than 5
greater_than_five = arr[arr > 5]
print("Elements > 5:", greater_than_five)

# -------------------------------
# 8. Random number generation
# -------------------------------
# Generate a 3x3 array of random numbers between 0 and 1
random_array = np.random.rand(3, 3)
print("Random 3x3 array:\n", random_array)

# -------------------------------
# 9. Save and load arrays
# -------------------------------
# Save the array to a file
np.save("my_array.npy", arr)

# Load the array back
loaded_arr = np.load("my_array.npy")
print("Loaded array from file:", loaded_arr)