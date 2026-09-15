import socket

# Create UDP socket for client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Client uses a different port
client_address = ("localhost", 10000)

# Bind client socket
client_socket.bind(client_address)

print("UDP Client started...")

# Keep client running in loop
while True:

    # Take string from user
    message = input("\nEnter a string (type exit to stop): ")

    # Stop client
    if message.lower() == "exit":
        break

    # Send message to server
    client_socket.sendto(
        message.encode(),
        ("localhost", 9999)
    )

    # Receive response from server
    data, server_address = client_socket.recvfrom(1024)

    print("Server response:", data.decode())

# Close client socket
client_socket.close()
