# Working of break statement for for loop

for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("Loop Ended")


# Working of break statement for while loop

count = 1

while count <= 5:
    if count == 3:
        break
    print(count)
    count += 1

print("Loop Terminated")