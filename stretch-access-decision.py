def check_access(user_role, is_active, requested_dataset):
    # Define allowed roles and restricted datasets
    allowed_roles = ["analyst", "scientist", "engineer"]
    restricted_datasets = ["salary_data", "personal_data"]

    # Check access conditions and provide specific denial reasons
    if not is_active:
        print(f"Access denied because the user is inactive. (Role: {user_role}, Dataset: {requested_dataset})")
    elif user_role not in allowed_roles:
        print(f"Access denied because the role is not allowed. (Role: {user_role}, Dataset: {requested_dataset})")
    elif requested_dataset in restricted_datasets:
        print(f"Access denied because the dataset is restricted. (Role: {user_role}, Dataset: {requested_dataset})")
    else:
        print(f"Access granted to dataset: {requested_dataset} for user role: {user_role}")
    print("-" * 50)



# --- Test Scenarios ---

# Scenario 1: Valid access (All conditions met)
print("--- Scenario 1: Valid Access ---")
check_access(user_role="analyst", is_active=True, requested_dataset="sales_data")

# Scenario 2: Inactive user
print("--- Scenario 2: Inactive User ---")
check_access(user_role="analyst", is_active=False, requested_dataset="sales_data")

# Scenario 3: Disallowed role
print("--- Scenario 3: Disallowed Role ---")
check_access(user_role="intern", is_active=True, requested_dataset="sales_data")

# Scenario 4: Restricted dataset
print("--- Scenario 4: Restricted Dataset ---")
check_access(user_role="scientist", is_active=True, requested_dataset="salary_data")