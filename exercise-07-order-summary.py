# Exercise 7: Order Summary

orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# 1. Print every order ID and customer
print("--- All Orders ID and Customer ---")
for order_id, details in orders.items():
    print(f"Order ID: {order_id}, Customer: {details['customer']}")


# 2. Print only completed orders
print("\n--- Completed Orders ---")
for order_id, details in orders.items():
    if details["status"] == "Completed":
        completed_orders={order_id: details}

for order_id, details in completed_orders.items():
    print(f"Order ID: {order_id}, Customer: {details['customer']}, Amount: {details['amount']}, Status: {details['status']}")


# 3. Calculate the total amount of completed orders
total_completed_amount = sum(details["amount"] for details in completed_orders.values())
for details in completed_orders.values():
    total_completed_amount += details["amount"]

print(f"\nTotal Amount of Completed Orders: NPR {total_completed_amount:,}")

# 4. Count pending orders
pending_count = sum(1 for details in orders.values() if details["status"] == "Pending")
print(f"Total Pending Orders: {pending_count}")


# 5. Add a new order to the dictionary
orders["ORD-004"] = {
    "customer": "Sagar",
    "amount": 4100,
    "status": "Pending"
}

print(f"\nAdded new order 'ORD-004'. Total orders now: {len(orders)}")