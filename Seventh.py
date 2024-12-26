import pandas as pd

# Creating the DataFrame
data = {
    "Name": ["Mudit Chauhan", "Seema Chopra", "Rani Gupta", "Aditya Narayan", "Sanjeev Sahni",
             "Prakash Kumar", "Ritu Agarwal", "Akshay Goel", "Meeta Kulkarni", "Preeti Ahuja",
             "Sunil Das Gupta", "Sonali Sapre", "Rashmi Talwar", "Ashish Dubey", "Kiran Sharma", "Sameer Bansal"],
    "Birth_Month": ["December", "January", "March", "October", "February", "December", "September",
                    "August", "July", "November", "April", "January", "June", "May", "February", "October"],
    "Gender": ["M", "F", "F", "M", "M", "M", "F", "M", "F", "F", "M", "F", "F", "M", "F", "M"],
    "Pass_Division": ["III", "II", "I", "I", "II", "III", "I", "I", "II", "II", "III", "I", "III", "II", "II", "I"]
}

df = pd.DataFrame(data)

# Part a: Perform one-hot encoding
df_encoded = pd.get_dummies(df, columns=["Gender", "Pass_Division"], prefix=["Gender", "Pass_Div"])

# Part b: Sort the DataFrame by Birth Month
# Define the correct order for months
month_order = ["January", "February", "March", "April", "May", "June", "July", 
               "August", "September", "October", "November", "December"]

# Convert 'Birth_Month' to a categorical type with the defined order
df_encoded["Birth_Month"] = pd.Categorical(df_encoded["Birth_Month"], categories=month_order, ordered=True)

# Sort the DataFrame by the 'Birth_Month' column
df_sorted = df_encoded.sort_values("Birth_Month").reset_index(drop=True)

# Display the final DataFrame
print(df_sorted)
