food = 0
travel = 0
shopping = 0

print("Enter expenses for each category.")
print("Enter 0 to stop.")

while True:
    print("\n1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter Food expense: ₹"))
        food += amount

    elif choice == 2:
        amount = float(input("Enter Travel expense: ₹"))
        travel += amount

    elif choice == 3:
        amount = float(input("Enter Shopping expense: ₹"))
        shopping += amount

    elif choice == 4:
        break

    else:
        print("Invalid choice!")

total = food + travel + shopping

print("\n================================")
print("       MONTHLY EXPENSE SUMMARY")
print("================================")
print("Food       : ₹", food)
print("Travel     : ₹", travel)
print("Shopping   : ₹", shopping)
print("--------------------------------")
print("Total      : ₹", total)
print("================================")