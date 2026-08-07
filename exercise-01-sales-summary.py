# Create variables for the product
product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

# Calculate sales metrics
gross_sales = unit_price * quantity_sold
discount_amount = gross_sales * discount_percentage
final_sales_amount = gross_sales - discount_amount

# Display the output using an f-string matching the expected format
print(f"Product: {product_name}")
print(f"Gross sales: NPR {gross_sales:.2f}")
print(f"Discount: NPR {discount_amount:.2f}")
print(f"Final sales: NPR {final_sales_amount:.2f}")