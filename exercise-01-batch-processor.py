# Loop through batch numbers from 1 to 10
for batch_number in range(1, 11):
    print(f"Processing batch {batch_number}")
    
    # Check if the batch number is a multiple of 3 using the modulo operator
    if batch_number % 3 == 0:
        print("Checkpoint reached")