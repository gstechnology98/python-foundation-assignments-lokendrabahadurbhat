# Retry Simulation
attempt = 1
max_attempts = 3
operation_successful = False


# Loop through attempts until the maximum number of attempts is reached
while attempt <= max_attempts:
    print(f"Attempt {attempt}")
    
    # Simulating success on the second attempt (as requested in the stretch goal)
    if attempt == 2:
        operation_successful = True
        break
        
    attempt += 1

# Display final message based on operation status
if operation_successful:
    print("Operation completed successfully")
else:
    print("Operation failed after three attempts")