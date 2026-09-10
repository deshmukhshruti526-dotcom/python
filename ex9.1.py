# Create an empty list
transactions = []

# Ask the user for 5 transaction amounts
print("Enter 5 transaction amounts:")
t1 = float(input("Transaction 1: "))
t2 = float(input("Transaction 2: "))
t3 = float(input("Transaction 3: "))
t4 = float(input("Transaction 4: "))
t5 = float(input("Transaction 5: "))

# Store the values in the list
transactions = [t1, t2, t3, t4, t5]

# Calculate the largest and average values
largest = max(transactions)
average = sum(transactions) / 5

# Output the results
print("\n--- Summary ---")
print("Largest Amount: " + str(largest))
print("Average Spend: " + str(average))