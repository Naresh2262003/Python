import pandas as pd
import numpy as np

# Sample dataset for demonstration
data = {
    "Date": ["2023-01-01", "2023-01-02", "2023-01-04", "2023-01-06"],
    "Sales": [100, 200, None, 400],
    "Category": ["A", "A", "B", "B"],
    "Region": ["North", "South", "North", "South"]
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

print("Original Dataset:")
print(df)

# a. Compute mean of Sales grouped by Category
mean_sales_by_category = df.groupby("Category")["Sales"].mean()
print("\nMean Sales by Category:")
print(mean_sales_by_category)

# b. Fill missing dates with values from the previous non-missing date
full_date_range = pd.date_range(start=df["Date"].min(), end=df["Date"].max())
df_filled = df.set_index("Date").reindex(full_date_range).rename_axis("Date").reset_index()
df_filled["Sales"] = df_filled["Sales"].fillna(method="ffill")
print("\nDataset with Missing Dates Filled:")
print(df_filled)

# c. Convert a year-month string to dates
df_filled["YearMonth"] = df_filled["Date"].dt.to_period("M")
print("\nDataset with Year-Month Conversion:")
print(df_filled)

# d. Group by two columns (Category and Region) and sort within groups
grouped_sorted = df.groupby(["Category", "Region"]).agg({"Sales": "sum"}).sort_values(by="Sales", ascending=False)
print("\nGrouped and Sorted Results:")
print(grouped_sorted)

# e. Split dataset into groups with bin counts
sales_bins = pd.cut(df["Sales"].fillna(0), bins=3, labels=["Low", "Medium", "High"])
df["Sales_Bin"] = sales_bins
print("\nDataset with Sales Binned:")
print(df)
