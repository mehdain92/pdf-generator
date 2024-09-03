import os
import socket
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# font_config = FontConfiguration()
# Define the path for the Unix socket
SOCKET_PATH = '/tmp/html_to_pdf_socket'

# Ensure the socket does not already exist
if os.path.exists(SOCKET_PATH):
    os.remove(SOCKET_PATH)

# Create a Unix socket
server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind the socket to the path
server_socket.bind(SOCKET_PATH)

# Listen for incoming connections
server_socket.listen(1)
print(f"Listening on {SOCKET_PATH}...")

while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()
    try:
        print("Connection established.")
        
        # Receive the HTML data
        html_data = connection.recv(4096).decode('utf-8')
        print("Received HTML data.")

        # Convert HTML to PDF
        pdf_output = HTML(string=html_data, base_url="file:///home/hasan/PhpstormProjects/novin/public/").write_pdf()

        # Send the PDF back through the socket
        connection.sendall(pdf_output)
        print("PDF sent back to the client.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up the connection
        connection.close()
