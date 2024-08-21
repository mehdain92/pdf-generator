import socket

# Define the path for the Unix socket
SOCKET_PATH = '/tmp/html_to_pdf_socket'

# Create a Unix socket
client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(SOCKET_PATH)

# Sample HTML data
html_data = """
<!DOCTYPE html>
<html>
<head>
    <title>Test PDF</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a test PDF generated from HTML.</p>
</body>
</html>
"""

# Send HTML data to the server
client_socket.sendall(html_data.encode('utf-8'))

# Receive the PDF data
pdf_data = bytearray()
while True:
    part = client_socket.recv(4096)
    if not part:
        break
    pdf_data.extend(part)

# Save the PDF to a file
with open('output.pdf', 'wb') as f:
    f.write(pdf_data)

print("PDF received and saved as 'output.pdf'.")

# Close the client socket
client_socket.close()
