seats = [
    ["a","a","r"],
    ["a","r","r"],
    ["r","a","r"]
]

for row in seats:
    print(row)

r = int(input("Enter row (1-3): ")) - 1
c = int(input("Enter column (1-3): ")) - 1

if seats[r][c] == "a":
    seats[r][c] = "r"
    print("Seat Reserved")
else:
    print("Already Reserved")