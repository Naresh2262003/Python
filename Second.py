import numpy as np

# Part (a): Compute mean, standard deviation, and variance along the second axis
array_a = np.random.randint(0, 100, size=(4, 5))  # Random 2D array with integers
print("Original Array:")
print(array_a)
mean_a = np.mean(array_a, axis=1)
std_a = np.std(array_a, axis=1)
var_a = np.var(array_a, axis=1)
print("Mean along the second axis:", mean_a)
print("Standard Deviation along the second axis:", std_a)
print("Variance along the second axis:", var_a)

# Part (b): Get indices of sorted elements of a given array
B = np.array([56, 48, 22, 41, 78, 91, 24, 46, 8, 33])
sorted_indices = np.argsort(B)
print("Original Array B:", B)
print("Indices of sorted elements:", sorted_indices)

# Part (c): Create a 2D array and reshape it based on user inputs
m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))
array_c = np.random.randint(1, 100, size=(m, n))
print("Original Array:")
print(array_c)
print("Shape of the array:", array_c.shape)
print("Type of the array:", type(array_c))
print("Data type of the elements:", array_c.dtype)
reshaped_array = array_c.reshape(n, m)
print("Reshaped Array:")
print(reshaped_array)

# Part (d): Test for zero, non-zero, and NaN elements
array_d = np.array([0, 2, 0, np.nan, 5, 0, 7, np.nan])
zero_indices = np.where(array_d == 0)[0]
non_zero_indices = np.where(array_d != 0)[0]
nan_indices = np.where(np.isnan(array_d))[0]
print("Original Array:", array_d)
print("Indices of zero elements:", zero_indices)
print("Indices of non-zero elements:", non_zero_indices)
print("Indices of NaN elements:", nan_indices)