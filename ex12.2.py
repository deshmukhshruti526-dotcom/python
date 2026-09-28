# Store IP address and port
server = ("192.168.1.1", 8080)

# Unpacking the tuple
ip_address, port = server

# Display server details
print("IP Address:", ip_address)
print("Port Number:", port)

# Demonstrate tuple immutability
try:
    server[0] = "192.168.1.2"
except TypeError:
    print("Error: Tuple cannot be modified")

# Display original settings
print("Original Server Settings:", server)