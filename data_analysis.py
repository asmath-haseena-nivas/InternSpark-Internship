import pandas as pd

# Load CSV file
data = pd.read_csv("students.csv")

# Display dataset
print("Student Marks Data")
print(data)

# Calculate average marks
data["Average"] = (data["Maths"] + data["Science"] + data["English"]) / 3

print("\nAverage Marks")
print(data[["Name", "Average"]])

# Highest average
top_student = data.loc[data["Average"].idxmax()]

print("\nTop Student")
print(top_student)
