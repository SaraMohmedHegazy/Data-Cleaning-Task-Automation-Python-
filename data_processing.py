import pandas as pd

# Step 1: Load the data from CSV file
df = pd.read_csv('Employees.csv')

# Step 2: Remove duplicates
df = df.drop_duplicates()

# Step 3: Remove decimal places in the Age column
df['Age'] = df['Age'].apply(lambda x: int(x))

# Step 4: Convert 'Salary(USD)' to EGP (1 USD = 30.85 EGP for example)
conversion_rate = 30.85
df['Salary_EGP'] = df['Salary(USD)'] * conversion_rate

# Step 5: Calculate and print statistics
# Average age
average_age = df['Age'].mean()
print(f'Average Age: {average_age}')

# Median salary (in EGP)
median_salary = df['Salary_EGP'].median()
print(f'Median Salary (EGP): {median_salary}')

# Gender ratio (Males to Females)
gender_counts = df['Gender'].value_counts()
male_female_ratio = gender_counts.get('Male', 0) / gender_counts.get('Female', 1)
print(f'Ratio of Males to Females: {male_female_ratio}')

# Step 6: Save the modified data to a new CSV file
df.to_csv('modified_data.csv', index=False)

# Optional: Print the first few rows of the new DataFrame to verify
print(df.head())
df.to_csv('modified_data.csv', index=False)
