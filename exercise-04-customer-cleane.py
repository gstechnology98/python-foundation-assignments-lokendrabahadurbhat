# Given raw values
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

# Clean the values
name = raw_name.strip().title()
city = raw_city.strip().capitalize()
age = int(raw_age.strip())
email = raw_email.strip().lower()

# Use a ternary expression for the adult status (Age >= 18)
status = "Adult" if age >= 18 else "Minor"

# Display the cleaned record using f-strings
print(f"Name: {name}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Status: {status}")