total_expense = 0
expense_count = 0

print("Enter daily expenses.")
print("Enter 0 to stop.")

while True:
    expense = float(input("Enter expense amount: "))

    if expense == 0:
        break

    total_expense += expense
    expense_count += 1

print("\n----- Monthly Expense Summary -----")
print("Total Monthly Expenditure: ₹", total_expense)
print("Number of Expenses Recorded:", expense_count)