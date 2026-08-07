# Function to calculate and classify pipeline health
def check_pipeline_health(rows_loaded, rows_failed, runtime_minutes):
    total_rows = rows_loaded + rows_failed
    failure_rate = (rows_failed / total_rows) * 100
    if failure_rate <= 2 and runtime_minutes <= 20:
        status = "Healthy"
    elif failure_rate <= 5:
        status = "Warning"
    else:
        status = "Critical"
        
    print(f"Rows Loaded: {rows_loaded}")
    print(f"Rows Failed: {rows_failed}")
    print(f"Runtime: {runtime_minutes} minutes")
    print(f"Failure Rate: {failure_rate:.2f}%")
    print(f"Pipeline Status: {status}")
    print("-" * 30)


# Test Case 1: Initial given values
# rows_loaded = 9800, rows_failed = 200, runtime_minutes = 18
print("--- Test Case 1 ---")
check_pipeline_health(9800, 200, 18)

# Test Case 2: First test case from prompt
# rows_loaded = 9500, rows_failed = 500, runtime_minutes = 15
print("--- Test Case 2 ---")
check_pipeline_health(9500, 500, 15)

# Test Case 3: Final test case from prompt (Low failure rate, high runtime)
# rows_loaded = 9900, rows_failed = 100, runtime_minutes = 30
print("--- Test Case 3 ---")
check_pipeline_health(9900, 100, 30)