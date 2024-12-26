import pandas as pd

# Creating the DataFrame
data = {
    'Name': ['Shah', 'Vats', 'Vats', 'Kumar', 'Vats', 'Kumar', 'Shah', 'Shah', 'Kumar', 'Vats'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'MonthlyIncome': [114000, 65000, 43150, 69500, 155000, 103000, 55000, 112400, 81030, 71900]
}

df = pd.DataFrame(data)

# a. Calculate and display familywise gross monthly income
family_income = df.groupby('Name')['MonthlyIncome'].sum()
print("Familywise Gross Monthly Income:")
print(family_income)

# b. Calculate and display the member with the highest monthly income in a family
highest_income_member = df.loc[df.groupby('Name')['MonthlyIncome'].idxmax()]
print("\nMember with the highest monthly income in each family:")
print(highest_income_member[['Name', 'Gender', 'MonthlyIncome']])

# c. Calculate and display monthly income of all members with income greater than Rs. 60000.00
high_income_members = df[df['MonthlyIncome'] > 60000]
print("\nMembers with monthly income greater than Rs. 60000:")
print(high_income_members[['Name', 'Gender', 'MonthlyIncome']])

# d. Calculate and display the average monthly income of the female members in the Shah family
shah_female_members = df[(df['Name'] == 'Shah') & (df['Gender'] == 'Female')]
average_income_shah_female = shah_female_members['MonthlyIncome'].mean()
print("\nAverage monthly income of female members in the Shah family:")
print(average_income_shah_female)
