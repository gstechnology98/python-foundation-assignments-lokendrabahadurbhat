# Exercise 4: Sales Analysis

monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# 1. Sorted list from highest to lowest
sorted_sales = sorted(monthly_sales, reverse=True)

# 2. List containing only values above 100000 using list comprehension
for sale in monthly_sales:
    if sale > 100000:
        high_sales= sale



# 3. List where each amount has 13% tax added (amount * 1.13) using list comprehension
for sale in monthly_sales:
    sales_with_tax= round(sale * 1.13, 2)


# 4. Total sales amount using sum()
total_sales = sum(monthly_sales)


# 5. Average sales amount using sum() and len()
average_sales = total_sales / len(monthly_sales)

# Display the outputs
print(f"Original Sales: {monthly_sales}")
print(f"Sorted Sales (Highest to Lowest): {sorted_sales}")
print(f"Sales Above 100,000: {high_sales}")
print(f"Sales with 13% Tax Added: {sales_with_tax}")
print(f"Total Sales Amount: NPR {total_sales:,.2f}")
print(f"Average Sales Amount: NPR {average_sales:,.2f}")