# Pandas DataFrame Operations: Slicing & Adding Columns

This script demonstrates core pandas techniques for slicing data and dynamically adding columns using a synthetic employee dataset.

```python
import pandas as pd
import numpy as np

# 1. Initialize the Sample DataFrame
data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'Finance'],
    'Base_Salary': [60000, 95000, 70000, 110000, 85000],
    'Performance_Score': [4.2, 3.8, 4.9, 4.5, 3.9]
}
df = pd.DataFrame(data)
df.set_index('Employee_ID', inplace=True)
print("Initial DataFrame:")
print(df, "\n" + "="*50 + "\n")

# ==========================================
# PART 1: SLICING TECHNIQUES
# ==========================================

print("--- 1.1 Column Slicing ---")
# Single Column (Series)
names = df['Name']
# Multiple Columns (DataFrame)
dept_salary = df[['Department', 'Base_Salary']]
print(dept_salary, "\n")

print("--- 1.2 Label-Based Slicing (.loc) ---")
# Slice specific rows by label and select a single column
alice_charlie_salary = df.loc[101:103, 'Base_Salary']
print(alice_charlie_salary, "\n")

print("--- 1.3 Position-Based Slicing (.iloc) ---")
# Slice first 3 rows and first 2 columns strictly by integer positions
first_chunk = df.iloc[0:3, 0:2]
print(first_chunk, "\n" + "="*50 + "\n")


# ==========================================
# PART 2: ADDING COLUMNS TECHNIQUES
# ==========================================

print("--- 2.1 Direct Assignment (In-Place) ---")
# Adding a scalar value
df['Is_Active'] = True
# Adding from a list matching row length
df['Location'] = ['New York', 'San Francisco', 'Chicago', 'Austin', 'Boston']
print(df[['Name', 'Is_Active', 'Location']], "\n")

print("--- 2.2 Functional Copy Creation (.assign) ---")
# Create a new DataFrame with calculated columns via method chaining
df_with_bonus = df.assign(
    Bonus=df['Base_Salary'] * 0.10,
    Total_Comp=lambda x: x['Base_Salary'] + (x['Base_Salary'] * 0.10)
)
print("New DataFrame Copy (df_with_bonus):")
print(df_with_bonus[['Name', 'Base_Salary', 'Bonus', 'Total_Comp']], "\n")

print("--- 2.3 Explicit Column Placement (.insert) ---")
# Insert a column at a specific index location in-place
df.insert(1, 'Email', ['alice@company.com', 'bob@company.com', 'charlie@company.com', 'david@company.com', 'eva@company.com'])
print(df, "\n")

print("--- 2.4 Conditional Assignment (.loc & np.select) ---")
# Single Condition: Set Tier 'Senior' if Base_Salary > 90000
df['Tier'] = 'Junior' # default
df.loc[df['Base_Salary'] > 90000, 'Tier'] = 'Senior'

# Multiple Conditions using numpy.select (Advanced)
conditions = [
    (df['Performance_Score'] >= 4.5),
    (df['Performance_Score'] >= 4.0) & (df['Performance_Score'] < 4.5),
    (df['Performance_Score'] < 4.0)
]
choices = ['Excellent', 'Good', 'Satisfactory']
df['Rating'] = np.select(conditions, choices, default='Unrated')

print("Final Modified DataFrame:")
print(df)
```
