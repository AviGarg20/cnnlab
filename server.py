import socket

# Create UDP socket for server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server IP and port
server_address = ("localhost", 9999)

# Bind socket to server port
server_socket.bind(server_address)

print("UDP Server started...")
print("Server is waiting for client...")

# Keep server running in loop
while True:

    # Receive data from client
    data, client_address = server_socket.recvfrom(1024)

    message = data.decode()

    print("\nClient connected from:", client_address)
    print("Message received:", message)

    # Reverse the string
    reversed_string = message[::-1]

    # Send result back to client
    server_socket.sendto(
        reversed_string.encode(),
        client_address
    )

    print("Reversed string sent:", reversed_string)
