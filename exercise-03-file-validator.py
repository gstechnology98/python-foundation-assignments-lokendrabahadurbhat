# Ask the user to enter a file name and normalize it
file_name = input("Enter a file name: ").strip().lower()

# Define the allowed file extensions
allowed_extensions = (".csv", ".json", ".parquet")

# Check if the file name ends with any of the allowed extensions
if file_name.endswith(allowed_extensions):
    print(f"Valid file: {file_name}")
else:
    print(f"Invalid file: {file_name}. Allowed formats are .csv, .json, and .parquet.")