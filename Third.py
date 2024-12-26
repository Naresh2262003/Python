import pandas as pd
import numpy as np

# Step 1: Create a DataFrame with 3 columns and 50 rows of random numeric data
np.random.seed(42)  # For reproducibility
data = pd.DataFrame({
    'Column1': np.random.randint(1, 100, 50),
    'Column2': np.random.randint(1, 100, 50),
    'Column3': np.random.randint(1, 100, 50)
})

# Step 2: Replace 10% of the values with null values
num_nulls = int(data.size * 0.1)  # Calculate 10% of total values
null_indices = (np.random.randint(0, 50, num_nulls), np.random.randint(0, 3, num_nulls))

# Assign np.nan using .iloc for proper handling
for row, col in zip(*null_indices):
    data.iloc[row, col] = np.nan

print("DataFrame with null values:\n", data)

# a. Identify and count missing values
missing_values = data.isnull().sum().sum()
print("\nTotal missing values:", missing_values)

# b. Drop the column having more than 5 null values
data = data.dropna(axis=1, thresh=45)  # At least 45 non-null values (50 - 5 = 45)
print("\nDataFrame after dropping columns with more than 5 null values:\n", data)

# c. Identify the row label having the maximum sum and drop that row
row_sums = data.sum(axis=1)
max_sum_row = row_sums.idxmax()
data = data.drop(index=max_sum_row)
print("\nDataFrame after dropping the row with the maximum sum:\n", data)

# d. Sort the DataFrame based on the first column
data = data.sort_values(by='Column1')
print("\nDataFrame sorted by the first column:\n", data)

# e. Remove all duplicates from the first column
data = data.drop_duplicates(subset='Column1')
print("\nDataFrame after removing duplicates from the first column:\n", data)

# f. Find the correlation and covariance
correlation = data['Column1'].corr(data['Column2'])
covariance = data['Column2'].cov(data['Column3'])
print("\nCorrelation between Column1 and Column2:", correlation)
print("Covariance between Column2 and Column3:", covariance)

# g. Detect and remove outliers (using IQR method)
Q1 = data['Column2'].quantile(0.25)
Q3 = data['Column2'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data = data[(data['Column2'] >= lower_bound) & (data['Column2'] <= upper_bound)]
print("\nDataFrame after removing outliers from Column2:\n", data)

# h. Discretize the second column into 5 bins
data['Column2_binned'] = pd.cut(data['Column2'], bins=5, labels=False)
print("\nDataFrame with Column2 discretized into 5 bins:\n", data)
