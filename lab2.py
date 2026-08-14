# Simple Grocery Shop Billing Calculator

print("===== GROCERY SHOP BILL =====")

customer = input("Enter Customer Name: ")

item = input("Enter Item Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Item: "))

# Arithmetic Operators
total_bill = quantity * price

# Discount Calculation
if total_bill >= 1000:
    discount = total_bill * 0.10      # 10% discount
elif total_bill >= 500 and total_bill < 1000:
    discount = total_bill * 0.05      # 5% discount
else:
    discount = 0

# Final Amount
final_amount = total_bill - discount

# Output
print("\n===== BILL =====")
print("Customer Name :", customer)
print("Item          :", item)
print("Quantity      :", quantity)
print("Price         : ₹", price)
print("Total Bill    : ₹", total_bill)
print("Discount      : ₹", discount)
print("Final Amount  : ₹", final_amount)

# Relational and Logical Operators
if final_amount > 0 and quantity > 0:
    print("Status : Payment Successful")
else:
    print("Invalid Input")