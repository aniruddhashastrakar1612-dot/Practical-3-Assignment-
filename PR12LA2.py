import pandas as pd

# Read CSV file (since your file is employees.csv)
df = pd.read_csv("employees.csv")

# Display full data
print("Employee Data:\n")
print(df)

# a) Employees in Automotive domain
print("\nEmployees in Automotive domain:")
auto_emp = df[df["Department"] == "Automotive"]
print(auto_emp)

# b) Details using Employee ID
emp_id = int(input("\nEnter Employee ID: "))

emp = df[df["Employee ID"] == emp_id]
print("\nEmployee Details:")
print(emp)

# d) List of Developers
print("\nList of Developers:")
developers = df[df["Designation"] == "Developer"]
print(developers)