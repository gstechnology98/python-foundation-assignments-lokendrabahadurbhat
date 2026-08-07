#Create Variable
total_rows = 2000
missing_rows = 120
duplicate_rows = 30

# Calculate total number and percentage of problematic rows (assuming no overlap)
problematic_rows = missing_rows + duplicate_rows
problem_percentage = (problematic_rows / total_rows) * 100


# Classify the dataset based on the rules
if problem_percentage <= 2:
    final_classification = "Excellent"
elif problem_percentage <= 5:
    final_classification = "Acceptable"
else:
    final_classification = "Needs Cleaning"


# Display the output using f-strings
print(f"Total rows: {total_rows}")
print(f"Problematic rows: {problematic_rows}")
print(f"Problem percentage: {problem_percentage:.2f}%")
print(f"Final classification: {final_classification}")