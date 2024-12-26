import pandas as pd

# Sample DataFrames for illustration. Replace with reading from Excel files using `pd.read_excel()`.
data1 = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Time of joining": ["10:00", "10:15", "10:30"],
    "Duration": [30, 40, 50]
}
data2 = {
    "Name": ["Bob", "Charlie", "David"],
    "Time of joining": ["10:00", "10:20", "10:40"],
    "Duration": [40, 50, 30]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# a. Find names of students who attended the workshop on both days.
both_days = pd.merge(df1, df2, on="Name")
print("Students who attended both days:\n", both_days["Name"].tolist())

# b. Find names of all students who attended the workshop on either of the days.
either_days = pd.concat([df1, df2])
either_days_unique = either_days["Name"].unique()
print("Students who attended on either day:\n", list(either_days_unique))

# c. Merge the two dataframes row-wise and find the total number of records.
row_wise_merge = pd.concat([df1, df2], ignore_index=True)
print("Total number of records after row-wise merge:", len(row_wise_merge))

# d. Merge two dataframes and use 'Name' and 'Duration' as multi-row indexes. Generate descriptive statistics.
multi_index_merge = pd.concat([df1, df2]).set_index(["Name", "Duration"])
print("Descriptive statistics for multi-index dataframe:\n", multi_index_merge.describe())