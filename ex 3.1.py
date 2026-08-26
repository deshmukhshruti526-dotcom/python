age = int(input("Enter applicant's age: "))
income = float(input("Enter annual family income (₹): "))

if age < 25 and income < 300000:
    print("Eligible for the specialized education scholarship scheme.")
else:
    print("Not eligible for the specialized education scholarship scheme.")