# Traffic Signal Simulation System

print("===== Traffic Signal Simulation =====")

signal = input("Enter Signal Color (Red/Yellow/Green): ").lower()

if signal == "red":
    print("Action : STOP")
elif signal == "yellow":
    print("Action : WAIT")
elif signal == "green":
    print("Action : GO")
else:
    print("Invalid Signal Color")